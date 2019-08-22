.PHONY: clean

clean:
	rm -rf *.pyc *.html __pycache__

fmt:
	black *.py

run:
	./py24.py
