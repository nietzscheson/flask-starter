FROM python:3.9.2 as base

ARG NAME

ENV PYTHONUNBUFFERED=1 \
    NAME=$NAME \
    FLASK_APP=/home/core/app.py \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.13 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VENV_PATH="/opt/pysetup/.venv"


ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"


FROM base as builder-base

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml ./

RUN poetry lock && poetry install --no-dev

FROM base as development

ENV FLASK_ENV=development
WORKDIR $PYSETUP_PATH

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

RUN poetry install

RUN useradd --create-home core
WORKDIR /home/core
USER core

COPY . ./

ENTRYPOINT ["sh","./entrypoint.sh" ]

CMD [ "flask run --host 0.0.0.0" ]

# FROM base as production

# ENV FLASK_ENV=production
# COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
# RUN useradd --create-home core
# WORKDIR /home/core
# USER core
# COPY . ./
# CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "main:app"]
