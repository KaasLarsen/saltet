<!-- BEGIN:nextjs-agent-rules -->

# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->

## Cursor Cloud specific instructions

- Node.js 22+ is required by `@supabase/supabase-js`. The default image already provides it; do not install another Node toolchain.
- Install with `npm ci`. If `.env.local` is missing, copy `.env.example`. Supabase keys are optional: without a URL and anon key, recipe ratings stay empty in local dev. Do not put real keys in the repo.
- Dev server: `npm run dev` (listens on `0.0.0.0:3000`). Open `/`, search for `flæsk`, and open a recipe such as `/opskrifter/ovn/stegt-flaesk-ovn`.
- `npm test` checks rating-format helpers. `npm run lint` currently fails on existing `react-hooks/set-state-in-effect` errors in the filter components.
- `npm run build` statically generates every recipe (about 1700 MDX files) and takes a long time. Do not run it at the same time as `npm run dev`; they share the Next.js output directory.
