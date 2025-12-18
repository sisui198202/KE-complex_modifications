SHELL := /bin/sh

.PHONY: all rebuild update-dist preview-server update-json index

# 生成物
DOCS_JSON := $(wildcard docs/json/*.json)
EXTRA_HTML := $(wildcard src/extra_descriptions/*.html)

# デフォルトターゲット: JSON と index.html を更新
all: update-json index

# JSON を生成 (src/json/*.erb -> docs/json/*.json)
update-json:
	@./scripts/update-json.sh

# docs/index.html を生成
# docs/json/*.json または src/index.html.erb, extra_descriptions に依存
index: docs/index.html

docs/index.html: src/index.html.erb $(DOCS_JSON) $(EXTRA_HTML) scripts/erb2html.rb scripts/json2exhtml.rb
	@mkdir -p docs
	@ruby scripts/erb2html.rb < src/index.html.erb > docs/index.html
	@echo "updated: $@"

# 強制再生成: 生成物を消して作り直し
rebuild:
	@rm -f docs/index.html docs/json/*.json src/extra_descriptions/*.html 2>/dev/null || true
	@$(MAKE) all

# 互換ターゲット（all と同義）
update-dist: all

# ローカルプレビュー（docs をルートに 8000 番で起動）
preview-server:
	@cd docs && python3 -m http.server 8000 || ruby -run -e httpd . -p 8000
	@echo "open http://localhost:8000"
