# Organization-Owned Configuration

The supplied environment files contain local defaults and **blank credentials**. None of the owner's existing provider credentials or personal account details were copied.

| Setting | Who supplies it | Initial state |
| --- | --- | --- |
| Local PostgreSQL database/user/password | Organization or local operator | `DATABASE_URL` blank; new localhost database required |
| Super Admin email, password and PIN | Organization administrator | No account exists; operator bootstrap and private activation required |
| Office timezone, location, radius/accuracy and approved network | Organization | Database starts empty; configure through System Settings |
| Google Maps browser key and map ID | Organization Google Cloud project | Both blank |
| Gmail OAuth client ID, client secret, refresh token and sender | Organization Google account/project | All blank |
| SMTP host, username, app password and sender | Organization mail administrator | All blank; port 587 and STARTTLS are non-secret defaults |

Keep `EMAIL_PROVIDER=smtp` until an email option is selected. For Gmail API, set it to `gmail_api` only after the organization completes its own private OAuth setup with Gmail send permission. The previous sender, OAuth JSON, refresh token and SMTP password must not be reused. A Google app password is for SMTP, not a replacement for a Gmail API refresh token.

Maps requires the organization's own enabled Google APIs, website/API restrictions and cost approval. For local use, restrict the browser key to the exact localhost/127.0.0.1 origins used. A browser Maps key is visible by design; Gmail secrets and database credentials must stay backend-only. Browser location permission is separate from the office map picker.

Do not commit actual environment files, OAuth JSON files, records, database exports or operational logs. Only sanitized `.env.example` files belong in source control. Restart the relevant local process after changing configuration; public frontend variables are embedded during a build.

Questions for the organization before future hosting: chosen hosting product and server capability, budget, domain, database ownership/backup policy, mail sender/provider, Google project ownership and approved data retention. No answers are needed to keep this source copy independent; a local database is required before accounts and attendance can run.
