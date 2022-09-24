FROM python:3.9-slim-buster

WORKDIR /api

COPY requirements.txt .

RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY app.py .

EXPOSE 5000

ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]