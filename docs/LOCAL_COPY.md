# Local Copy Boundaries

Snapshot date: 12-Oct-2026. This folder preserves the latest frontend, API, contracts, database migrations, company logo and 2026 holiday import. It is not an old Git checkout and does not contain the existing local or cloud database.

Included: `frontend/`, `backend/`, `contracts/`, the backend's Python API contract export utility and new local setup documentation. Startup and maintenance commands are documented directly in the README; no PowerShell helpers or `scripts/` folder are required.

Excluded: Netlify edge functions/config, Render deployment/start script, Neon infrastructure npm package/config/context, Git/GitHub workflows/history, agent configuration, old hosting documents, temporary operator files, personal environment files, OAuth credentials, logs, caches, installed dependencies and build artifacts.

Local adaptations: frontend launch binds to 127.0.0.1; frontend development origins are loopback only; the documented backend startup command binds to 127.0.0.1; settings reject remote database hosts and non-development mode. Provider-specific comments are removed from local configuration examples. Existing session/CSRF/role/location protections and integration implementations remain intact for future adaptation.

`backend/.env` and `frontend/.env.local` were generated from sanitized defaults, not copied from the original files. Maps/Gmail/SMTP/database credentials remain blank. The source application and running hosted services were not edited, redeployed or reconfigured when making this folder.

Install dependencies anew and configure a new local database to complete runtime acceptance. A blank database URL intentionally reports unavailable readiness instead of quietly borrowing another environment. Future provider setup must be reviewed separately before any credentials or employee data are transferred.

Verification: backend Ruff lint/format, mypy, OpenAPI contract, frontend ESLint and TypeScript checks passed. The Next.js Webpack build passed; this copy uses Webpack for dev/build because the Turbopack CSS worker failed on the current Windows setup. Known private configuration scans found no matches. Blank integration fields and remote-database rejection were checked. Database-backed runtime workflows remain pending until the organization supplies a new local database.
