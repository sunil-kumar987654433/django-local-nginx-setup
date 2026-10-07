FROM python:3.13.16-slim AS builder

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt /app/

RUN pip install --upgrade pip && \
    pip install \
        --prefix=/install \
        --no-cache-dir \
        -r requirements.txt


# =========================
# Final stage
# =========================
FROM python:3.13.16-slim

WORKDIR /app

COPY --from=builder /install /usr/local
COPY . .

RUN useradd --create-home --shell /bin/bash django_user && \
    mkdir -p /app/staticfiles && \
    chown -R django_user:django_user /app && \
    chmod +x /app/entrypoint.sh

USER django_user

CMD ["./entrypoint.sh"]