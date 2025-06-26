# WSL + Poetry を使ったAI/DS開発環境構築ガイド

## 概要
WSL2（Windows Subsystem for Linux）とPoetryを組み合わせた、AI/データサイエンス研修のための開発環境構築手順です。Windows上でLinux環境を活用し、効率的な開発環境を実現します。

## WSLのメリット
- **ネイティブLinux環境**: Ubuntu環境での開発
- **Windows統合**: WindowsとLinuxファイルシステムの相互アクセス
- **パフォーマンス**: 仮想化による性能向上
- **GPU活用**: CUDA対応（WSL2 + NVIDIA Docker）

## Poetryのメリット
- **依存関係管理**: lockファイルによる再現可能な環境
- **仮想環境自動管理**: プロジェクトごとの環境分離
- **パッケージ公開**: 社内パッケージの簡単公開
- **開発効率**: 依存関係の競合解決

---

## ステップ1: WSL2環境構築

### 1.1 WSL2有効化
```powershell
# PowerShell（管理者権限）で実行
# WSL機能の有効化
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# 仮想マシンプラットフォーム機能の有効化
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# 再起動後、WSL2をデフォルトに設定
wsl --set-default-version 2
```

### 1.2 Ubuntu 24.04 LTSインストール
```powershell
# Microsoft Storeから、または直接インストール
wsl --install -d Ubuntu-24.04

# インストール後の確認
wsl -l -v
```

### 1.3 Ubuntu初期設定
```bash
# Ubuntu起動後、ユーザー作成
# ユーザー名・パスワードを設定

# システム更新
sudo apt update && sudo apt upgrade -y

# 必要なパッケージインストール
sudo apt install -y \
    build-essential \
    curl \
    git \
    vim \
    htop \
    tree \
    wget \
    zip \
    unzip
```

## ステップ2: Python環境構築

### 2.1 Python 3.13インストール
```bash
# デフォルトのPython確認
python3 --version

# Ubuntu 24.04には最新のPythonが含まれていますが、
# 必要に応じて最新版をインストール
sudo apt install -y python3 python3-pip python3-venv python3-dev

# pipのアップグレード
python3 -m pip install --upgrade pip

# Python 3.13が利用可能でない場合は、deadsnakesリポジトリから
# sudo apt install software-properties-common
# sudo add-apt-repository ppa:deadsnakes/ppa
# sudo apt update
# sudo apt install python3.13 python3.13-venv python3.13-dev
```

### 2.2 Poetry インストール
```bash
# 公式インストーラーを使用
curl -sSL https://install.python-poetry.org | python3 -

# ~/.bashrcにPATH追加
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# インストール確認
poetry --version

# Poetry設定の最適化
poetry config virtualenvs.in-project true  # .venv フォルダをプロジェクト内に作成
poetry config virtualenvs.prefer-active-python true
```

## ステップ3: AI/DS研修環境構築

### 3.1 プロジェクトクローン・セットアップ
```bash
# プロジェクトディレクトリに移動
cd ~/projects  # または任意のディレクトリ

# リポジトリクローン
git clone <repository-url> ai-ds-training
cd ai-ds-training

# 依存関係インストール
poetry install

# 開発用ツールも含む
poetry install --with dev

# GPU環境の場合（CUDA対応GPU有り）
poetry install --with gpu
```

### 3.2 仮想環境の確認
```bash
# 仮想環境情報表示
poetry env info

# インストール済みパッケージ確認
poetry show

# 依存関係ツリー表示
poetry show --tree

# 仮想環境をアクティベート
poetry shell
```

### 3.3 Jupyter環境設定
```bash
# JupyterLab起動
poetry run jupyter lab --ip=0.0.0.0 --port=8888 --no-browser

# バックグラウンドで起動
nohup poetry run jupyter lab --ip=0.0.0.0 --port=8888 --no-browser &

# カスタム設定で起動
poetry run jupyter lab --config=config/jupyter_config.py
```

## ステップ4: GPU環境構築（オプション）

### 4.1 NVIDIA Docker + WSL2
```bash
# NVIDIA Container Toolkitインストール
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)
curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -
curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list

sudo apt-get update && sudo apt-get install -y nvidia-docker2

# Docker再起動
sudo systemctl restart docker
```

### 4.2 GPU対応確認
```bash
# 仮想環境内でGPU確認
poetry shell

# PyTorch GPU確認
python -c "import torch; print(torch.cuda.is_available())"

# TensorFlow GPU確認
python -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

## ステップ5: 開発ツール設定

### 5.1 VS Code + WSL拡張
```bash
# VS Code WSL拡張インストール
# VS Code内で Ctrl+Shift+P → "Remote-WSL: New Window"

# WSL内でプロジェクト開く
code .

# 推奨拡張機能
# - Python
# - Jupyter
# - GitLens
# - Black Formatter
# - isort
```

### 5.2 Git設定
```bash
# Git設定
git config --global user.name "Your Name"
git config --global user.email "your.email@company.com"

# SSH鍵生成（GitHub用）
ssh-keygen -t ed25519 -C "your.email@company.com"
```

### 5.3 品質管理ツール設定
```bash
# 仮想環境内で実行
poetry shell

# コードフォーマット
black .
isort .

# 静的解析
flake8 .
mypy .

# テスト実行
pytest
```

## ステップ6: トラブルシューティング

### 6.1 よくある問題と解決策

#### Poetry関連
```bash
# Poetry環境削除・再構築
poetry env remove python
poetry install

# キャッシュクリア
poetry cache clear --all .

# 仮想環境の場所確認
poetry env info --path
```

#### WSL関連
```bash
# WSL再起動
wsl --shutdown
wsl

# Ubuntu再インストール
wsl --unregister Ubuntu-22.04
wsl --install -d Ubuntu-22.04
```

#### GPU関連
```bash
# CUDA診断
nvidia-smi  # Windows側で実行
poetry run python -c "import torch; print(torch.version.cuda)"
```

### 6.2 パフォーマンス最適化

#### メモリ使用量制限
```bash
# ~/.wslconfigファイル作成（Windows側）
[wsl2]
memory=8GB  # WSL2のメモリ使用量制限
processors=4  # CPU使用コア数制限
```

#### ディスク容量管理
```bash
# 不要なパッケージキャッシュ削除
sudo apt autoremove
sudo apt autoclean

# Poetryキャッシュクリア
poetry cache clear --all .
```

## ステップ7: 社内環境統合

### 7.1 社内ネットワーク設定
```bash
# プロキシ設定（必要に応じて）
export HTTP_PROXY=http://proxy.company.com:8080
export HTTPS_PROXY=http://proxy.company.com:8080

# Poetry用プロキシ設定
poetry config http-basic.proxy user password
```

### 7.2 社内リポジトリ設定
```bash
# 社内PyPIリポジトリ設定
poetry config repositories.company-pypi https://pypi.company.com/simple/
poetry config http-basic.company-pypi username password
```

### 7.3 バックアップ・復元
```bash
# 仮想環境のエクスポート
poetry export -f requirements.txt --output requirements.txt

# プロジェクト設定のバックアップ
cp pyproject.toml pyproject.toml.backup
```

---

この環境構築により、Windows環境でありながらLinuxネイティブな開発体験を得られ、効率的なAI/データサイエンス学習が可能になります。 