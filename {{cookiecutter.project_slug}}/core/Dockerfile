FROM python:3.9 as base

ARG NAME
ENV NAME=$NAME
ENV FLASK_APP=/core/app.py
ENV FLASK_ENV=development


RUN pip3 install --upgrade pip pipenv

RUN apt-get update && apt-get install -y --no-install-recommends gcc

WORKDIR /core

COPY Pipfile* .

RUN pipenv lock
RUN pipenv install --system --deploy

COPY . .

FROM base as development

CMD flask run --host 0.0.0.0

FROM base as debug

RUN pip3 install debugpy

ENTRYPOINT ["python", "-m", "debugpy", "--listen", "0.0.0.0:5678", "--wait-for-client", "-m", "unittest", "discover"]
