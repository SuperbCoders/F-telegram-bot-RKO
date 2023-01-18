FROM python:3.8.3-slim AS python_base

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Workaround for https://github.com/debuerreotype/debuerreotype/issues/10
RUN seq 1 8 | xargs -I{} mkdir -p /usr/share/man/man{}

RUN apt-get update && apt-get install -y \
  # general dependencies
  ca-certificates \
  build-essential python3-dev \
  # psycopg2 dependencies
  python3-psycopg2 \
  # CFFI dependencies
  python-cffi \
  # https://docs.djangoproject.com/en/dev/ref/django-admin/#dbshell
  postgresql-client


WORKDIR /usr/src/app

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY ./django/pyproject.toml /usr/src/app/pyproject.toml
COPY ./django/poetry.lock /usr/src/app/poetry.lock

RUN poetry install

COPY ./django /usr/src/app/

# Django image
FROM python_base AS django

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

# Celery image
FROM python_base as celery

ENV COLUMNS=80
RUN useradd -ms /bin/bash celery
USER celery

# Telegram bot image
FROM python_base as telegram
