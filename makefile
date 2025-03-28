# Пути
VENV_DIR = newm
INSTALL_DIR = ./make/newm

# Основные команды
.PHONY: all install venv run clean

all: install

install:  ## Установить в локальную директорию
	pip install --target=$(INSTALL_DIR) . && mv ./make/newm/bin ./make/

venv:  ## Создать виртуальное окружение и установить зависимости
	python -m venv $(VENV_DIR)
	$(VENV_DIR)/bin/pip install .

run:  ## Запустить newm
	$(INSTALL_DIR)/bin/start-newm

clean:  ## Очистить установку
	rm -rf $(INSTALL_DIR) $(VENV_DIR) *.egg-info build dist
