FROM python:3.7-alpine

ENV BRANCH_NAME
ENV REPO

WORKDIR /home/jenkins/workspace/

ADD . .

RUN pip install -r requirements.txt

RUN pwd

EXPOSE 80

CMD ["python", "manage.py", "runserver"]


