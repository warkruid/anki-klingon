# Warning! This is a _VERY_ idiosyncratic Makefile. 
# It probably only works for me. YMMV!

clean:
	rm .*~
	rm *~

all: winactivate installreq
	python gendict.py -i klingon-english.csv
	python gendict.py -i english-klingon.csv

venv:
	python -m venv ./venv

winactivate: venv
	venv\Scripts\activate.bat

installreq: winactivate
	pip install -r requirements.txt

changelog:
	git log  --reverse 
