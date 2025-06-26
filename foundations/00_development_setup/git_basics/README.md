# Git基礎ガイド

## 学習目標
- Gitの基本概念と重要性を理解する
- Gitの初期設定とセットアップができる
- 基本的なワークフロー（add, commit, push）をマスターする
- ブランチ操作とマージの基本を理解する
- リモートリポジトリとの連携ができる

## 所要時間: 3時間

---

## 1. Gitとは何か？

### 🎯 一言で言うと
**Git**は、ソースコードのバージョン管理システムです。ファイルの変更履歴を記録し、以前のバージョンに戻すことができます。

### 🚫 バージョン管理なしの問題
```
project/
├── analysis.py
├── analysis_backup.py
├── analysis_final.py
├── analysis_final_v2.py
├── analysis_final_v2_fixed.py
└── analysis_really_final.py
```
- どれが最新？
- 何が変更されたか不明
- 複数人で作業すると混乱
- バックアップが不確実

### ✅ Gitによる解決
```bash
git log --oneline
a1b2c3d データ可視化機能追加
d4e5f6g バグ修正: 欠損値処理
g7h8i9j 初回コミット
```
- 変更履歴が明確
- いつでも過去のバージョンに戻れる
- 複数人での協調作業が可能
- 確実なバックアップ

## 2. Gitの基本概念

### 📁 リポジトリ（Repository）
プロジェクトのデータと履歴を保存する場所

### 🔄 ワークフロー
1. **作業ディレクトリ**: ファイルを編集
2. **ステージングエリア**: コミット対象を選択
3. **ローカルリポジトリ**: 変更を記録
4. **リモートリポジトリ**: 他の人と共有

```
作業ディレクトリ → ステージング → ローカルリポジトリ → リモートリポジトリ
   (編集)        (git add)    (git commit)      (git push)
```

### 🌿 ブランチ（Branch）
異なる機能や実験を並行して開発するための仕組み

## 3. Gitの初期設定

### 🔧 WSL2 Ubuntu 24.04環境での設定確認
```bash
# Gitのインストール確認
git --version
# 例: git version 2.34.1

# 現在の設定確認
git config --list
```

### 👤 ユーザー情報の設定
```bash
# 名前とメールアドレスの設定（必須）
git config --global user.name "山田太郎"
git config --global user.email "yamada@example.com"

# 設定確認
git config --global user.name
git config --global user.email
```

### 📝 エディタの設定
```bash
# デフォルトエディタの設定（VS Codeを使用）
git config --global core.editor "code --wait"

# nano を使用する場合
git config --global core.editor "nano"
```

### 🎨 出力の色設定
```bash
# カラー出力を有効化
git config --global color.ui auto
```

### 🔐 認証設定（GitHub用）
```bash
# 認証情報の保存（HTTPS使用時）
git config --global credential.helper store

# SSH鍵の生成（推奨）
ssh-keygen -t ed25519 -C "yamada@example.com"
# 公開鍵をGitHubに登録する必要があります
```

## 4. 基本的なワークフロー

### 🚀 リポジトリの初期化

#### 新しいプロジェクトの場合
```bash
# プロジェクトディレクトリ作成
mkdir my-data-project
cd my-data-project

# Gitリポジトリ初期化
git init

# 初期ファイル作成
echo "# My Data Project" > README.md
touch analysis.py
```

#### 既存のプロジェクトの場合
```bash
cd existing-project
git init
```

### 📋 ファイルの状態確認
```bash
# 現在の状態確認
git status

# 出力例:
# On branch main
# No commits yet
# 
# Untracked files:
#   (use "git add <file>..." to include in what will be committed)
#         README.md
#         analysis.py
```

### ➕ ファイルをステージングに追加
```bash
# 特定のファイルを追加
git add README.md

# 複数ファイルを追加
git add analysis.py data.csv

# 全てのファイルを追加
git add .

# 現在のディレクトリ以下の全てを追加
git add -A
```

### 💾 変更をコミット
```bash
# コミット実行
git commit -m "初回コミット: READMEと分析スクリプト追加"

# より詳細なコミットメッセージ
git commit -m "データ読み込み機能実装

- CSVファイルの読み込み機能追加
- 基本的なデータ型チェック
- エラーハンドリング改善"
```

### 📜 コミット履歴の確認
```bash
# コミット履歴表示
git log

# 簡潔な表示
git log --oneline

# グラフィカルな表示
git log --graph --oneline --all
```

## 5. ファイル操作とステージング

### 📄 ファイルの変更確認
```bash
# 変更内容の確認
git diff

# ステージング済みの変更を確認
git diff --staged

# 特定のファイルの変更を確認
git diff analysis.py
```

### 🔄 変更の取り消し

#### 作業ディレクトリの変更を取り消し
```bash
# 特定のファイルの変更を取り消し
git checkout -- analysis.py

# 全ての変更を取り消し
git checkout -- .
```

#### ステージングを取り消し
```bash
# 特定のファイルのステージングを取り消し
git reset HEAD analysis.py

# 全てのステージングを取り消し
git reset HEAD
```

#### コミットの取り消し
```bash
# 直前のコミットを取り消し（変更は保持）
git reset --soft HEAD~1

# 直前のコミットを取り消し（変更も破棄）
git reset --hard HEAD~1
```

## 6. ブランチ操作

### 🌿 ブランチの基本

#### ブランチの確認・作成
```bash
# 現在のブランチ確認
git branch

# 新しいブランチ作成
git branch feature/data-visualization

# ブランチを作成して切り替え
git checkout -b feature/data-cleaning

# または（Git 2.23以降）
git switch -c feature/data-cleaning
```

#### ブランチの切り替え
```bash
# 既存のブランチに切り替え
git checkout main
git switch main

# ブランチ切り替え前の状態確認
git status
```

### 🔀 マージ操作

#### 基本的なマージ
```bash
# mainブランチに切り替え
git checkout main

# feature/data-visualizationブランチをマージ
git merge feature/data-visualization
```

#### コンフリクト（競合）の解決
```bash
# コンフリクトが発生した場合
git status
# 競合ファイルを手動で編集
# <<<<<<< HEAD
# =======
# >>>>>>> feature/data-visualization
# の箇所を修正

# 修正後
git add .
git commit -m "コンフリクト解決"
```

## 7. リモートリポジトリ操作

### 🌐 GitHubとの連携

#### 新しいリポジトリの作成
```bash
# GitHub上でリポジトリ作成後
git remote add origin https://github.com/username/my-data-project.git

# 初回プッシュ
git push -u origin main
```

#### 既存のリポジトリのクローン
```bash
# リポジトリのクローン
git clone https://github.com/username/my-data-project.git
cd my-data-project
```

### 📤 プッシュとプル

#### プッシュ（ローカル→リモート）
```bash
# 変更をリモートにプッシュ
git push origin main

# 新しいブランチをプッシュ
git push -u origin feature/new-analysis
```

#### プル（リモート→ローカル）
```bash
# リモートの変更を取得
git pull origin main

# フェッチ（取得のみ）
git fetch origin

# 変更の確認後にマージ
git merge origin/main
```

## 8. 実践例: データ分析プロジェクト

### 🎪 シナリオ
売上データの分析プロジェクトをGitで管理してみましょう。

```bash
# 1. プロジェクト作成・初期化
mkdir sales-analysis
cd sales-analysis
git init

# 2. 初期ファイル作成
echo "# 売上データ分析プロジェクト" > README.md
touch analysis.py requirements.txt
git add .
git commit -m "初回コミット: プロジェクト初期化"

# 3. データ読み込み機能の開発
git checkout -b feature/data-loading
# analysis.pyを編集...
git add analysis.py
git commit -m "データ読み込み機能実装"

# 4. mainブランチにマージ
git checkout main
git merge feature/data-loading

# 5. 可視化機能の開発
git checkout -b feature/visualization
# 可視化コードを追加...
git add .
git commit -m "売上トレンドグラフ機能追加"

# 6. GitHubにプッシュ
git remote add origin https://github.com/username/sales-analysis.git
git push -u origin main
git push -u origin feature/visualization
```

## 9. 便利なコマンド集

### 🔧 日常的に使うコマンド
```bash
# 状態確認
git status

# 変更内容確認
git diff

# ファイル追加
git add <file>

# コミット
git commit -m "メッセージ"

# ブランチ作成・切り替え
git checkout -b <branch-name>

# マージ
git merge <branch-name>

# プッシュ
git push origin <branch-name>

# プル
git pull origin <branch-name>
```

### 🔍 履歴・情報確認
```bash
# コミット履歴
git log --oneline

# ブランチ一覧
git branch -a

# リモート情報
git remote -v

# 特定のコミットの詳細
git show <commit-hash>

# ファイルの変更履歴
git log --follow <file>
```

### 🧹 クリーンアップ
```bash
# マージ済みブランチの削除
git branch -d feature/completed-feature

# リモートブランチの削除
git push origin --delete feature/old-feature

# 不要なファイルの削除
git clean -f
```

## 10. .gitignoreファイル

### 📝 .gitignoreの作成
```bash
# .gitignoreファイル作成
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/

# Jupyter Notebook
.ipynb_checkpoints

# データファイル
*.csv
*.xlsx
data/
!data/sample/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Poetry
poetry.lock
EOF

git add .gitignore
git commit -m ".gitignore追加"
```

## 11. トラブルシューティング

### ❌ よくあるエラーと解決法

#### "Author identity unknown"
```bash
# ユーザー情報の設定
git config user.name "Your Name"
git config user.email "your@email.com"
```

#### "fatal: not a git repository"
```bash
# Gitリポジトリの初期化
git init
```

#### "Your branch is ahead of 'origin/main' by X commits"
```bash
# リモートにプッシュ
git push origin main
```

#### プッシュが拒否される
```bash
# リモートの変更を先に取得
git pull origin main
# コンフリクトがあれば解決
git push origin main
```

### 🔧 緊急時の対処法
```bash
# 全ての変更を破棄して最新の状態に戻す
git reset --hard HEAD

# 特定のコミットまで戻す
git reset --hard <commit-hash>

# 作業ディレクトリを一時的に保存
git stash
# 作業を復元
git stash pop
```

## 12. まとめ

### ✅ できるようになったこと
- [ ] Gitの基本概念の理解
- [ ] 初期設定とセットアップ
- [ ] 基本的なワークフロー（add, commit, push）
- [ ] ブランチ操作とマージ
- [ ] リモートリポジトリとの連携
- [ ] トラブルシューティング

### 🚀 次のステップ
1. **実際のプロジェクトで練習**: 毎日のコミット習慣をつける
2. **ブランチ戦略の学習**: Git Flow, GitHub Flowの理解
3. **協調作業**: Pull Request, Code Reviewの実践

### 💡 実務での活用ポイント
- **頻繁なコミット**: 小さな変更でも定期的にコミット
- **意味のあるコミットメッセージ**: 後から見てわかりやすい説明
- **ブランチの活用**: 機能ごとに別ブランチで開発
- **リモートバックアップ**: 定期的にプッシュしてバックアップ

### 🔄 推奨ワークフロー
```bash
# 1. 作業開始前
git pull origin main

# 2. 新機能開発
git checkout -b feature/new-feature

# 3. 定期的なコミット
git add .
git commit -m "Progress: 機能Xの実装中"

# 4. 完了時
git checkout main
git merge feature/new-feature
git push origin main
```

---

📚 **参考資料**:
- [Git公式ドキュメント](https://git-scm.com/doc)
- [Atlassian Git チュートリアル](https://www.atlassian.com/git/tutorials)
- [GitHub Git ハンドブック](https://guides.github.com/introduction/git-handbook/)

次は [hands_on.md](./hands_on.md) で実際に手を動かして練習しましょう！ 