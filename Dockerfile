FROM python:latest
COPY requirements.txt requirements.txt
COPY hello.py hello.py

RUN pip install -r requirements.txt

RUN pip install redis

EXPOSE 5000

CMD ["python", "hello.py"]