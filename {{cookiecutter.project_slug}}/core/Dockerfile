FROM python:3.9 as base

ARG NAME
ENV NAME=$NAME
ENV FLASK_APP=/core/app.py
ENV FLASK_ENV=development

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base AS python-deps

RUN pip install pipenv==2022.3.28
RUN apt-get update && apt-get install -y --no-install-recommends gcc

# Install python dependencies in /.venv
COPY Pipfile* ./
RUN pipenv lock
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base AS development

# Copy virtual env from python-deps stage
COPY --from=python-deps /usr/local /usr/local
COPY --from=python-deps /Pipfile* /
COPY --from=python-deps /.venv /.venv

ENV PATH="/.venv/bin:$PATH"

RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --dev

# Create and switch to a new user
RUN useradd --create-home appuser
WORKDIR /core
USER appuser

# Install application into container
COPY . ./

ENTRYPOINT ["sh","./entrypoint.sh" ]

CMD [ "flask run --host 0.0.0.0" ]
