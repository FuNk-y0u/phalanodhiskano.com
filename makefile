# =====PROJECT VARIABLE========
LANG = python
FILE = manage.py
PROJECT_NAME = phalanodhiskano
APP = main

# used to run the server
all:
	@echo --=== STARTING $(PROJECT_NAME) SERVER ===---
	@$(LANG) $(FILE) runserver

# used to run the shell
shell:
	@echo --=== $(PROJECT_NAME) shell ===--
	@ $(LANG) $(FILE) shell 

# used to make migrations
mmig:
	@echo --=== MAKING MIGRATION ON $(APP) ===--
	@ $(LANG) $(FILE) makemigrations $(APP)

# used to apply migrations made in mmig
apply:
	@echo --=== APPLYING MIGRATION ON $(APP) ===--
	@ $(LANG) $(FILE) migrate

# used to create admin account
create-admin:
	@ $(LANG) $(FILE) createsuperuser



