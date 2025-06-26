# Poetry基礎ガイド

## 学習目標
- Poetryの役割と重要性を理解する
- Poetryを使ったプロジェクト作成・管理ができる
- パッケージの追加・削除・更新操作をマスターする
- 仮想環境とpyproject.tomlの概念を理解する

## 所要時間: 2時間

---

## 1. Poetryとは何か？

### 🎯 一言で言うと
**Poetry**は、Pythonプロジェクトの依存関係管理と環境構築を自動化するツールです。

### 🚫 従来の問題
```bash
# pip + requirements.txtの問題
pip install pandas==1.5.0
pip install numpy
# → numpyのバージョンが不明確
# → 他の人の環境で動かない可能性
# → 依存関係の競合が発生しやすい
```

### ✅ Poetryの解決策
```bash
# Poetryの場合
poetry add pandas==1.5.0
# → 自動でnumpyの適切なバージョンも解決
# → poetry.lockファイルで確実な再現性
# → 依存関係の競合を事前に検出
```

## 2. Poetryの主な機能

### 📦 パッケージ管理
- 依存関係の自動解決
- セマンティックバージョニング対応
- 開発用と本番用の依存関係分離

### 🔧 仮想環境管理
- プロジェクトごとの独立した環境
- Python環境の自動切り替え
- 環境の確実な再現

### 🛠️ プロジェクト管理
- プロジェクトの標準化
- ビルド・公開の自動化
- 設定ファイルの一元管理

## 3. Poetryのインストール（確認）

### WSL2 Ubuntu 24.04環境での確認
```bash
# インストール確認
poetry --version
# 例: Poetry version 1.6.1

# 設定確認
poetry config --list
```

### 基本設定
```bash
# 仮想環境をプロジェクト内に作成（推奨）
poetry config virtualenvs.in-project true

# 確認
poetry config virtualenvs.in-project
# 出力: true
```

## 4. 基本的な使い方

### 📁 新しいプロジェクト作成
```bash
# 新しいプロジェクト作成
poetry new my-data-project
cd my-data-project

# 作成されるディレクトリ構造
my-data-project/
├── pyproject.toml      # プロジェクト設定
├── README.md           # プロジェクト説明
├── my_data_project/    # メインパッケージ
│   └── __init__.py
└── tests/              # テストファイル
    └── __init__.py
```

### 📄 既存プロジェクトでの初期化
```bash
# 既存のディレクトリでPoetryプロジェクト化
cd existing-project
poetry init

# 対話式でpyproject.tomlを作成
# プロジェクト名、バージョン、依存関係などを入力
```

### 🔍 pyproject.tomlの理解
```toml
[tool.poetry]
name = "my-data-project"
version = "0.1.0"
description = "データ分析プロジェクト"
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.13"
pandas = "^2.2.0"
numpy = "^1.26.0"

[tool.poetry.group.dev.dependencies]
pytest = "^7.0.0"
jupyter = "^1.0.0"
```

## 5. パッケージ管理の実践

### ➕ パッケージの追加

#### 基本的な追加
```bash
# 最新版を追加
poetry add pandas

# 特定のバージョンを追加
poetry add numpy==1.21.0

# バージョン範囲指定
poetry add matplotlib>=3.5.0,<4.0.0
poetry add seaborn^0.11.0  # 0.11.0以上、0.12.0未満
```

#### 開発用パッケージの追加
```bash
# 開発用（テスト、デバッグ用）
poetry add --group dev pytest jupyter black

# 省略形
poetry add -D pytest jupyter black
```

#### 複数パッケージの一括追加
```bash
# データサイエンス基本セット
poetry add pandas numpy matplotlib seaborn scikit-learn

# 開発用ツール
poetry add --group dev pytest black flake8 mypy jupyter
```

### ➖ パッケージの削除
```bash
# パッケージ削除
poetry remove pandas

# 開発用パッケージの削除
poetry remove --group dev pytest

# 複数パッケージの削除
poetry remove numpy matplotlib seaborn
```

### 🔄 パッケージの更新

#### 特定パッケージの更新
```bash
# 特定パッケージを最新に更新
poetry update pandas

# 複数パッケージの更新
poetry update pandas numpy matplotlib
```

#### 全パッケージの更新
```bash
# 全パッケージの更新
poetry update

# 更新可能なパッケージの確認（更新せずに確認のみ）
poetry show --outdated
```

## 6. 仮想環境の管理

### 🌟 仮想環境の操作
```bash
# 仮想環境のインストール・有効化
poetry install

# 仮想環境内でコマンド実行
poetry run python my_script.py
poetry run jupyter lab
poetry run pytest

# 仮想環境シェルの起動
poetry shell
# この状態で通常のpythonコマンドが使える
python my_script.py
exit  # 仮想環境から抜ける
```

### 📊 環境情報の確認
```bash
# インストール済みパッケージの一覧
poetry show

# 特定パッケージの詳細
poetry show pandas

# 依存関係ツリーの表示
poetry show --tree

# 仮想環境のパス確認
poetry env info --path
```

## 7. 実践例: データ分析プロジェクト

### 🎪 シナリオ
売上データの分析プロジェクトをセットアップしてみましょう。

```bash
# 1. プロジェクト作成
poetry new sales-analysis
cd sales-analysis

# 2. データ分析用ライブラリ追加
poetry add pandas numpy matplotlib seaborn

# 3. 開発用ツール追加
poetry add --group dev jupyter pytest black

# 4. 仮想環境の確認
poetry install
poetry show

# 5. Jupyter Labの起動
poetry run jupyter lab
```

### 📝 作成されるpyproject.toml
```toml
[tool.poetry]
name = "sales-analysis"
version = "0.1.0"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = "^3.8"
pandas = "^1.5.3"
numpy = "^1.24.3"
matplotlib = "^3.7.1"
seaborn = "^0.12.2"

[tool.poetry.group.dev.dependencies]
jupyter = "^1.0.0"
pytest = "^7.4.0"
black = "^23.7.0"
```

## 8. よくあるコマンド集

### 🔧 日常的に使うコマンド
```bash
# プロジェクト作成
poetry new <project-name>

# 依存関係インストール
poetry install

# パッケージ追加
poetry add <package-name>

# 開発用パッケージ追加
poetry add --group dev <package-name>

# 仮想環境でコマンド実行
poetry run <command>

# 仮想環境シェル起動
poetry shell

# パッケージ一覧表示
poetry show

# 依存関係更新
poetry update
```

### 🔍 確認・診断系コマンド
```bash
# 設定確認
poetry config --list

# 環境情報確認
poetry env info

# パッケージ詳細確認
poetry show <package-name>

# 依存関係ツリー表示
poetry show --tree

# 更新可能パッケージ確認
poetry show --outdated
```

## 9. トラブルシューティング

### ❌ よくあるエラーと解決法

#### "poetry command not found"
```bash
# 解決方法1: PATHの確認
echo $PATH | grep -o '[^:]*poetry[^:]*'

# 解決方法2: 再インストール
curl -sSL https://install.python-poetry.org | python3 -
```

#### "No module named 'poetry'"
```bash
# システムのPythonとPoetryの競合
# 仮想環境内で以下を実行
poetry env use python3.13
poetry install
```

#### "SolverProblemError"（依存関係の競合）
```bash
# 依存関係の明示的な指定
poetry add "package-a>=1.0.0" "package-b<2.0.0"

# キャッシュクリア
poetry cache clear --all .
```

### 🔧 環境リセット
```bash
# 仮想環境の削除・再作成
poetry env remove python
poetry install
```

## 10. まとめ

### ✅ できるようになったこと
- [ ] Poetryの基本概念の理解
- [ ] 新しいプロジェクトの作成
- [ ] パッケージの追加・削除・更新
- [ ] 仮想環境の管理
- [ ] pyproject.tomlの読み方

### 🚀 次のステップ
1. **実際のプロジェクトで練習**: 小さなデータ分析プロジェクトを作成
2. **Git連携**: バージョン管理との組み合わせ
3. **チーム開発**: 他の人とのプロジェクト共有

### 💡 実務での活用ポイント
- **常にPoetryを使う**: 新しいプロジェクトは必ずPoetryで開始
- **依存関係は明示的に**: バージョンを意識してパッケージ追加
- **定期的な更新**: セキュリティアップデートを忘れずに
- **pyproject.tomlの管理**: 設定ファイルもバージョン管理に含める

---

📚 **参考資料**:
- [Poetry公式ドキュメント](https://python-poetry.org/docs/)
- [Python依存関係管理ベストプラクティス](https://python-poetry.org/docs/basic-usage/)

次は [hands_on.md](./hands_on.md) で実際に手を動かして練習しましょう！ 