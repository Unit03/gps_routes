# GPS Routes

First, run a PostGIS server with a `gps_routes` database, `postgis` extension
enabled and 5432 port published:

```bash
docker run --detach --publish 5432 mdillon/postgis
psql -h 172.17.0.3 -U postgres  # The IP may be different for you.
```

```sql
CREATE DATABASE gps_routes;
CREATE EXTENSION postgis;
```

Point `SQL_DSN` environment variable at the server

```
export SQL_DSN=postgresql+psycopg2://postgres@172.17.0.3/gps_routes
```

Install the API:

```bash
pip install --editable .[tests]
```

Run database migrations:

```bash
alembic upgrade head
```

and run the API:

```bash
gunicorn --bind 127.0.0.1:5000 gps_routes.api:app
```

## Test

```
py.test
```
