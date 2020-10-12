FROM python:3.8

MAINTAINER swapna <swapnay@gmail.com>

RUN apt update && \
    apt install -y netcat-openbsd
WORKDIR /app
COPY requirements.txt .
COPY app/logging.conf .
COPY docker-entrypoint.sh .
RUN pip install -r requirements.txt
COPY /app/ /app/

RUN chmod +x docker-entrypoint.sh
#COPY /conf/docker-entrypoint-initdb.d/ /usr/local/bin/docker-entrypoint-initdb.d/
#RUN chmod -R +x /usr/local/bin/docker-entrypoint-initdb.d
COPY /conf/docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/
RUN chmod -R +x /docker-entrypoint-initdb.d

CMD ["/bin/bash", "docker-entrypoint.sh"]

