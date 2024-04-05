FROM python:3-alpine

RUN apk add --no-cache postgresql-client

RUN adduser -D dvf

USER dvf

WORKDIR /home/dvf

ENV PATH="/home/dvf/.local/bin:$PATH"

COPY ./dvf .
RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
