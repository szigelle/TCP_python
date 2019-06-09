FROM ubuntu
RUN apt-get update
RUN apt-get install python3

COPY client.py /
COPY entrypoint_client.sh /
ENTRYPOINT ["/entrypoint_client.sh"]
CMD ["300"]


