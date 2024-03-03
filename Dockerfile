FROM alpine:3.19 as builder

RUN apk add --no-cache python3 py3-pip libpq postgresql-client curl
RUN adduser -D dvf

USER dvf

WORKDIR /home/dvf

# Create a virtual environment and activate it
RUN python3 -m venv venv
ENV PATH="/home/dvf/venv/bin:$PATH"

COPY . .
RUN pip3 install -r requirements.txt --no-cache-dir

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "myapp:app"]