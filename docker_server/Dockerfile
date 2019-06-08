FROM ubuntu
RUN apt-get update
RUN apt-get install python3

COPY server.py /
COPY runserver.sh /
ENTRYPOINT ["/runserver.sh"]

