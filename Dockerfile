FROM python:3.12.10-alpine3.21 as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

FROM python:3.12.10-alpine3.21
WORKDIR /app
COPY --from=builder /app .
CMD ["python", "gameday.py"]