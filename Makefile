CURRENT = $(shell git rev-parse --short HEAD)

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
	@echo " freeze		to freeze applicaion"
	@echo " gh-pages	to update gh-pages"

install:
	@pip install -r requirements/main.txt

serv:
	@python setup.py serve -d -r -p 5008

freeze:
	@python setup.py freeze

test:
	@python setup.py test -q

watch:
	@grunt watch

gh-pages:
	git checkout -b gh-pages-$(CURRENT)
	FREEZER_BASE_URL='/flaskapp' python setup.py freeze
	git add -f gh-pages
	git commit --allow-empty -m "Update gh-pages at $(CURRENT)"
	git push origin `git subtree split --prefix gh-pages`:gh-pages --force
	git checkout -
	git branch -D gh-pages-$(CURRENT)

.PHONY: clean help install serv test watch freeze gh-pages
