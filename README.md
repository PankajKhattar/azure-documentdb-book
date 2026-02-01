# Azure DocumentDB – Book Companion Repository

This repository contains runnable examples, scripts, and reference material for the book **"Azure DocumentDB"**.

Each folder maps directly to a chapter in the book and contains practical, hands-on examples that complement the concepts discussed.

## Repository Structure

- `docker/` – Local setup using DocumentDB OSS
- `chapter-02-document-model/` – Document model, BSON basics, schema flexibility
- Additional chapter folders will be added progressively

## Prerequisites

- Docker & Docker Compose
- Node.js 18+ or Python 3.9+
- Basic familiarity with MongoDB-style APIs

## Operating System Compatibility

This repository is **operating system–agnostic**.

All examples have been tested on:
- Linux
- macOS
- Windows (via Docker Desktop)

Because DocumentDB OSS is run using Docker, the underlying host OS does not affect the behavior of the examples.

## Getting Started

Start with Chapter 2 by setting up DocumentDB OSS locally:

```bash
cd docker/documentdb-oss
docker compose up -d
