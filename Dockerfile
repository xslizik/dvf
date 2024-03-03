FROM alpine:3.19 as builder

RUN apk add --no-cache python3 py3-pip libpq postgresql-client curl
RUN adduser -D dvf

USER dvf

WORKDIR /home/dvf

COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 8000

CMD python3 dvf.py