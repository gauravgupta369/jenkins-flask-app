FROM python:3.7-alpine

RUN mkdir /app

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

# ENV FLASK_APP=app.py
# ENV FLASK_ENV=development


# CMD ["python", "test.py"]