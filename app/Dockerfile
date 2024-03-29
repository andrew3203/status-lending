# pull official base image
FROM python:3.9


# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql gettext\
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && apk del build-deps

RUN apk add --no-cache libstdc++ && \
    apk add --no-cache g++ && \
    ln -s /usr/include/locale.h /usr/include/xlocale.h

RUN apk add --update nodejs npm \
    && rm -rf /var/cache/apk/*
RUN npm install -g nodemon


# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
# Добавьте зависимости для сборки Pillow
RUN apk add --no-cache jpeg-dev zlib-dev libjpeg

# Замените команду установки wheel на установку из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

RUN mkdir /usr/src/app/mediafiles

# copy project
COPY . .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
