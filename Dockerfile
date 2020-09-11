FROM python:3.7-slim-buster

RUN mkdir /app

WORKDIR /app

ADD . /app

RUN apt-get update

RUN pip install -U pip && \
    pip install -r requirements.txt

# ENV FLASK_APP=app.py
# ENV FLASK_ENV=development

# CMD ["python", "test.py"]