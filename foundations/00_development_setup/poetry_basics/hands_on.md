# Poetry基礎 - ハンズオン実習

## 🎯 実習の目標
実際にコマンドを実行してPoetryの基本操作を体験し、データ分析プロジェクトの環境構築をマスターします。

## ⏱️ 所要時間: 1時間

---

## 事前準備

### 環境確認
```bash
# WSL2 Ubuntu 24.04環境で以下のコマンドを実行
poetry --version
python --version
pwd
```

### 作業ディレクトリの準備
```bash
# ホームディレクトリに移動
cd ~

# 実習用ディレクトリ作成
mkdir poetry-hands-on
cd poetry-hands-on
```

---

## 🚀 ハンズオン 1: 初めてのPoetryプロジェクト

### Step 1: 新しいプロジェクト作成
```bash
# 新しいプロジェクトを作成
poetry new data-analysis-demo
cd data-analysis-demo

# 作成された構造を確認
ls -la
tree  # treeコマンドがない場合は find . -type f を使用
```

**確認ポイント**:
- [ ] `pyproject.toml` ファイルが作成された
- [ ] `data_analysis_demo/` ディレクトリが作成された
- [ ] `tests/` ディレクトリが作成された

### Step 2: pyproject.tomlの内容確認
```bash
# pyproject.tomlの内容を表示
cat pyproject.toml
```

**理解すべき項目**:
- `[tool.poetry]` セクション: プロジェクト情報
- `[tool.poetry.dependencies]` セクション: 実際の依存関係
- `[tool.poetry.group.dev.dependencies]` セクション: 開発用依存関係

### Step 3: 依存関係のインストール
```bash
# 現在の依存関係をインストール
poetry install

# インストール結果を確認
poetry show
```

---

## 📦 ハンズオン 2: パッケージ管理の実践

### Step 1: データ分析用ライブラリの追加
```bash
# pandasを追加
poetry add pandas

# pyproject.tomlの変更を確認
cat pyproject.toml
```

**確認ポイント**:
- [ ] `[tool.poetry.dependencies]` にpandasが追加された
- [ ] `poetry.lock` ファイルが作成された

### Step 2: 複数パッケージの追加
```bash
# データ分析・可視化用パッケージを一括追加
poetry add numpy matplotlib seaborn

# インストール済みパッケージの確認
poetry show
```

### Step 3: 開発用パッケージの追加
```bash
# 開発・テスト用パッケージを追加
poetry add --group dev jupyter pytest black

# 開発用パッケージを含めた全体確認
poetry show --tree
```

### Step 4: 特定バージョンの指定
```bash
# 特定のバージョンを指定してインストール
poetry add scikit-learn==1.3.0

# バージョン範囲指定
poetry add requests^2.28.0

# インストール結果の確認
poetry show scikit-learn requests
```

---

## 🔧 ハンズオン 3: 仮想環境の操作

### Step 1: 仮想環境情報の確認
```bash
# 仮想環境の情報を表示
poetry env info

# 仮想環境のパスを確認
poetry env info --path
```

### Step 2: 仮想環境内でのコマンド実行
```bash
# 仮想環境内でPythonバージョン確認
poetry run python --version

# 仮想環境内でパッケージ確認
poetry run python -c "import pandas; print(pandas.__version__)"
```

### Step 3: 仮想環境シェルの起動
```bash
# 仮想環境シェルを起動
poetry shell

# シェル内でコマンド実行（仮想環境内）
python --version
python -c "import numpy; print('NumPy version:', numpy.__version__)"

# 仮想環境から抜ける
exit
```

---

## 📊 ハンズオン 4: 実際のデータ分析プロジェクト

### Step 1: サンプルスクリプトの作成
```bash
# メインのPythonファイルを作成
cat > data_analysis_demo/main.py << 'EOF'
"""
簡単なデータ分析のサンプル
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_sample_data():
    """サンプルデータの作成"""
    np.random.seed(42)
    data = {
        'month': ['1月', '2月', '3月', '4月', '5月', '6月'],
        'sales': np.random.randint(100, 1000, 6),
        'profit': np.random.randint(10, 100, 6)
    }
    return pd.DataFrame(data)

def analyze_data(df):
    """データの基本統計分析"""
    print("=== データの概要 ===")
    print(df.head())
    print("\n=== 基本統計量 ===")
    print(df.describe())
    return df

def visualize_data(df):
    """データの可視化"""
    plt.figure(figsize=(10, 6))
    
    # 売上のグラフ
    plt.subplot(1, 2, 1)
    plt.bar(df['month'], df['sales'])
    plt.title('月別売上')
    plt.xlabel('月')
    plt.ylabel('売上')
    
    # 利益のグラフ
    plt.subplot(1, 2, 2)
    plt.plot(df['month'], df['profit'], marker='o')
    plt.title('月別利益')
    plt.xlabel('月')
    plt.ylabel('利益')
    
    plt.tight_layout()
    plt.savefig('analysis_result.png')
    plt.show()

if __name__ == "__main__":
    # データ分析の実行
    df = create_sample_data()
    df = analyze_data(df)
    visualize_data(df)
    print("\n分析完了！グラフは analysis_result.png に保存されました。")
EOF
```

### Step 2: スクリプトの実行
```bash
# Poetry経由でスクリプト実行
poetry run python data_analysis_demo/main.py

# 結果ファイルの確認
ls -la *.png
```

### Step 3: Jupyter Labの起動
```bash
# Jupyter Labを起動
poetry run jupyter lab

# ブラウザが開かない場合は表示されたURLをコピーして手動でアクセス
# Ctrl+C で停止
```

---

## 🔄 ハンズオン 5: パッケージの更新と削除

### Step 1: パッケージの更新
```bash
# 更新可能なパッケージの確認
poetry show --outdated

# 特定のパッケージを更新
poetry update pandas

# 全パッケージの更新
poetry update
```

### Step 2: パッケージの削除
```bash
# 不要なパッケージを削除
poetry remove requests

# 削除結果の確認
poetry show | grep requests
```

### Step 3: 依存関係の整理
```bash
# 依存関係ツリーの確認
poetry show --tree

# 孤立した依存関係のチェック（手動確認）
poetry show
```

---

## 🧪 ハンズオン 6: 別環境での再現

### Step 1: プロジェクトの複製準備
```bash
# 現在のディレクトリから親ディレクトリに移動
cd ..

# プロジェクトをコピー（別環境をシミュレート）
cp -r data-analysis-demo data-analysis-demo-copy
cd data-analysis-demo-copy
```

### Step 2: 仮想環境の削除と再作成
```bash
# 既存の仮想環境を削除
poetry env remove python

# 依存関係の再インストール
poetry install

# 環境が正しく再現されたか確認
poetry run python data_analysis_demo/main.py
```

---

## 🔍 ハンズオン 7: トラブルシューティング

### Step 1: 意図的にエラーを発生させる
```bash
# 存在しないパッケージを追加してみる
poetry add non-existent-package-12345

# エラーメッセージを確認
```

### Step 2: キャッシュのクリア
```bash
# キャッシュの確認
poetry cache list

# キャッシュのクリア
poetry cache clear --all pypi
```

### Step 3: 環境のリセット
```bash
# 仮想環境の完全リセット
poetry env remove python
poetry install
poetry env info
```

---

## ✅ 実習チェックリスト

### 基本操作
- [ ] `poetry new` でプロジェクト作成
- [ ] `poetry add` でパッケージ追加
- [ ] `poetry remove` でパッケージ削除
- [ ] `poetry install` で依存関係インストール
- [ ] `poetry show` でパッケージ一覧確認

### 仮想環境操作
- [ ] `poetry run` でコマンド実行
- [ ] `poetry shell` で仮想環境起動
- [ ] `poetry env info` で環境情報確認

### ファイル理解
- [ ] `pyproject.toml` の内容理解
- [ ] `poetry.lock` の役割理解

### 実践的な使用
- [ ] データ分析ライブラリの管理
- [ ] Jupyter Lab での開発
- [ ] 環境の複製と再現

---

## 🎓 まとめと次のステップ

### 今日習得したスキル
1. **Poetryの基本概念**: プロジェクト管理、依存関係、仮想環境
2. **実用的なコマンド**: add, remove, install, show, run
3. **データ分析環境の構築**: pandas, numpy, matplotlib等の管理
4. **トラブルシューティング**: 問題発生時の対処法

### 実務での活用方法
```bash
# 新しいプロジェクト開始時の推奨フロー
poetry new my-new-project
cd my-new-project
poetry add pandas numpy matplotlib seaborn jupyter
poetry add --group dev pytest black
poetry run jupyter lab
```

### 次の実習課題
1. **個人プロジェクト**: 実際のデータを使った分析プロジェクト作成
2. **環境共有**: チームメンバーとの環境共有実践
3. **Git連携**: Poetryプロジェクトのバージョン管理

---

## 🔗 参考リンク
- [Poetry公式ドキュメント](https://python-poetry.org/docs/)
- [次の実習: Git基礎](../git_basics/hands_on.md)

お疲れさまでした！Poetryの基本操作をマスターできました。
続いて Git の実習に進みましょう！ 