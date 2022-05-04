FROM python:3.9.2 as python-base

RUN apt-get update \
    && apt-get install --no-install-recommends -y \
        curl \
        build-essential

ARG NAME

ENV NAME=$NAME \
    FLASK_APP=/home/core/app.py\
    FLASK_ENV=development \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.1.13 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    WORKDIR="/home/core" \
    VENV_PATH="/home/core/.venv"

WORKDIR $WORKDIR

ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

FROM python-base as builder-base

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

COPY poetry.lock pyproject.toml ./

# RUN poetry install --no-dev --no-root

FROM python-base as development

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $WORKDIR $WORKDIR

RUN poetry install --remove-untracked
#
# RUN useradd --create-home core
# WORKDIR /home/core
# USER core

COPY . ./

ENTRYPOINT ["sh","./entrypoint.sh" ]

CMD [ "flask run --host 0.0.0.0" ]

FROM python-base as production

COPY --from=builder-base $POETRY_HOME $POETRY_HOME
COPY --from=builder-base $WORKDIR $WORKDIR

COPY . ./

ENTRYPOINT ["sh","./entrypoint.sh" ]

CMD [ "gunicorn --bind 0.0.0.0:5000 app:app" ]
