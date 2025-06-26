# Git基礎 - ハンズオン実習

## 🎯 実習の目標
実際にコマンドを実行してGitの基本操作を体験し、バージョン管理の仕組みを理解します。

## ⏱️ 所要時間: 1.5時間

---

## 事前準備

### 環境確認
```bash
# WSL2 Ubuntu 24.04環境で以下のコマンドを実行
git --version
pwd
whoami
```

### 作業ディレクトリの準備
```bash
# ホームディレクトリに移動
cd ~

# 実習用ディレクトリ作成
mkdir git-hands-on
cd git-hands-on
```

---

## 🔧 ハンズオン 1: Git初期設定

### Step 1: ユーザー情報の設定
```bash
# ユーザー名の設定（実際の名前に変更してください）
git config --global user.name "山田太郎"

# メールアドレスの設定（実際のメールアドレスに変更してください）
git config --global user.email "yamada@example.com"

# 設定の確認
git config --global user.name
git config --global user.email
```

### Step 2: エディタとその他の設定
```bash
# デフォルトエディタの設定
git config --global core.editor "nano"

# カラー出力の有効化
git config --global color.ui auto

# 改行コードの設定（Windows/Linuxの互換性のため）
git config --global core.autocrlf input

# 設定の全体確認
git config --list | grep user
```

---

## 🚀 ハンズオン 2: 初めてのGitリポジトリ

### Step 1: 新しいプロジェクトの初期化
```bash
# プロジェクトディレクトリ作成
mkdir my-first-repo
cd my-first-repo

# Gitリポジトリの初期化
git init

# 隠しファイルを含めてディレクトリ内容確認
ls -la
```

**確認ポイント**:
- [ ] `.git` ディレクトリが作成された

### Step 2: 初期ファイルの作成
```bash
# READMEファイル作成
echo "# 私の最初のGitプロジェクト" > README.md

# Pythonスクリプトファイル作成
cat > hello.py << 'EOF'
def greet(name):
    """挨拶する関数"""
    return f"こんにちは、{name}さん！"

if __name__ == "__main__":
    print(greet("世界"))
EOF

# ファイル作成確認
ls -la
```

### Step 3: ファイルの状態確認
```bash
# 現在の状態確認
git status

# 詳細な状態確認
git status -s
```

**理解すべき状態**:
- `Untracked files`: まだGitで管理されていないファイル
- `Changes to be committed`: コミット対象として準備されたファイル
- `Changes not staged`: 変更されたが、まだステージングされていないファイル

---

## 📋 ハンズオン 3: 基本的なワークフロー

### Step 1: ファイルをステージングエリアに追加
```bash
# README.mdをステージングエリアに追加
git add README.md

# 状態確認
git status

# hello.pyも追加
git add hello.py

# 再び状態確認
git status
```

### Step 2: 初回コミット
```bash
# 初回コミット実行
git commit -m "初回コミット: READMEとhelloスクリプト追加"

# コミット結果確認
git status
```

### Step 3: コミット履歴の確認
```bash
# コミット履歴表示
git log

# 簡潔な履歴表示
git log --oneline

# 詳細な履歴（統計情報付き）
git log --stat
```

---

## 📝 ハンズオン 4: ファイルの変更とコミット

### Step 1: ファイルの変更
```bash
# hello.pyに機能追加
cat >> hello.py << 'EOF'

def farewell(name):
    """別れの挨拶をする関数"""
    return f"さようなら、{name}さん！"

# メイン部分の更新
if __name__ == "__main__":
    print(greet("世界"))
    print(farewell("世界"))
EOF
```

### Step 2: 変更内容の確認
```bash
# 変更内容の確認
git diff

# ファイルごとの変更確認
git diff hello.py

# 状態確認
git status
```

### Step 3: 変更のコミット
```bash
# 変更をステージング
git add hello.py

# ステージング済みの変更を確認
git diff --staged

# コミット実行
git commit -m "機能追加: farewell関数とメイン処理更新"

# 履歴確認
git log --oneline
```

---

## 🌿 ハンズオン 5: ブランチ操作

### Step 1: ブランチの作成と切り替え
```bash
# 現在のブランチ確認
git branch

# 新しいブランチ作成
git branch feature/calculator

# ブランチ一覧確認
git branch

# 新しいブランチに切り替え
git checkout feature/calculator

# または Git 2.23以降の新しいコマンド
# git switch feature/calculator

# 現在のブランチ確認
git branch
```

### Step 2: 新機能の開発
```bash
# 計算機能付きファイル作成
cat > calculator.py << 'EOF'
def add(a, b):
    """足し算"""
    return a + b

def subtract(a, b):
    """引き算"""
    return a - b

def multiply(a, b):
    """掛け算"""
    return a * b

def divide(a, b):
    """割り算"""
    if b == 0:
        return "ゼロで割ることはできません"
    return a / b

if __name__ == "__main__":
    print(f"5 + 3 = {add(5, 3)}")
    print(f"5 - 3 = {subtract(5, 3)}")
    print(f"5 * 3 = {multiply(5, 3)}")
    print(f"5 / 3 = {divide(5, 3)}")
EOF

# ファイル追加とコミット
git add calculator.py
git commit -m "計算機能追加: 四則演算の実装"
```

### Step 3: mainブランチとの比較
```bash
# mainブランチの内容確認
git checkout main
ls -la

# feature/calculatorブランチの内容確認
git checkout feature/calculator
ls -la

# ブランチ間の差分確認
git diff main feature/calculator
```

---

## 🔀 ハンズオン 6: マージ操作

### Step 1: mainブランチへのマージ
```bash
# mainブランチに切り替え
git checkout main

# 現在の状態確認
ls -la

# feature/calculatorブランチをマージ
git merge feature/calculator

# マージ後の確認
ls -la
git log --oneline
```

### Step 2: ブランチの削除
```bash
# マージ済みブランチの削除
git branch -d feature/calculator

# ブランチ一覧確認
git branch
```

---

## ⚔️ ハンズオン 7: コンフリクト（競合）の解決

### Step 1: 競合状況の作成
```bash
# 新しいブランチ作成
git checkout -b feature/improved-greeting

# hello.pyの修正（ブランチA）
sed -i 's/こんにちは/おはよう/g' hello.py
git add hello.py
git commit -m "挨拶を朝の挨拶に変更"

# mainブランチに戻る
git checkout main

# hello.pyの修正（ブランチB - 競合する変更）
sed -i 's/こんにちは/こんばんは/g' hello.py
git add hello.py
git commit -m "挨拶を夜の挨拶に変更"
```

### Step 2: 競合の発生とマージ
```bash
# マージ実行（競合が発生）
git merge feature/improved-greeting

# 競合状況の確認
git status

# 競合ファイルの内容確認
cat hello.py
```

### Step 3: 競合の解決
```bash
# エディタで競合を解決（nanoを使用）
nano hello.py

# 以下のように手動で編集:
# <<<<<<< HEAD
# こんばんは
# =======
# おはよう
# >>>>>>> feature/improved-greeting
# 
# この部分を、例えば「こんにちは」に変更

# 解決後、ファイルを確認
cat hello.py

# 解決したファイルをステージング
git add hello.py

# マージコミット完了
git commit -m "コンフリクト解決: 挨拶を統一"

# 履歴確認
git log --oneline --graph
```

---

## 🔄 ハンズオン 8: 変更の取り消し

### Step 1: 作業ディレクトリの変更取り消し
```bash
# ファイルを変更
echo "一時的な変更" >> hello.py

# 変更確認
git diff hello.py

# 変更を取り消し
git checkout -- hello.py

# 取り消し結果確認
git diff hello.py
```

### Step 2: ステージングの取り消し
```bash
# ファイルを変更してステージング
echo "テスト変更" >> hello.py
git add hello.py

# ステージング状況確認
git status

# ステージングを取り消し
git reset HEAD hello.py

# 取り消し結果確認
git status
```

### Step 3: コミットの取り消し
```bash
# 適当なコミットを作成
echo "取り消し予定の変更" >> hello.py
git add hello.py
git commit -m "取り消し予定のコミット"

# 履歴確認
git log --oneline

# 直前のコミットを取り消し（変更は保持）
git reset --soft HEAD~1

# 状況確認
git status
git log --oneline
```

---

## 🌐 ハンズオン 9: GitHub連携（オプション）

### Step 1: リモートリポジトリの設定
```bash
# 注意: 実際のGitHubアカウントが必要です
# GitHubでリポジトリを作成してからURLを設定

# リモートリポジトリの追加（例）
# git remote add origin https://github.com/your-username/my-first-repo.git

# リモート情報確認
git remote -v
```

### Step 2: プッシュとプル（シミュレーション）
```bash
# プッシュコマンドの説明（実際のリポジトリがあれば実行）
echo "git push -u origin main でリモートにプッシュ"

# プルコマンドの説明
echo "git pull origin main でリモートから更新取得"
```

---

## 📁 ハンズオン 10: .gitignoreファイル

### Step 1: 無視したいファイルの作成
```bash
# 無視したいファイルを作成
echo "print('テストファイル')" > test_temp.py
mkdir __pycache__
touch __pycache__/test.pyc
echo "secret_key=12345" > .env

# 現在の状態確認
git status
```

### Step 2: .gitignoreファイルの作成
```bash
# .gitignoreファイル作成
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python

# 環境設定ファイル
.env
.venv
env/
venv/

# 一時ファイル
*_temp.py
*.tmp

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
EOF

# .gitignoreの効果確認
git status

# .gitignore自体をコミット
git add .gitignore
git commit -m ".gitignore追加: Python用の無視ファイル設定"
```

---

## ✅ 実習チェックリスト

### 基本設定
- [ ] ユーザー名とメールアドレスの設定
- [ ] エディタとカラー設定

### 基本操作
- [ ] `git init` でリポジトリ初期化
- [ ] `git add` でファイルステージング
- [ ] `git commit` で変更コミット
- [ ] `git status` で状態確認
- [ ] `git log` で履歴確認

### ブランチ操作
- [ ] `git branch` でブランチ作成
- [ ] `git checkout` でブランチ切り替え
- [ ] `git merge` でブランチマージ

### 変更管理
- [ ] `git diff` で変更内容確認
- [ ] `git reset` でステージング取り消し
- [ ] `git checkout --` で変更取り消し

### 高度な操作
- [ ] コンフリクトの解決
- [ ] `.gitignore` の設定

---

## 🧪 実習課題: 完全なプロジェクト管理

### 課題: データ分析プロジェクトの管理
```bash
# 1. 新しいプロジェクト作成
mkdir data-project-git
cd data-project-git
git init

# 2. 基本ファイル作成
echo "# データ分析プロジェクト" > README.md
echo "pandas==1.5.3" > requirements.txt

# 3. 初回コミット  
git add .
git commit -m "初回コミット: プロジェクト基盤"

# 4. データ読み込み機能をブランチで開発
git checkout -b feature/data-loading
cat > data_loader.py << 'EOF'
import pandas as pd

def load_csv(filename):
    """CSVファイルを読み込む"""
    return pd.read_csv(filename)

def validate_data(df):
    """データの基本検証"""
    print(f"データ形状: {df.shape}")
    print(f"欠損値数: {df.isnull().sum().sum()}")
    return df
EOF

git add data_loader.py
git commit -m "データ読み込み機能実装"

# 5. メインブランチにマージ
git checkout main
git merge feature/data-loading

# 6. 分析機能をブランチで開発
git checkout -b feature/analysis
cat > analyzer.py << 'EOF'
def basic_stats(df):
    """基本統計量を計算"""
    return df.describe()

def correlation_matrix(df):
    """相関行列を計算"""
    return df.corr()
EOF

git add analyzer.py
git commit -m "分析機能実装"

# 7. .gitignore追加
cat > .gitignore << 'EOF'
*.csv
__pycache__/
.ipynb_checkpoints/
EOF

git add .gitignore
git commit -m ".gitignore追加"

# 8. メインブランチにマージ
git checkout main
git merge feature/analysis

# 9. 最終的な履歴確認
git log --oneline --graph --all
```

---

## 🎓 まとめと次のステップ

### 今日習得したスキル
1. **Git基本概念**: リポジトリ、ステージング、コミット、ブランチ
2. **基本ワークフロー**: add → commit → push の流れ
3. **ブランチ戦略**: 機能別開発とマージ
4. **競合解決**: コンフリクトの理解と解決方法
5. **プロジェクト管理**: .gitignore、履歴管理

### 実務での活用方法
```bash
# 日常的な開発フロー
git checkout main
git pull origin main
git checkout -b feature/new-feature
# 開発作業...
git add .
git commit -m "機能実装"
git checkout main
git merge feature/new-feature
git push origin main
```

### 推奨する練習方法
1. **毎日のコミット**: 小さな変更でも定期的にコミット
2. **意味のあるコミットメッセージ**: 何を変更したか明確に記述
3. **ブランチの活用**: 機能やバグ修正ごとにブランチを作成
4. **定期的なプッシュ**: リモートリポジトリへの定期的なバックアップ

---

## 🔗 参考リンク
- [Git公式ドキュメント](https://git-scm.com/doc)
- [次のステップ: Poetry + Git 統合実習](../integration_project/README.md)

お疲れさまでした！Gitの基本操作をマスターできました。
次は Poetry と Git を組み合わせた実際の開発フローを体験しましょう！ 