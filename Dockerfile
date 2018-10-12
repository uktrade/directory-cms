FROM python:3.6

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
# Different src directory for pip to prevent 'pip install -e' packages to be installed in /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt --src /usr/local/src

# Required to compile translations
RUN apt-get update && apt-get install -y gettext && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . /usr/src/app

# Install dockerize https://github.com/jwilder/dockerize
ENV DOCKERIZE_VERSION v0.5.0
RUN wget -q https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

CMD ["/usr/src/app/docker/cmd-webserver.sh"]

EXPOSE 8000
