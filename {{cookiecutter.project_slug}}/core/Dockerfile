### https://github.com/andreyors/docker-flask-multistage

# FROM python:3.9.2 as python-base
#
# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1 \
#     PIP_NO_CACHE_DIR=off \
#     PIP_DISABLE_PIP_VERSION_CHECK=on \
#     PIP_DEFAULT_TIMEOUT=100 \
#     POETRY_HOME="/opt/poetry" \
#     POETRY_VIRTUALENVS_IN_PROJECT=true \
#     POETRY_NO_INTERACTION=1 \
#     PYSETUP_PATH="/opt/pysetup" \
#     VENV_PATH="/opt/pysetup/.venv" \
#     PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
#
# FROM python-base as builder-base
# RUN apt-get update \
#     && apt-get install --no-install-recommends -y \
#         curl \
#         build-essential
#
# ENV POETRY_VERSION=1.2.0a2
# RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
#
# WORKDIR $PYSETUP_PATH
# COPY ./poetry.lock ./pyproject.toml ./
# RUN poetry install --no-dev  # respects
#
# FROM python-base as development
#
# # Copying poetry and venv into image
# COPY --from=builder-base $POETRY_HOME $POETRY_HOME
# COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH

# COPY poetry.lock pyproject.toml ./
#
# # RUN poetry install --no-dev --no-root
# RUN python -m venv ${VENV_PATH} \
#     && . /opt/venv/bin/activate \
#     && pip install --upgrade pip \
#     && pip install poetry==${POETRY_VERSION} \
#     && poetry install --no-dev --no-ansi
#
# FROM python-base as development
#
# COPY --from=python-base $VENV_PATH $VENV_PATH
#
# # RUN poetry install --remove-untracked
#
# # COPY . ./
#
# # CMD flask db upgrade; flask run --host 0.0.0.0
#
# # RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
# #     POETRY_HOME="/opt/poetry" \
# #     POETRY_VIRTUALENVS_IN_PROJECT=false \
# #     POETRY_NO_INTERACTION=1 \
# #     WORKDIR="/home/core" \
# #     VENV_PATH="/home/core/.venv"
#
# # WORKDIR $WORKDIR
# #
# # ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"
# #
# # FROM python-base as builder-base
# #
# # RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python
# #
# # COPY poetry.lock pyproject.toml ./
# #
# # RUN poetry install --no-dev --no-root
# #
# # FROM python-base as development
# #
# # COPY --from=builder-base $POETRY_HOME $POETRY_HOME
# # COPY --from=builder-base $WORKDIR $WORKDIR
# #
# # RUN poetry install --remove-untracked
# #
# # COPY . ./
# #
# # CMD flask db upgrade; flask run --host 0.0.0.0
# #
#

FROM python:3.9.2 as python-base

ARG NAME
ENV NAME=$NAME
ENV FLASK_APP=/home/core/app.py

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN pip install --upgrade pip

RUN pip install poetry==1.2.0a2

WORKDIR /home/core

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false

RUN poetry install --no-root --no-dev

FROM python-base as development

ENV FLASK_ENV=development

RUN poetry install

COPY . ./

CMD flask db upgrade; flask run --host 0.0.0.0
