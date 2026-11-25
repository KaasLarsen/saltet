-- Saltet newsletter subscribers (email capture only — no sending).
-- Run in Supabase SQL editor for the saltet project.

create table if not exists public.newsletter_subscribers (
  email text not null primary key,
  created_at timestamptz not null default now(),
  source text not null default 'footer',
  unsubscribed_at timestamptz
);

create index if not exists newsletter_subscribers_created_at_idx
  on public.newsletter_subscribers (created_at desc);

alter table public.newsletter_subscribers enable row level security;

-- No direct table access for anon; only via SECURITY DEFINER RPC.
revoke all on public.newsletter_subscribers from anon, authenticated;
grant usage on schema public to anon, authenticated;

create or replace function public.newsletter_subscribe(
  p_email text,
  p_source text default 'footer'
)
returns json
language plpgsql
security definer
set search_path = public
as $$
declare
  v_email text;
  v_source text;
begin
  v_email := lower(trim(coalesce(p_email, '')));
  if v_email is null
     or length(v_email) < 3
     or length(v_email) > 254
     or position('@' in v_email) < 2
     or v_email !~ '^[^@\s]+@[^@\s]+\.[^@\s]+$'
  then
    raise exception 'invalid_email';
  end if;

  v_source := lower(trim(coalesce(p_source, 'footer')));
  if v_source is null or length(v_source) = 0 or length(v_source) > 40 then
    v_source := 'footer';
  end if;
  if v_source !~ '^[a-z0-9_-]+$' then
    v_source := 'footer';
  end if;

  insert into public.newsletter_subscribers (email, source, created_at)
  values (v_email, v_source, now())
  on conflict (email) do nothing;

  -- Idempotent: already subscribed still returns ok (no email enumeration).
  return json_build_object('ok', true);
end;
$$;

grant execute on function public.newsletter_subscribe(text, text) to anon, authenticated;
