FROM python:3.14-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    APP_HOME=/app

WORKDIR $APP_HOME

COPY pyproject.toml poetry.lock README.md LICENSE ./

RUN pip install --no-cache-dir poetry && \
    poetry install --only main --no-root --no-interaction

COPY . .

RUN chmod +x entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
