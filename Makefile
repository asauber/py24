.PHONY: clean

clean:
	rm -rf *.pyc *.html __pycache__

fmt:
	black *.py

