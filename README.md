# GPS Routes

Install the API:

```bash
pip install --editable .[tests]
```

and run it:

```bash
gunicorn --bind 127.0.0.1:5000 gps_routes.api:app
```

## Test

```
py.test
```
