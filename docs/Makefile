SHELL := /bin/bash

HOST ?= 127.0.0.1
PORT ?= 8765

python = /usr/bin/env python $(1)

.DEFAULT_GOAL := help

.PHONY: help
help:
	@grep -E '^[\.a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: serve
serve: ## Serve the slides
	@echo "Serving slides at http://$(HOST):$(PORT)/"
	@echo "Quit the server with CONTROL-C."
	@$(call python,-m http.server --bind $(HOST) $(PORT))

.PHONY: pdf
pdf: ## Export slides as PDF
	docker-compose up decktape
	docker-compose down
