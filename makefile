# Пути
INSTALL_DIR := ./make/usr/lib/sqwm
BIN_DIR := ./make/usr/bin
WAYLAND_SESSION_DIR := ./make/usr/share/wayland-sessions
PYWM_DIR := ./pywm
NEWM_DIR := ./newm

# Основные команды
.PHONY: all install run clean prepare-dirs

all: install

prepare-dirs: $(INSTALL_DIR) $(BIN_DIR) $(WAYLAND_SESSION_DIR)

install: prepare-dirs
	@echo "Installing newm..."
	cd $(NEWM_DIR) && \
	pip install --target=../$(INSTALL_DIR) . && \
	cd ../ && \
	cp -r $(NEWM_DIR)/bin/. $(BIN_DIR)/ && \
	cp -r $(INSTALL_DIR)/newm/resources/newm.desktop $(WAYLAND_SESSION_DIR)/ && \
	cd $(PYWM_DIR) && \
	pip install --target=../$(INSTALL_DIR) . --upgrade && \
	cd ../ && \
	cp -r $(INSTALL_DIR)/bin/. $(BIN_DIR)/ && \
	rm -r $(INSTALL_DIR)/bin/
	@echo "Installation complete. Run 'make run' to start newm."

run: $(BIN_DIR)/start-newm
	$(BIN_DIR)/start-newm

clean:
	@echo "Cleaning up..."
	rm -rf ./make

# Правила для создания директорий
$(INSTALL_DIR) $(BIN_DIR) $(WAYLAND_SESSION_DIR):
	mkdir -p $@

$(BIN_DIR)/start-newm:
	@test -f $@ || (echo "Error: start-newm not found! Run 'make install' first." && exit 1)
