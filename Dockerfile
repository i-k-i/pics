FROM python:3.7.0-alpine

RUN apk update && apk add libpq
RUN apk update && apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev
RUN apk add zlib jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev
#gunicorn
RUN apk --no-cache add libc-dev

RUN mkdir -p /usr/src/pics
WORKDIR /usr/src/pics
COPY . .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

RUN apk del .build-deps

STOPSIGNAL SIGINT
CMD exec python manage.py runserver
