FROM python:3.7-alpine

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

RUN pwd

EXPOSE 80

CMD ["python", "manage.py", "runserver"]


