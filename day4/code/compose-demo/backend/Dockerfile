FROM python:alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN adduser -S -H app
USER app
EXPOSE 8000
CMD uvicorn main:app --port 8000 --host 0.0.0.0
