startdb:
	docker run --rm --name postgres -e POSTGRES_PASSWORD=admin -d -p 5432:5432 postgres:14
stopdb:
	docker stop postgres
