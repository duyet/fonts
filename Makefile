FONTS = $(shell ls sources)
BUILD_DIR = fonts

.PHONY: all build clean test widen $(FONTS)

all: build

build: $(FONTS)

$(FONTS):
	@echo "Building font: $@"
	mkdir -p $(BUILD_DIR)/$@/ttf
	mkdir -p $(BUILD_DIR)/$@/woff2
	for f in sources/$@/*.glyphs; do \
		uv run --with-requirements requirements.txt fontmake -g $$f -o ttf --output-dir $(BUILD_DIR)/$@/ttf; \
	done
	cp $(BUILD_DIR)/$@/ttf/*.ttf $(BUILD_DIR)/$@/woff2/
	for f in $(BUILD_DIR)/$@/woff2/*.ttf; do \
		uv run --with-requirements requirements.txt fonttools ttLib.woff2 compress $$f; \
		rm $$f; \
	done

test:
	@echo "Running Fontbakery checks..."
	for f in $(BUILD_DIR)/*/ttf/*.ttf; do \
		uv run --with-requirements requirements.txt fontbakery check-googlefonts $$f --loglevel WARN || true; \
	done

widen:
	uv run python3 widen_font.py

ulw:
	bash ulw_test.sh

clean:
	rm -rf $(BUILD_DIR) deploy master_ufo instance_ufo
