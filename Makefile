.EXPORT_ALL_VARIABLES:

##################
# Install commands
##################
install: ## Create a poetry env and install dev and production requirements
	poetry shell
	poetry install

init:
	@poetry run python utils/gen_data.py

##################
# Run flask apps
##################
server:
	@poetry run python main.py
