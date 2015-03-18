all: help

clean:
	@find . -name *.py? -delete
	@rm -rf build dist *.egg-info

help:
	@echo "Please use \`make <target>\` where target one of"
	@echo " clean		to cleanup the package directory"
	@echo " install	to install requirements into environment"
	@echo " serv		to run dev server"
	@echo " test 		to run the test suite"
	@echo " watch		to enable livereload on assets changes"

install:
	@pip install -r requirements/main.txt

serv:
	@python setup.py serve -d -r -p 5008

test:
	@python setup.py test -q

watch:
	@grunt watch

.PHONY: clean help install serv test watch
