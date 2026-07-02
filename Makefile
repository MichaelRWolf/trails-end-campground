CLOUD_DIR := $(HOME)/Library/CloudStorage/GoogleDrive-michaelrwolfseattle@gmail.com/My Drive/trails-end-campground

.PHONY: install setup-hooks

install:
	cp source/Dawn_Testimonials_2025-10-09.txt "$(CLOUD_DIR)/Dawn_Testimonials_2025-10-09.txt"

setup-hooks:
	pre-commit install
