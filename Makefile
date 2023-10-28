#!make
include .env

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))

IMAGE_NAME ?= ${DOCKER__USERNAME}/${PROJECT__NAME}:${PROJECT__VERSION}
CONTAINER_NAME ?= ${DOCKER__USERNAME}-${PROJECT__NAME}-${PROJECT__VERSION}

build:
	docker build -t ${IMAGE_NAME} --rm -f ./deployment/Dockerfile .

run-container:
	docker run -d --rm --name ${CONTAINER_NAME}-container -p 3000:3000 ${IMAGE_NAME}

compose-dev:
	docker-compose --env-file .env -f deployment/docker-compose.yml -p ${CONTAINER_NAME} --profile ${DOCKER__USERNAME}  up -d --remove-orphans

compose-prod:
	docker-compose --env-file .env.prod -f deployment/docker-compose.yml -f deployment/docker-compose.prod.yml -p ${CONTAINER_NAME} --profile ${DOCKER__USERNAME}  up -d --remove-orphans

compose-rebuild-dev:
	docker-compose --env-file .env -p ${CONTAINER_NAME} --profile ${DOCKER__USERNAME} up -d --build --remove-orphans -f ./deployment/docker-compose.yml

compose-rebuild-prod:
	docker-compose --env-file .env.prod -p ${CONTAINER_NAME} --profile ${DOCKER__USERNAME} up -d --build --remove-orphans -f ./deployment/docker-compose.yml -f deployment/docker-compose.prod.yml

alembic-init:
	alembic init ./db/migrations

migrate:
	pipenv run auto_migration
	pipenv run migrate

test:
	pipenv run test



