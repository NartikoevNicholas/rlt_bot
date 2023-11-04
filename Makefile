docker_run:
	docker-compose -f docker-compose.yml up -d --remove-orphans

open_mongodb:
	docker-compose exec -it mongodb bash

import_mongodb:
	docker exec -i mongodb /usr/bin/mongorestore --uri "mongodb://test:test@mongodb:27017/test" --drop /var/backups/sampleDB

docker_clear:
	docker rm -f `docker ps -qa`
	docker rmi -f `docker images -qa`
	docker volume prune -a
	docker network prune
	docker system prune --volumes
