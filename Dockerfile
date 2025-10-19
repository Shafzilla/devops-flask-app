FROM python:latest AS builder-image
COPY requirements.txt requirements.txt
COPY hello.py hello.py

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "hello.py"]