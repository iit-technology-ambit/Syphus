FROM python:3.6
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev &&\
    python -m pip install --upgrade setuptools wheel

RUN pip install pipenv
RUN pipenv --python 3.6 && \
	pipenv install


ENTRYPOINT ["python"]
CMD ["pipenv","manage.py"]
