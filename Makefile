
SCARR_SCRIPT = benchmark_scarr.py
SCARR_REQ = scarr_benchmarks/req_scarr.txt
SCARED_SCRIPT = benchmark_scared.py
SCARED_REQ = scared_benchmarks/req_scared.txt
LASCAR_SCRIPT = benchmark_lascar.py
LASCAR_REQ = lascar_benchmarks/req_lascar.txt

VENV_DIR = ve

PYTHON = $(VENV_DIR)/bin/python3

all: compile_scarr compile_scared compile_lascar

scarr: compile_scarr

scared: compile_scared

lascar: compile_lascar

venv:
	python3.10 -m venv $(VENV_DIR)

install_scarr: venv
	$(PYTHON) -m pip install -r $(SCARR_REQ)

compile_scarr: install_scarr
	$(PYTHON) $(SCARR_SCRIPT)

install_scared: venv
	$(PYTHON) -m pip install -r $(SCARED_REQ)

compile_scared: install_scared
	$(PYTHON) $(SCARED_SCRIPT)

install_lascar: venv
	$(PYTHON) -m pip install -r $(LASCAR_REQ)

compile_lascar: install_lascar
	$(PYTHON) $(LASCAR_SCRIPT)

clean:
	rm -rf $(VENV_DIR)
