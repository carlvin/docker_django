# syntax=docker/dockerfile:1
# Fetch official latest base image for python 
FROM python:3.10.0-alpine
# Prevent python from writing pyc to docker container
ENV PYTHONDONTWRITEBYTECODE=1
# Flush out python buffer
ENV PYTHONUNBUFFERED=1

# Setting up the working directory
WORKDIR /app

ADD simple-crm-app/requirements.freeze /app/requirements.freeze

RUN set -ex \
    && apk add --no-cache --virtual .build-deps postgresql-dev gcc python3-dev musl-dev build-base \
    && python -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install --no-cache-dir -r /app/requirements.freeze \
    && runDeps="$(scanelf --needed --nobanner --recursive /venv \
        | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
        | sort -u \
        | xargs -r apk info --installed \
        | sort -u)" \
    && apk add --virtual rundeps $runDeps \
    && apk del .build-deps


# Set the virtual environment
ENV VIRTUAL_ENV=/venv
ENV PATH=$VIRTUAL_ENV/bin:$PATH

# copy entrypoint.sh
COPY ./entrypoint.sh /app
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Copy all the files to your app
COPY simple-crm-app /app

#EXPOSE 8000

ENTRYPOINT [ "/app/entrypoint.sh" ]

#CMD [ "gunicorn","--bind",":8000","--workers","3","config.wsgi:application" ]