.PHONY:
init: down volume up
down:
	docker-compose down
volume:
	docker volume prune -f
pull:
	docker-compose pull
build:
	docker-compose build
up: pull build
	docker-compose up -d
	make ps
ps:
	docker-compose ps
test:
	docker-compose run --rm starter pytest tests.py -s
prune:
	make down
	docker volume prune -f
	docker system prune -f
