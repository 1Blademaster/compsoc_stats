FROM python:3.9-slim-buster

WORKDIR /api

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "get_members.py"]