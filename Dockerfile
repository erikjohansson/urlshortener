FROM python:3.11-slim-buster

# cleaning up unused files
RUN apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
    && rm -rf /requirements.txt

COPY . /usr/src/app

EXPOSE 80

CMD ["sh", "./runserver.sh"]
