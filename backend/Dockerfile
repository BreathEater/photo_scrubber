FROM python:3.11-slim

RUN apt-get update && apt-get install -y exiftool && rm -rf /var/lib/apt/lists/*

WORKDIR /app

#installing Python dependecies:
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Running the API server:
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
