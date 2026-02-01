# DocumentDB OSS – Local Setup

This folder contains a Docker Compose configuration to run DocumentDB OSS locally.

## Authentication Note

The DocumentDB OSS container image is hosted on GitHub Container Registry (ghcr.io) and requires authentication.

Before running Docker Compose, log in once:

```bash
docker login ghcr.io
```
You will need a GitHub personal access token with ```read:packages``` permission.

## Start DocumentDB OSS

```bash
docker compose up -d
docker ps
```

DocumentDB should be listening on:
mongodb://localhost:27017
