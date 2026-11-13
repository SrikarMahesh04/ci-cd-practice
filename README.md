# Virtue ClockIn — Local Development Copy

[![CI Pipeline](https://github.com/SrikarMahesh04/ci-cd-practice/actions/workflows/ci.yml/badge.svg)](https://github.com/SrikarMahesh04/ci-cd-practice/actions/workflows/ci.yml)

Created 12-Oct-2026 from the current application. This is an independent source copy for organization-owned development and future hosting decisions. It retains the current features rather than reverting to an older implementation.

No Git history, deployment workflows, hosting configuration, cloud project links, credentials, installed dependencies, database records, employee accounts or logs are included. Changes here do not update the existing hosted application. No hosting provider has been selected for this copy.

## Requirements

- Node.js 20+ and npm.
- Python 3.12+ and uv.
- A new local PostgreSQL database, with organization-approved credentials.

The frontend uses npm with `package-lock.json`. The backend uses uv. Install dependencies inside this folder; do not share the original application's virtual environment or database.

## First setup

1. Create a **new empty PostgreSQL database on this computer** using PostgreSQL administration tools. Choose its own database name and credentials. Do not reuse the live database or import existing employee records.
2. Edit `backend/.env`: fill `DATABASE_URL` with the new local database connection URL. For example, its structure is `postgresql://<user>:<password>@localhost:5432/<new_database>`. Replace placeholders privately; URI-encode special characters in credentials. All provider credentials are deliberately blank.
3. Install locked dependencies and apply migrations:

```powershell
cd backend
uv sync --frozen
uv run --frozen alembic upgrade head
cd ../frontend
pnpm install --frozen-lockfile
cd ..
```

4. Open two terminals in this folder (your editor's terminal, Command Prompt or PowerShell all work). Start the backend in one:

```powershell
cd backend
uv run --frozen uvicorn app.main:app --host 127.0.0.1 --port 8000
```

```powershell
cd frontend
pnpm dev
```

Open `http://localhost:3000`. Backend health is `http://127.0.0.1:8000/health`; readiness is `/ready` and needs the database. These commands bind to loopback, not the public internet or LAN. Settings reject remote database addresses and non-development mode in this copy; a future hosting adaptation must deliberately revise this local-only guard.

## Moving this folder

Move the entire `local-only` folder to your preferred location, including hidden files such as `.gitignore`, `backend/.env` and `frontend/.env.local`. You may rename the folder. Open that folder as the project in your new Codex chat. Paths are relative to the project; it does not need the original hosted project's folder.

PostgreSQL runs separately: moving this folder does not move a database. If moving to another computer, install the requirements there and configure a new local database. Reinstall dependencies after moving an already configured copy, especially the Python virtual environment. No deployment or Git remote is configured in this copy.

## Initial organization setup

From `backend/`, bootstrap the first Super Admin using the organization's real name and email:

```powershell
uv run --frozen python -m app.cli bootstrap --email <organization-admin-email> --name "<organization-admin-name>" --activation-link
```

Keep the printed activation link private. Open it locally and choose a new password and PIN. No default account or credentials are supplied. Then configure office timezone/location/network rules and create shifts and employees. Punch verification remains unavailable until the required settings are supplied.

Import the approved 2026 calendar into this new database when ready:

```powershell
uv run --frozen python -m app.cli import-holidays-2026
```

This adds nine office holidays and five additional optional working days; Ugadi is an office holiday. Matching entries are preserved and conflicting entries stop the import. Nothing is imported automatically during startup.

Email and Maps are optional integrations until the organization provides its own configuration. Their absence is shown truthfully in the UI. For local activation/recovery without configured email, an operator can issue a private single-use link:

```powershell
uv run --frozen python -m app.cli issue-link --email <existing-account-email>
```

## Checks and future changes

Optional maintenance commands, after installing dependencies, from `backend/`:

```text
uv run --frozen ruff check .
uv run --frozen ruff format --check .
uv run --frozen mypy app
uv run --frozen python export_contract.py --check
```

From `frontend/`:

```text
pnpm exec next typegen
pnpm typecheck
pnpm lint
pnpm build
```

The Python utility `backend/export_contract.py` maintains the shared API contract; it does not start either application. Run it without `--check` when intentionally updating OpenAPI. No PowerShell helper scripts or automated test suite are included. Run commands from this copy's folder, not the original workspace.

See [organization configuration](docs/ORGANIZATION_CONFIGURATION.md) and [copy boundaries](docs/LOCAL_COPY.md). Git initialization, publishing, cloud databases, hosting plans and domain setup are separate future decisions. No automatic push or deployment is configured.
