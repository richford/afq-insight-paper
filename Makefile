.PHONY: clean data help
.DEFAULT_GOAL := help

current_dir = $(shell pwd)

data: ## Download raw data.
	python src/data/get_data.py --dataset=all

docker-build: ## Build a docker image with all of the required software.
	docker build -t afq-insight-paper ./docker

docker-lab: ## Run JupyterLab from the docker image. Follow instructions in stdout to access the JupyterLab URL.
	docker run -it --rm -p 8899:8899 -v $(current_dir):/afq-insight-paper afq-insight-paper

docker-shell: ## Obtain an interactive shell in the afq-insight-paper docker image.
	docker run -it --rm -v $(current_dir):/afq-insight-paper afq-insight-paper /bin/bash -c "conda activate afq-insight-paper;"

clean: ## Delete output files
	cd src && make clean
	cd reports && make clean

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
