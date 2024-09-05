include .env

db-up:
	docker compose up -d

db-stop:
	docker compose stop

db-reset:
	docker compose down -v