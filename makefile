# Пути
INSTALL_DIR = ./make/newm

# Основные команды
.PHONY: all make run clean

all: make

make:  ## Установить в локальную директорию
	pip install --target=$(INSTALL_DIR) . && rm -r ./make/bin && mv ./make/newm/bin ./make/ && cp -r ./bin/. ./make/bin/. && git submodule update --init --remote --recursive && cd ./subprojects/pywm/ && make && cp -r ./make/bin/. ../../make/bin/. && cp -r ./make/pywm/. ../../make/newm/.

run:  ## Запустить newm
	$(INSTALL_DIR)/bin/start-newm

clean:  ## Очистить установку
	rm -rf $(INSTALL_DIR)
