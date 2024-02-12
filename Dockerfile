# Dockerfile
FROM python:3.12

ENV PYTHONUNBUFFERED  1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
# Install PostgreSQL client utilities
RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/*
RUN pip install -r requirements.txt

COPY . /app/

EXPOSE  8000

CMD ["./entrypoint.sh"]