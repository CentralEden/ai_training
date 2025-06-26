# WSL実習ガイド - 実際に手を動かして学ぼう

## 実習の目標
- WSL2 + Ubuntu 24.04の環境構築
- 基本的なLinuxコマンドの習得
- 開発環境としてのWSL活用方法の体験
- 実際のプロジェクト作成フローの実践

## 前提条件
- Windows 10 (build 19041以上) または Windows 11
- 管理者権限でのコマンド実行が可能
- インターネット接続環境

## 実習時間
- **合計**: 90分
- **Phase 1**: WSL環境構築 (30分)
- **Phase 2**: 基本操作習得 (30分)  
- **Phase 3**: 開発環境構築 (30分)

---

## Phase 1: WSL環境構築 (30分)

### ✅ Step 1: Windows機能の有効化 (5分)

#### 1-1. PowerShellを管理者権限で起動
```powershell
# Windows + X → "Windows PowerShell (管理者)"
# または
# Windows + R → "powershell" → Ctrl + Shift + Enter
```

#### 1-2. WSL機能を有効化
```powershell
# WSL機能を有効化
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

# 仮想マシン機能を有効化
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

# 再起動
Restart-Computer
```

**💡 ポイント**: 再起動が必要です。再起動後、次のステップに進んでください。

### ✅ Step 2: WSL2の設定 (5分)

#### 2-1. WSL2をデフォルトに設定
```powershell
# WSL2をデフォルトバージョンに設定
wsl --set-default-version 2

# WSLの状態確認
wsl --status
```

**期待する出力**:
```
既定のバージョン: 2
```

#### 2-2. WSLカーネル更新（必要に応じて）
```powershell
# WSLカーネルを最新に更新
wsl --update

# WSLを一度シャットダウン
wsl --shutdown
```

### ✅ Step 3: Ubuntu 24.04のインストール (20分)

#### 3-1. 利用可能なディストリビューション確認
```powershell
# インストール可能なLinuxディストリビューション一覧
wsl --list --online
```

**期待する出力**:
```
NAME                                   FRIENDLY NAME
Ubuntu                                 Ubuntu
Ubuntu-24.04                           Ubuntu 24.04 LTS
Ubuntu-22.04                           Ubuntu 22.04 LTS
...
```

#### 3-2. Ubuntu 24.04をインストール
```powershell
# Ubuntu 24.04 LTSをインストール
wsl --install -d Ubuntu-24.04
```

**💡 新卒エンジニア向けメモ**:
- ダウンロードに5-10分かかります
- インターネット速度によって時間が変わります
- 途中でエラーが出たら、再実行してみてください

#### 3-3. 初期セットアップ
インストール完了後、Ubuntu環境が自動的に起動します：

```bash
# ユーザー名を入力（英数字のみ、小文字推奨）
Enter new UNIX username: your-username

# パスワードを設定（入力時は表示されません）
New password: [パスワード入力]
Retype new password: [パスワード再入力]
```

**⚠️ 重要**: 
- ユーザー名は英数字のみ（日本語NG）
- パスワードは忘れないようにメモ！
- パスワード入力時は画面に表示されません（正常です）

#### 3-4. インストール確認
```bash
# Ubuntu環境で実行
whoami  # ユーザー名が表示される
pwd     # 現在位置が表示される (/home/your-username)
```

**期待する出力**:
```bash
$ whoami
your-username
$ pwd  
/home/your-username
```

---

## Phase 2: 基本操作習得 (30分)

### ✅ Step 4: ファイル・ディレクトリ操作 (15分)

#### 4-1. 基本的なナビゲーション
```bash
# 現在位置確認
pwd

# ディレクトリ内容確認
ls

# 詳細表示
ls -la

# ホームディレクトリに移動
cd ~
cd /home/your-username  # 同じ意味
```

**💡 新卒エンジニア向け解説**:
```bash
# ls -la の見方
drwxr-xr-x 2 user user 4096 Dec 10 10:00 Documents
│││││││││
│││││││└─ その他ユーザーの権限 (r-x: 読み・実行可)
│││││└─── グループの権限 (r-x: 読み・実行可)  
│││└───── 所有者の権限 (rwx: 読み・書き・実行可)
││└────── ディレクトリかファイルか (d: ディレクトリ)
│└─────── ファイルタイプ
└──────── 権限情報
```

#### 4-2. ディレクトリ作成・移動
```bash
# プロジェクト用ディレクトリ作成
mkdir projects
mkdir projects/my-first-project

# または一度に作成
mkdir -p projects/data-analysis/src

# 作成確認
ls -la projects/

# ディレクトリに移動
cd projects/my-first-project
pwd  # 現在位置確認
```

#### 4-3. ファイル操作
```bash
# 空ファイル作成
touch README.md
touch main.py
touch data.csv

# ファイル一覧確認
ls -la

# ファイルに内容を書き込み
echo "# My First Project" > README.md
echo "print('Hello, WSL!')" > main.py

# ファイル内容確認
cat README.md
cat main.py
```

#### 4-4. ファイル・ディレクトリのコピー・移動
```bash
# ファイルコピー
cp main.py main_backup.py

# ディレクトリコピー（再帰的）
cp -r ../my-first-project ../my-first-project-backup

# ファイル移動・リネーム
mv main_backup.py backup/main.py  # ディレクトリを移動
mv data.csv sales_data.csv        # リネーム

# 確認
ls -la
```

### ✅ Step 5: 権限管理とプロセス操作 (15分)

#### 5-1. ファイル権限の確認・変更
```bash
# 現在の権限確認
ls -la main.py

# 実行権限付与
chmod +x main.py

# 権限確認（実行権限が追加されているか）
ls -la main.py

# Pythonスクリプト実行
python3 main.py
```

**期待する出力**:
```bash
$ python3 main.py
Hello, WSL!
```

#### 5-2. システム情報確認
```bash
# OS情報確認
cat /etc/os-release

# CPU情報
lscpu

# メモリ情報
free -h

# ディスク使用量
df -h

# 現在実行中のプロセス
ps aux | head -10
```

#### 5-3. パッケージ管理の基本
```bash
# パッケージリスト更新
sudo apt update

# Python 3.13インストール（まだの場合）
sudo apt install -y python3.13 python3.13-pip

# インストール確認
python3.13 --version
```

**💡 新卒エンジニア向けメモ**:
- `sudo`: 管理者権限で実行
- `apt`: Ubuntuのパッケージマネージャー
- `-y`: 確認なしでインストール実行

---

## Phase 3: 開発環境構築 (30分)

### ✅ Step 6: 開発ツールのセットアップ (15分)

#### 6-1. Git設定
```bash
# Git インストール確認
git --version

# Git未インストールの場合
sudo apt install -y git

# Git設定（あなたの情報に変更してください）
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# 設定確認
git config --list | grep user
```

#### 6-2. Python開発環境
```bash
# Python 3.13が使用可能か確認
python3.13 --version

# pipのアップグレード
python3.13 -m pip install --upgrade pip

# 基本的なツールインストール
python3.13 -m pip install poetry

# Poetry確認
poetry --version
```

#### 6-3. VS Code連携設定
```bash
# VS Code WSL拡張の動作確認
# まず、VS Codeが Windows側にインストールされていることを確認

# WSL内でVS Code起動テスト
code --version

# プロジェクトをVS Codeで開く
cd ~/projects/my-first-project
code .
```

**💡 トラブルシューティング**:
- `code` コマンドが見つからない場合:
  1. Windows側でVS Codeをインストール
  2. VS CodeでWSL拡張をインストール
  3. WSLを再起動

### ✅ Step 7: 実際の開発フロー体験 (15分)

#### 7-1. プロジェクト初期化
```bash
# 新しいプロジェクト作成
cd ~/projects
mkdir data-analysis-demo
cd data-analysis-demo

# Git初期化
git init

# Poetry プロジェクト初期化
poetry init --no-interaction --name data-analysis-demo

# 依存関係追加
poetry add pandas numpy matplotlib

# 開発用依存関係追加
poetry add --group dev pytest black
```

#### 7-2. サンプルコード作成
```bash
# メインスクリプト作成
cat << 'EOF' > main.py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    # サンプルデータ作成
    data = {
        'month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
        'sales': [100, 120, 140, 110, 160]
    }
    
    df = pd.DataFrame(data)
    print("Sales Data:")
    print(df)
    
    # 基本統計
    print(f"\nAverage Sales: {df['sales'].mean():.2f}")
    print(f"Max Sales: {df['sales'].max()}")
    
    return df

if __name__ == "__main__":
    result = main()
EOF

# テストファイル作成
mkdir tests
cat << 'EOF' > tests/test_main.py
import pytest
from main import main

def test_main():
    result = main()
    assert len(result) == 5
    assert 'sales' in result.columns
    assert result['sales'].mean() == 126.0
EOF
```

#### 7-3. 実行とテスト
```bash
# 仮想環境でスクリプト実行
poetry run python main.py

# テスト実行
poetry run pytest tests/

# コードフォーマット
poetry run black main.py tests/
```

**期待する出力**:
```bash
$ poetry run python main.py
Sales Data:
  month  sales
0   Jan    100
1   Feb    120
2   Mar    140
3   Apr    110
4   May    160

Average Sales: 126.00
Max Sales: 160

$ poetry run pytest tests/
===== test session starts =====
collected 1 item

tests/test_main.py .                                    [100%]
===== 1 passed in 0.05s =====
```

#### 7-4. Git管理
```bash
# .gitignore作成
cat << 'EOF' > .gitignore
__pycache__/
*.pyc
.pytest_cache/
.coverage
dist/
build/
*.egg-info/
EOF

# ファイルをステージング
git add .

# 初回コミット
git commit -m "Initial commit: データ分析プロジェクト作成"

# コミット履歴確認
git log --oneline
```

---

## 実習完了チェック

### ✅ 環境構築確認
以下のコマンドが正常に動作することを確認してください：

```bash
# WSL環境確認
wsl --status

# Ubuntu確認
lsb_release -a

# Python確認
python3.13 --version

# Poetry確認
poetry --version

# Git確認
git --version

# VS Code連携確認
code --version
```

### ✅ 操作スキル確認
以下の操作ができることを確認してください：

```bash
# ファイル・ディレクトリ操作
cd ~/projects
mkdir test-project
cd test-project
touch test.py
echo "print('Test')" > test.py
python3 test.py
rm test.py
cd ..
rmdir test-project

# Git操作
git init
git add .
git commit -m "Test commit"
git log --oneline

# Poetry操作
poetry new test-poetry-project
cd test-poetry-project
poetry add requests
poetry install
poetry run python -c "import requests; print('OK')"
```

---

## トラブルシューティング

### 🚨 よくある問題と解決法

#### 問題1: WSLが起動しない
**症状**:
```powershell
PS C:\> wsl
WSL 2 requires an update to its kernel component.
```

**解決法**:
```powershell
# WSLカーネル更新
wsl --update

# WSL再起動
wsl --shutdown
wsl
```

#### 問題2: Ubuntu 24.04が見つからない
**症状**:
```powershell
PS C:\> wsl -d Ubuntu-24.04
指定されたディストリビューションは存在しません
```

**解決法**:
```powershell
# インストール済みディストリビューション確認
wsl --list

# Ubuntu 24.04再インストール
wsl --install -d Ubuntu-24.04
```

#### 問題3: Poetry コマンドが見つからない
**症状**:
```bash
$ poetry --version
poetry: command not found
```

**解決法**:
```bash
# Poetry再インストール
curl -sSL https://install.python-poetry.org | python3 -

# PATHに追加
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# 確認
poetry --version
```

#### 問題4: VS Code連携がうまくいかない
**症状**: `code .` コマンドが動かない

**解決法**:
1. Windows側でVS Codeをインストール
2. VS CodeでWSL拡張をインストール
3. WSL内で `code .` を実行

#### 問題5: 権限エラー
**症状**:
```bash
$ ./script.py
Permission denied
```

**解決法**:
```bash
# 実行権限付与
chmod +x script.py

# または
python3 script.py
```

---

## 実習の振り返り

### 🎯 学んだこと
- [ ] WSL2 + Ubuntu 24.04の環境構築
- [ ] 基本的なLinuxコマンド操作
- [ ] ファイル・ディレクトリ管理
- [ ] 権限システムの理解
- [ ] Git基本操作
- [ ] Poetry基本操作
- [ ] VS Code連携

### 🚀 次のステップ
1. **日常的にWSLを使う**: 開発作業は全てWSL環境で
2. **Linuxコマンドに慣れる**: 毎日使って体に覚えさせる
3. **Poetry基礎学習**: 次の実習で詳しく学習
4. **Git基礎学習**: バージョン管理の基本を習得

### 💡 実務での活用
- **プロジェクト作成**: 必ずWSL環境で
- **コマンド操作**: GUI頼りからCLI中心へ
- **環境管理**: Poetry + Git の組み合わせ
- **チーム開発**: 環境統一の重要性を実感

---

## 追加練習課題

### 🏋️ 練習課題1: ファイル操作マスター (10分)
```bash
# 以下の構造を作成してください
~/practice/
├── documents/
│   ├── report.md
│   └── notes.txt
├── scripts/
│   ├── analyzer.py
│   └── utils.py
└── data/
    ├── input.csv
    └── output.csv

# 各ファイルに適当な内容を書き込み
# analyzer.py には実行権限を付与
# 最後に全体をtarで圧縮
```

### 🏋️ 練習課題2: 開発環境セットアップ (15分)
```bash
# 新しいプロジェクトを作成
# Poetry で pandas, numpy, matplotlib を追加
# Gitで管理開始
# サンプルコードを作成・実行
# テストコードを作成・実行
# 全てをコミット
```

### 🏋️ 練習課題3: トラブルシューティング (5分)
```bash
# 意図的にエラーを発生させて解決する練習
# 1. 存在しないディレクトリに移動
# 2. 権限のないファイルを実行
# 3. 存在しないコマンドを実行
# 4. Gitで設定なしでコミット
# 各エラーメッセージを読んで適切に解決
```

---

💡 **実習完了おめでとうございます！**
- WSL環境での開発の基礎が身につきました
- 次はPoetry基礎とGit基礎に進みましょう
- 分からないことがあれば遠慮なく質問してください
- 毎日少しずつでもWSLを使って慣れていきましょう！ 🌟 