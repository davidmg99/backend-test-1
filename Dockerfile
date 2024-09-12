FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ /app/src

WORKDIR /app/src

EXPOSE 8002

CMD ["python", "app.py"]