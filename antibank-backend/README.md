# ANTIBANK Backend

FastAPI backend for ANTIBANK financial simulation.

## Run locally

uvicorn main:app --reload

## Docker

docker build -t antibank-backend .
docker run -p 8000:8000 antibank-backend
