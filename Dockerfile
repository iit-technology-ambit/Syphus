FROM python:3.6
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev &&\
    python -m pip install --upgrade setuptools wheel

WORKDIR /app
COPY requirements.txt requirements.txt
COPY app app
COPY manage.py manage.py
RUN pip install -r requirements.txt


ENTRYPOINT ["python", "manage.py"]
