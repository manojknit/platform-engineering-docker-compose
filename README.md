# Platform Engineering Interview

This Weather API has been built using python with a dependency management and packaging solution called poetry. Platform Engineering side added nginx as proxy.

## Pre-requisites
* Docker installed
* Python 3.10+ installed
* Run `docker compose up` and hit the backend to get status: "ok".


## API
This has been built using python with a dependency management and packaging solution called poetry. You can use poetry if you wish.

## How to run
- Open in VSCODE and run the following in the terminal
```
cd server
poetry install
cd ..
docker-compose down
docker-compose build
docker-compose up
docker-compose logs
```
