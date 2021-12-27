FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV PYTHONIOENCODING utf-8
ENV DJANGO_SETTINGS_MODULE showminder.settings

RUN adduser -D -u 1000 chris
WORKDIR /usr/src/app

ADD requirements*.txt /usr/src/app/
RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev linux-headers postgresql-dev \
  && pip install --no-cache-dir -r requirements.txt

ADD . /usr/src/app
RUN mkdir /tmp/staticfiles && /usr/src/app/showminder/manage.py collectstatic --noinput

EXPOSE 8000

USER chris

CMD ["honcho", "start"]
