.PHONY: clean data help
.DEFAULT_GOAL := help

data: ## Download raw data.
	python src/data/get_data.py --dataset=all

docker-build: ## Build a docker image with all of the required software.
	docker build -t afq-insight-paper .

docker-lab: ## Run JupyterLab from the afq-insight-paper docker image. Follow the instructions in the standard output to access the JupyterLab URL.
	docker run -it -p 8899:8899 afq-insight-paper

docker-shell: ## Obtain an interactive shell in the afq-insight-paper docker image.
	docker run -it afq-insight-paper /bin/bash

clean: ## Delete output files
	cd src && make clean
	cd reports && make clean

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
