FROM python:3.10.6-alpine3.16
LABEL org.opencontainers.image.authors="Balint Szigeti"
COPY main.py requirements.txt /
# https://stackoverflow.com/a/59812588
ENV PYTHONUNBUFFERED 1
RUN python -m pip install -r /requirements.txt
EXPOSE 8080

ENTRYPOINT [ "waitress-serve", "--host", "0.0.0.0", "main:app" ]
