# Пути
INSTALL_DIR = ./make/newm

# Основные команды
.PHONY: all make run clean

all: make

make:  ## Установить в локальную директорию
	pip make --target=$(INSTALL_DIR) . && mv ./make/newm/bin ./make/

run:  ## Запустить newm
	$(INSTALL_DIR)/bin/start-newm

clean:  ## Очистить установку
	rm -rf $(INSTALL_DIR)
