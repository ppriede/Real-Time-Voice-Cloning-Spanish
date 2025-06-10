FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt ./
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY . .

CMD ["python", "demo_cli.py"]
