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
