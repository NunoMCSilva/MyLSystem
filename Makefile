per = pipenv run

test:
	$(per) pytest

flake:
	$(per) flake8
