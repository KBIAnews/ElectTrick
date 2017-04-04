SHELL := /bin/bash

# ET_DB_USER ?= $(shell bash -c 'read -p "Database User: " pwd; echo $$pwd')
# ET_DB_PASS ?= $(shell bash -c 'read -p "Databse Password: " pwd; echo $$pwd')
# ET_S3_ACCESS_ID ?= $(shell bash -c 'read -p "AWS Key ID: " pwd; echo $$pwd')
# ET_S3_ACCESS_SECRET ?= $(shell bash -c 'read -p "AWS Key Secret: " pwd; echo $$pwd')
# echo "ET_DB_USER=$(ET_DB_USER)"

.PHONY: init
init:
	@echo "THIS IS THE INIT COMMAND - ONLY DO THIS ONCE - EDIT .BASHRC LATER"
	echo "# The following are environment variables used by the ElectTricks app.">>~/.bashrc
	@read -p "Enter DB User:" db_user; \
	echo "export ET_DB_USER=$$db_user">>~/.bashrc
	@read -p "Enter DB Password:" db_pass; \
	echo "export ET_DB_PASS=$$db_pass">>~/.bashrc
	@read -p "Enter AWS Key ID:" sthree_id; \
	echo "export ET_AWS_ID=$$sthree_id">>~/.bashrc
	@read -p "Enter AWS Key Secret:" sthree_secret; \
	echo "export ET_AWS_SECRET=$$sthree_secret">>~/.bashrc
	@echo "Done. Now source ~/.bashrc fresh before you do anything else."