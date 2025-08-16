FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --default-timeout=200 --retries=10 -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

