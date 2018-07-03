FROM python:3.6

RUN set -x && addgroup --system app && adduser --system --group app

RUN pip install --upgrade pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY . /app
RUN pip install -e /app

USER app
WORKDIR /app

EXPOSE 5000
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "gps_routes.api:app"]
