.PHONY: clean system-packages python-packages install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages: 
	sudo apt install python3-pip -y
	pip3 install pipenv

python-packages:
	pipenv install --dev

tests:
	python3 manage.py test

run:
	python3 manage.py run

install: system-packages python-packages

all: clean install tests run