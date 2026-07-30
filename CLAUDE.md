# ShowMinder Project Notes

Django app to track watched TV shows via TMDB. Two Django apps: `frontend` (htmx-driven UI) and `api`.

## Stack

- Django 6.0.3, Python 3.13+, managed with `uv`.
- `django-htmx`, `django-bootstrap-v5` (forked, see `pyproject.toml` `[tool.uv.sources]` for Django 5/6 compat fixes), `whitenoise` for static files.
- Postgres in prod (`DB_HOST`/`DB_USER`/`DB_PASSWORD` env vars), sqlite (`db.sqlite3`) locally.
- `gunicorn` behind `honcho` (see `Procfile`), served from a plain Docker image (`Dockerfile`) — no TLS at the app level.
- Tests: `pytest` + `pytest-django` (`pytest.ini` sets `DJANGO_SETTINGS_MODULE=showminder.settings`).

## Deployment

- Deployed on k3s with Traefik as ingress, config lives in a separate repo: `myfarm/k3s/showminder.yaml` (+ `myfarm/k3s/traefik.yaml` for the cluster-wide default TLS cert `ca-net-tls`).
- Traefik terminates TLS and proxies to gunicorn over **plain HTTP** inside the cluster (`containerPort 8000`). The IngressRoute listens on both `web` and `websecure` entrypoints with no explicit redirect between them.
- Public host: `showminder.ca-net.org` (also reachable internally as `showminder-new`).
- `ALLOWED_HOSTS = ["*"]` — intentionally permissive since Traefik is the only ingress path.

## Frontend patterns

- htmx (`htmx.org@1.6.0`, loaded in `templates/bootstrap.html`) drives all dynamic UI — no custom JS framework.
- CSRF token is injected into every htmx request via a `htmx:configRequest` listener in `bootstrap.html` that sets the `X-CSRFToken` header from `{{ csrf_token }}`.
- Search-as-you-type inputs use `hx-trigger` with a `delay` modifier; prefer `input changed delay:...ms[, keyup[key=='Enter']]` over `keyup changed` — iOS Safari does not reliably fire `keyup` for the virtual keyboard in all cases (see `add.html`, `detail.html`).
- `showminder.middleware.NoCacheHTMLMiddleware` forces `Cache-Control: no-cache, no-store, must-revalidate` on all `text/html` responses — added because Safari's "Add to Home Screen"/"Add to Dock" web-app mode aggressively caches HTML otherwise.

## Known issue: POST requests failing only in prod (over HTTPS) — FIXED 2026-07-30

**Symptom:** htmx searches that use `hx-post` (`add.html`, `detail.html`) returned no results / silently did nothing when used over the internet on prod, but worked fine when tested against `localhost` dev. `hx-get`-based search (`index.html`'s filter box) worked fine in both places.

**Root cause:** `settings.py` had no `SECURE_PROXY_SSL_HEADER`, so Django always computed `request.is_secure() == False`, even in prod where Traefik terminates real HTTPS. Django's `CsrfViewMiddleware._origin_verified()` compares the browser's `Origin` header against an expected origin built as `"https" if request.is_secure() else "http"` + host. Browsers attach `Origin` to POST/fetch requests (not to plain GETs), so:
- Prod: browser sends `Origin: https://showminder.ca-net.org`, Django expects `http://showminder.ca-net.org` → mismatch → CSRF 403 → htmx swap does nothing.
- Dev (`http://localhost`): both sides agree on `http://` → works.
- `index.html`'s `hx-get` search: no `Origin` header on GET → check never runs → always "works", masking the real bug.

**Fix:** set `SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")` in `settings.py`, since Traefik is the sole ingress and sets `X-Forwarded-Proto` itself (not spoofable by external clients, as gunicorn is only reachable via the internal ClusterIP).

**Lesson:** when a bug only reproduces over a real HTTPS deployment and not on `http://localhost`, check `SECURE_PROXY_SSL_HEADER`/reverse-proxy trust settings before assuming it's a client/browser quirk. GET vs. POST behaving differently is a strong signal to look at CSRF's `Origin` header check specifically.

## Testing note

No meaningful automated test exists (or is feasible) for browser-side event-binding or CSRF-origin bugs like the one above — Django's test client doesn't run a browser/JS engine and doesn't send `Origin` headers or model reverse-proxy header trust the way a real browser + Traefik does. Verify HTTPS/CSRF-proxy behavior against the actual deployed prod environment, not via `pytest`.
