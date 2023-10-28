FROM python:3.10.13-slim-bullseye

WORKDIR /app

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

RUN apt-get update --fix-missing && \
    apt-get install -y \
      musl-dev \
      libpq-dev \
      gcc  \
      figlet \
      libffi-dev

# Install pipenv and compilation dependencies
RUN pip install pipenv

# Install project requarements
COPY Pipfile .
COPY Pipfile.lock .

ENV PIPENV_VENV_IN_PROJECT=1
RUN pipenv uninstall --all
RUN pipenv --clear
RUN pipenv install --dev

# Copy source code
COPY . .

EXPOSE ${SERVER__PORT}

RUN chmod a+x /app/deployment/entrypoint.sh
ENTRYPOINT ["/app/deployment/entrypoint.sh"]
