FROM python:3.10-alpine

WORKDIR /app
COPY app_flask.py app_flask.py
COPY requirements.txt requirements.txt
RUN pip3 install -v -r requirements.txt

CMD ["flask", "--app", "app_flask", "--debug", "run", "--host=0.0.0.0"]