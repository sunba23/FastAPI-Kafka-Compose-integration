# FastAPI + Faststream + Kafka + Docker Compose example

This repository contains a working example of integration of Kafka in KRaft mode, FastAPI and Faststream, all dockerized and coordinated with Docker Compose.

## Usage

After cloning the repo, do:

```bash
docker compose up
```

Then (after the producer is ready, which takes about 10 seconds because of the healthcheck) run:

```bash
curl -X POST "http://localhost:8000/produce" \
  -H "Content-Type: application/json" \
  -d '{
    "user_id": "12345",
    "event_type": "login",
    "percent": 90
}'
```

You can check that the message has been received by the consumer by running:

```bash
docker logs kafka-consumer
```

## References

A part of the code is taken from [here](https://github.com/katyagorshkova/kafka-kraft), but with some improvements to work out-of-the-box and also to provide a working example with additional consumer and in-API producer services.

## TODO

- In docker-compose.yml, healthcheck logic could be added to producer, since it starts at the same time as consumer and consumer tries to read a non-existent topic. However, the existing restart logic is sufficient.
