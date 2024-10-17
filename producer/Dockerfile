FROM python:3.9-slim

WORKDIR /app

# Install FastAPI, Uvicorn, and FastStream
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application code
COPY . .

# Run FastAPI
CMD ["uvicorn", "producer:app", "--host", "0.0.0.0", "--port", "8000"]

