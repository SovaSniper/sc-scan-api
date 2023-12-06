# syntax=docker/dockerfile:1

# FROM python:3.11
FROM python:3.9-slim

WORKDIR /code

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY . .

EXPOSE 8080

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--reload", "--loop", "asyncio", "--port", "8080"]