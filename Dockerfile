FROM python:3.8.2-slim
WORKDIR /app
RUN apt-get update && apt-get install -y gcc
COPY requirements.txt .
RUN pip install --upgrade pip && \
		pip install -r requirements.txt
COPY . .
CMD ["python", "-u", "main.py"]