BDIST = python3 setup.py bdist
BUILD = python3 setup.py build --force
CLEAN = /bin/rm -fr couchdb/__pycache__
INSTALL = python3 setup.py install --force --optimize 2
SDIST = python3 setup.py sdist
TEST = python3 tests.py

.DEFAULT_GOAL := sdist
.PHONY: all

all: bdist build clean i install reinstall sdist test

bdist:
	$(BDIST)

build:
	$(BUILD)

clean:
	$(CLEAN)

i:
	$(INSTALL) && $(CLEAN)

install:
	$(INSTALL)

reinstall:
	$(INSTALL)

sdist:
	$(SDIST)

test:
	$(TEST)
