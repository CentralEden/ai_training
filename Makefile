# AI/DS研修プログラム開発用Makefile

.PHONY: help install install-dev clean test lint format check jupyter
.DEFAULT_GOAL := help

help: ## このヘルプメッセージを表示
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install: ## 基本依存関係をインストール
	poetry install

install-dev: ## 開発用依存関係も含めてインストール
	poetry install --with dev

install-gpu: ## GPU対応環境をインストール
	poetry install --with dev --with gpu

clean: ## キャッシュとビルドファイルを削除
	poetry cache clear --all .
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".coverage" -exec rm -rf {} +

test: ## テストを実行
	poetry run pytest

test-notebooks: ## Jupyter Notebookのテストを実行
	poetry run pytest --nbval-lax foundations/ specializations/ advanced/ || true

lint: ## コード品質チェック
	poetry run flake8 .
	poetry run mypy .
	poetry run nbqa flake8 . --extend-ignore=E203,W503 --max-line-length=88

format: ## コードフォーマット実行
	poetry run black .
	poetry run isort .
	poetry run nbqa black .
	poetry run nbqa isort .

check: ## フォーマットチェック（CI用）
	poetry run black --check --diff .
	poetry run isort --check --diff .
	poetry run nbqa black --check --diff .
	poetry run nbqa isort --check --diff .

jupyter: ## JupyterLabを起動
	poetry run jupyter lab --ip=0.0.0.0 --port=8888 --no-browser

jupyter-bg: ## JupyterLabをバックグラウンドで起動
	nohup poetry run jupyter lab --ip=0.0.0.0 --port=8888 --no-browser &

update: ## 依存関係を更新
	poetry update

lock: ## 依存関係をロック
	poetry lock

show: ## インストール済みパッケージを表示
	poetry show

shell: ## Poetry仮想環境をアクティベート
	poetry shell

env-info: ## 仮想環境情報を表示
	poetry env info

export-requirements: ## requirements.txtを生成（デプロイ用）
	poetry export -f requirements.txt --output requirements.txt --without-hashes

build-docs: ## ドキュメントをビルド
	poetry run mkdocs build

serve-docs: ## ドキュメントサーバーを起動
	poetry run mkdocs serve

new-specialization: ## 新しい専門分野テンプレートを作成
	@read -p "専門分野名を入力してください: " name; \
	mkdir -p specializations/$$name/{01_basics,02_intermediate,03_advanced,04_project}/{notebooks,exercises,data,materials}; \
	echo "# $$name 専門コース" > specializations/$$name/README.md; \
	echo "$$name専門コーステンプレートを作成しました"

validate-structure: ## プロジェクト構造を検証
	@echo "プロジェクト構造を検証中..."
	@test -f pyproject.toml || (echo "pyproject.tomlが見つかりません" && exit 1)
	@test -d foundations || (echo "foundationsディレクトリが見つかりません" && exit 1)
	@test -d specializations || (echo "specializationsディレクトリが見つかりません" && exit 1)
	@test -d advanced || (echo "advancedディレクトリが見つかりません" && exit 1)
	@echo "✅ プロジェクト構造は正常です"

setup-wsl: ## WSL環境初期セットアップ
	@echo "WSL環境をセットアップ中..."
	sudo apt update && sudo apt upgrade -y
	sudo apt install -y build-essential curl git vim htop tree wget zip unzip
	curl -sSL https://install.python-poetry.org | python3 -
	echo 'export PATH="$$HOME/.local/bin:$$PATH"' >> ~/.bashrc
	poetry config virtualenvs.in-project true
	poetry config virtualenvs.prefer-active-python true
	@echo "✅ WSL環境セットアップ完了"

# 開発ワークフロー用ショートカット
dev-setup: install-dev ## 開発環境の初期セットアップ
	@echo "🔧 開発環境セットアップ中..."
	$(MAKE) validate-structure
	$(MAKE) test
	@echo "✅ 開発環境セットアップ完了"

ci-check: ## CI環境でのチェック実行
	$(MAKE) check
	$(MAKE) lint
	$(MAKE) test-notebooks

deploy-check: ## デプロイ前チェック
	$(MAKE) ci-check
	$(MAKE) export-requirements
	@echo "✅ デプロイ準備完了" 