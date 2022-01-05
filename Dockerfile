FROM python:3.9

RUN pip3 install --upgrade pipenv

RUN apt-get update && apt-get install -y --no-install-recommends gcc

WORKDIR /app

COPY Pipfile* .

RUN pipenv install --system --deploy

COPY . .
