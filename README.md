# Starnet - Where stars meet

## How to run?

> You need `docker` and `docker-compose` preinstalled on your machine.

```shell
docker-compose up
```

The server is listening at [localhost](http://localhost)
and here are some links:

- [Swagger UI](http://localhost/api/v1/swagger)
- [ReDoc](http://localhost/api/v1/redoc)
- [Admin Panel](http://localhost/admin)

## Quickly test service.

```shell
docker-compose up -d
docker-compose exec app bash
# now you are in the container's bash shell
python manage.py migrate
python manage.py loaddata users posts likes
```

Test users credentials (`username`:`password`):

- `admin1`:`adminpassword`
- `reviewer`:`thecodeisamazing`
- `simpleuser`:`qwertysad`
