FROM python:3.10-alpine

WORKDIR /app
COPY app.py app.py
COPY requirements.txt requirements.txt
RUN pip3 install -v -r requirements.txt

CMD ["flask", "--app", "app", "--debug", "run", "--host=0.0.0.0"]