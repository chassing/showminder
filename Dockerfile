FROM python:3.13-slim
COPY --from=ghcr.io/astral-sh/uv:0.8.22@sha256:9874eb7afe5ca16c363fe80b294fe700e460df29a55532bbfea234a0f12eddb1 /uv /bin/uv

ENV \
    PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=utf-8 \
    DJANGO_SETTINGS_MODULE=showminder.settings \
    # disable uv cache. it doesn't make sense in a container
    UV_NO_CACHE=true \
    UV_NO_MANAGED_PYTHON=true \
    UV_PYTHON_DOWNLOADS=never


RUN adduser --shell /bin/sh --disabled-password chris
RUN apt update && apt install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

ADD LICENSE README.md Procfile ./

ADD pyproject.toml uv.lock ./
RUN uv sync --frozen --no-group dev

ADD showminder ./showminder
RUN uv run ./showminder/manage.py collectstatic --noinput

EXPOSE 8000

USER chris

CMD ["uv", "run", "honcho", "start"]
