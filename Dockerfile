FROM python:3.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING utf-8
ENV DJANGO_SETTINGS_MODULE showminder.settings

RUN adduser --shell /bin/sh --disabled-password chris
WORKDIR /usr/src/app

ADD requirements*.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

ADD . /usr/src/app
RUN mkdir /tmp/staticfiles && /usr/src/app/showminder/manage.py collectstatic --noinput

EXPOSE 8000

USER chris

CMD ["honcho", "start"]
