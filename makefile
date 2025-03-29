# Пути
INSTALL_DIR = ./make/newm

# Основные команды
.PHONY: all install run clean

all: install

install:  ## Установить в локальную директорию
	pip install --target=$(INSTALL_DIR) . && mv ./make/newm/bin ./make/

run:  ## Запустить newm
	$(INSTALL_DIR)/bin/start-newm

clean:  ## Очистить установку
	rm -rf $(INSTALL_DIR)
