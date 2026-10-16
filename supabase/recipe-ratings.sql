-- Saltet recipe ratings (port of vinbot RPC shape).
-- Run in Supabase SQL editor for the saltet project.

create table if not exists public.recipe_ratings (
  kind text not null check (kind in ('recipe')),
  slug text not null,
  voter_hash text not null,
  ip_hash text,
  rating smallint not null check (rating between 1 and 5),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  primary key (kind, slug, voter_hash)
);

create index if not exists recipe_ratings_slug_idx
  on public.recipe_ratings (kind, slug);

create index if not exists recipe_ratings_ip_cast_idx
  on public.recipe_ratings (ip_hash, updated_at desc);

alter table public.recipe_ratings enable row level security;

-- No direct table access for anon; only via SECURITY DEFINER RPCs.
revoke all on public.recipe_ratings from anon, authenticated;
grant usage on schema public to anon, authenticated;

create or replace function public.recipe_rating_summary(
  p_kind text,
  p_slug text
)
returns json
language sql
stable
security definer
set search_path = public
as $$
  select case
    when count(*) = 0 then json_build_object('average', null, 'count', 0)
    else json_build_object(
      'average', round(avg(rating)::numeric, 1),
      'count', count(*)::int
    )
  end
  from public.recipe_ratings
  where kind = p_kind and slug = p_slug;
$$;

create or replace function public.recipe_rating_mine(
  p_kind text,
  p_slug text,
  p_voter_hash text
)
returns smallint
language sql
stable
security definer
set search_path = public
as $$
  select rating
  from public.recipe_ratings
  where kind = p_kind
    and slug = p_slug
    and voter_hash = p_voter_hash
  limit 1;
$$;

create or replace function public.recipe_rating_cast(
  p_kind text,
  p_slug text,
  p_voter_hash text,
  p_ip_hash text,
  p_rating integer
)
returns json
language plpgsql
security definer
set search_path = public
as $$
declare
  recent_casts int;
begin
  if p_kind is distinct from 'recipe' then
    raise exception 'invalid_kind';
  end if;
  if p_slug is null or length(trim(p_slug)) = 0 or length(p_slug) > 200 then
    raise exception 'invalid_slug';
  end if;
  if p_voter_hash is null or length(p_voter_hash) < 16 then
    raise exception 'invalid_voter';
  end if;
  if p_rating is null or p_rating < 1 or p_rating > 5 then
    raise exception 'invalid_rating';
  end if;

  if p_ip_hash is not null and length(p_ip_hash) >= 16 then
    select count(*)::int into recent_casts
    from public.recipe_ratings
    where ip_hash = p_ip_hash
      and updated_at > now() - interval '1 minute';

    if recent_casts >= 30 then
      raise exception 'rate_limited';
    end if;
  end if;

  insert into public.recipe_ratings as rr (
    kind, slug, voter_hash, ip_hash, rating, created_at, updated_at
  ) values (
    p_kind, p_slug, p_voter_hash, p_ip_hash, p_rating, now(), now()
  )
  on conflict (kind, slug, voter_hash) do update
    set rating = excluded.rating,
        ip_hash = excluded.ip_hash,
        updated_at = now();

  return public.recipe_rating_summary(p_kind, p_slug);
end;
$$;

grant execute on function public.recipe_rating_summary(text, text) to anon, authenticated;
grant execute on function public.recipe_rating_mine(text, text, text) to anon, authenticated;
grant execute on function public.recipe_rating_cast(text, text, text, text, integer) to anon, authenticated;
