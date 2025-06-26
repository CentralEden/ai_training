# WSL基礎 - Windows Subsystem for Linux

## 学習目標
- WSL2の概念と必要性の理解
- Ubuntu 24.04の基本操作習得
- WindowsとLinuxの違いと使い分け
- 開発環境としてのWSLの活用方法

## 対象者
- **新卒エンジニア**: Linuxに触れたことがない
- **Windows開発者**: Linux環境での開発に移行したい
- **学生**: 授業でLinuxコマンドは習ったが実際の開発での使い方がわからない

## 前提知識
- Windows PCの基本操作
- コマンドプロンプトまたはPowerShellの基本操作（cd、dir等）
- プログラミングの基本概念

## 学習時間
- **理論**: 30分
- **実習**: 90分
- **合計**: 2時間

---

## なぜWSLが必要なのか？

### 🤔 新卒エンジニアの疑問
**「なぜWindowsじゃダメなの？Visual Studioで開発すればいいじゃん？」**

### 📊 現実の開発現場

#### Web開発・データサイエンスの現場
```
開発環境      本番環境
Windows  →   Linux (90%以上)
   ↑            ↑
  違う環境    実際の本番
```

**問題例**:
- Windows: `C:\Users\user\project\data.csv`
- Linux: `/home/user/project/data.csv`
- → パスの書き方が違う → 本番でエラー

#### 実際の失敗例
```python
# Windows開発者が書いたコード
file_path = "C:\\data\\sales.csv"  # Windowsパス
df = pd.read_csv(file_path)

# 本番環境（Linux）にデプロイ
# → FileNotFoundError: C:\data\sales.csv が見つからない
# → 緊急対応で深夜残業...😰
```

### ✅ WSLを使うメリット

#### 1. **環境統一**
```bash
# 開発環境（WSL）
/home/user/project/data.csv

# 本番環境（Linux）  
/home/user/project/data.csv
# → 同じパス、同じコマンド、同じ動作！
```

#### 2. **ツールチェーンの統一**
```bash
# Linux系のツールがそのまま使える
docker run -it ubuntu:24.04    # Docker
kubectl get pods               # Kubernetes  
ssh user@server               # SSH接続
crontab -e                    # 定期実行
```

#### 3. **学習効率の向上**
- ネット上の技術記事の90%がLinux前提
- Stack Overflowの回答もLinux前提
- 先輩エンジニアもLinuxで作業

---

## WSL2とは何か？

### 🔍 技術的な説明

**WSL (Windows Subsystem for Linux)**
- MicrosoftがWindows上でLinuxを動かすために開発
- 仮想マシンより軽量、ネイティブより高性能
- Windows 10/11に標準搭載

**WSL1 vs WSL2**
```
WSL1: Linux互換レイヤー（翻訳機能）
WSL2: 軽量な仮想マシン（本物のLinuxカーネル）
```

### 🎯 新卒エンジニア向け簡単説明

**「WindowsパソコンにLinuxを入れる魔法」**

```
┌─────────────────────────────────┐
│          Windows 11             │
│  ┌─────────────────────────────┐ │
│  │     Ubuntu 24.04           │ │
│  │   (Linux環境)              │ │
│  │                            │ │
│  │  $ python data_analysis.py │ │
│  │  $ git commit -m "実装完了" │ │
│  └─────────────────────────────┘ │
│                                 │
│  Chrome, VS Code, Slack         │
└─────────────────────────────────┘
```

**メリット**:
- Windowsアプリ（Chrome、VS Code）はそのまま使える
- Linux環境（開発用）も同時に使える
- 再起動不要で両方使える

---

## Ubuntu 24.04について

### 🐧 Ubuntuとは？
- **Linux**の代表的なディストリビューション（種類）
- **初心者に優しい**設計
- **企業での採用率が高い**（AWS、Google Cloud等）
- **24.04**: 2024年4月リリースの最新LTS版

### 📅 LTSとは？
**Long Term Support（長期サポート）**
- 5年間のセキュリティアップデート保証
- 企業での採用が多い
- 安定性重視

```
Ubuntu バージョン履歴:
20.04 LTS (2020年) ← 古い
22.04 LTS (2022年) ← まだ使われている  
24.04 LTS (2024年) ← 最新・推奨 ★
```

---

## WindowsとLinuxの違い

### 📁 ファイルシステム

#### Windows
```
C:\
├── Users\
│   └── username\
│       ├── Documents\
│       └── Desktop\
├── Program Files\
└── Windows\
```

#### Linux (Ubuntu)
```
/
├── home/
│   └── username/
│       ├── Documents/
│       └── Desktop/
├── usr/
├── etc/
└── var/
```

**重要な違い**:
- Windows: `\` (バックスラッシュ)
- Linux: `/` (スラッシュ)
- Windows: ドライブレター (C:, D:)
- Linux: すべて `/` から開始

### 💻 コマンドの違い

| 操作 | Windows | Linux |
|------|---------|-------|
| ディレクトリ一覧 | `dir` | `ls` |
| ディレクトリ移動 | `cd` | `cd` |
| ファイル作成 | `type nul > file.txt` | `touch file.txt` |
| ファイル削除 | `del file.txt` | `rm file.txt` |
| 現在位置表示 | `cd` | `pwd` |

### 🔐 権限システム

#### Windows
```
- 管理者権限
- 一般ユーザー権限
```

#### Linux
```
- root (管理者)
- 一般ユーザー
- グループ権限
- ファイル毎の詳細権限 (rwx)
```

**実例**:
```bash
# ファイル権限表示
$ ls -la
-rw-r--r-- 1 user user 1024 Dec 10 10:00 data.csv
│││││││││
│││││││└─ その他の権限
│││││└─── グループ権限  
│││└───── 所有者権限
││└────── ディレクトリフラグ
│└─────── ファイルタイプ
└──────── 権限情報
```

---

## WSL環境での開発フロー

### 🚀 典型的な1日の作業フロー

#### 朝の作業開始
```bash
# 1. WSLを起動
wsl

# 2. プロジェクトディレクトリに移動
cd ~/projects/data-analysis

# 3. 仮想環境の有効化
poetry shell

# 4. 最新コードを取得
git pull origin main
```

#### 開発作業
```bash
# 5. 新機能ブランチ作成
git checkout -b feature/new-analysis

# 6. VS Codeで開発
code .  # VS CodeがWindows側で起動

# 7. Pythonスクリプト実行（Linux環境）
python src/analysis.py

# 8. テスト実行
pytest tests/
```

#### 作業終了
```bash
# 9. 変更をコミット
git add .
git commit -m "新しい分析機能を追加"

# 10. リモートにプッシュ
git push origin feature/new-analysis
```

### 🔄 ファイル共有の仕組み

#### WSLからWindowsファイルアクセス
```bash
# Windowsの C:\Users\username\Documents にアクセス
cd /mnt/c/Users/username/Documents

# WSLからWindowsファイルを編集可能
ls /mnt/c/Users/username/Desktop
```

#### WindowsからWSLファイルアクセス
```
エクスプローラーのアドレスバーに入力:
\\wsl$\Ubuntu-24.04\home\username
```

---

## 開発環境としてのWSL活用

### 🛠️ 推奨セットアップ

#### 1. **ターミナル**: Windows Terminal
```json
// Windows Terminal設定例
{
    "defaultProfile": "{Ubuntu-24.04のGUID}",
    "profiles": {
        "list": [
            {
                "name": "Ubuntu-24.04",
                "commandline": "wsl -d Ubuntu-24.04",
                "startingDirectory": "//wsl$/Ubuntu-24.04/home/username"
            }
        ]
    }
}
```

#### 2. **エディタ**: VS Code + WSL拡張
```bash
# WSL内でVS Code起動
code .

# 自動的にVS CodeのWSL拡張が動作
# → Linux環境でコード実行、Windows側でGUI表示
```

#### 3. **ファイル管理**: WSL内で完結
```bash
# プロジェクトファイルはWSL内に配置
~/projects/
├── data-analysis/
├── web-app/
└── machine-learning/

# WindowsのCドライブは使わない
# → パフォーマンス向上、パス問題解消
```

### ⚡ パフォーマンス最適化

#### ❌ 避けるべき構成
```bash
# WindowsファイルシステムでLinuxコマンド実行
cd /mnt/c/projects/my-project
python analysis.py  # 遅い！
```

#### ✅ 推奨構成
```bash
# WSLファイルシステムで作業
cd ~/projects/my-project  
python analysis.py  # 高速！
```

**パフォーマンス比較**:
- WSL内ファイル: 100%
- Windows内ファイル: 約30-50%（体感）

---

## 実践的な使い分け

### 💼 業務での使い分け例

#### Windows側で行う作業
- **ブラウザ**: Chrome、Edge（調査、資料作成）
- **Office**: Excel、PowerPoint（資料作成）
- **コミュニケーション**: Slack、Teams
- **設計**: Draw.io、Figma

#### WSL側で行う作業
- **プログラミング**: Python、Node.js実行
- **バージョン管理**: Git操作
- **パッケージ管理**: Poetry、npm
- **サーバー**: 開発サーバー起動
- **データベース**: PostgreSQL、MySQL

### 🎯 プロジェクト別推奨構成

#### データサイエンスプロジェクト
```bash
# WSL環境
~/projects/data-science/
├── notebooks/          # Jupyter Notebook
├── src/               # Pythonコード  
├── data/              # データファイル
├── tests/             # テストコード
└── pyproject.toml     # Poetry設定

# Windows環境
- Excel（データ確認）
- PowerPoint（発表資料）
- ブラウザ（Jupyter Notebook表示）
```

#### Webアプリ開発
```bash
# WSL環境  
~/projects/web-app/
├── backend/           # API開発
├── frontend/          # React等
├── docker-compose.yml # 環境構築
└── README.md

# Windows環境
- ブラウザ（アプリ確認）
- Figma（デザイン）
- Slack（チーム連携）
```

---

## トラブルシューティング

### 🚨 新卒エンジニアがハマりがちな問題

#### 1. WSLが起動しない
**症状**:
```
PS C:\> wsl
WSL 2 requires an update to its kernel component.
```

**原因**: WSL2カーネルが古い
**解決法**:
```powershell
# PowerShellを管理者権限で実行
wsl --update
wsl --shutdown
wsl
```

#### 2. Ubuntuが見つからない
**症状**:
```
PS C:\> wsl -d Ubuntu-24.04
指定されたディストリビューションは存在しません
```

**原因**: Ubuntu未インストール
**解決法**:
```powershell
# 利用可能なディストリビューション確認
wsl --list --online

# Ubuntu 24.04インストール
wsl --install -d Ubuntu-24.04
```

#### 3. ファイルアクセスが遅い
**症状**: WSLでの作業が異常に遅い
**原因**: WindowsファイルシステムでLinuxコマンド実行
**解決法**:
```bash
# ❌ 遅い（Windowsファイルシステム）
cd /mnt/c/projects
python script.py

# ✅ 高速（WSLファイルシステム）  
cd ~/projects
python script.py
```

#### 4. VS Codeが連携しない
**症状**: `code .` コマンドが動かない
**原因**: VS CodeのWSL拡張未インストール
**解決法**:
1. VS Codeに「WSL」拡張をインストール
2. WSL内で `code .` 実行

#### 5. 権限エラー
**症状**:
```bash
$ python script.py
Permission denied
```

**原因**: ファイルに実行権限がない
**解決法**:
```bash
# 実行権限付与
chmod +x script.py

# または
python script.py  # pythonコマンド経由
```

---

## 実習の準備

### ✅ 事前チェックリスト

#### Windows環境確認
```powershell
# Windows バージョン確認（10 build 19041以上必要）
winver

# WSL機能確認
dism.exe /online /get-featureinfo /featurename:Microsoft-Windows-Subsystem-Linux
```

#### WSL2有効化確認
```powershell
# WSL2がデフォルトか確認
wsl --status

# WSL2に設定
wsl --set-default-version 2
```

### 🎯 実習で学ぶこと

1. **Ubuntu 24.04インストール**
   - Microsoft Storeまたはコマンドラインインストール
   - 初期セットアップ（ユーザー作成、パスワード設定）

2. **基本操作習得**
   - ディレクトリ操作（cd、ls、mkdir）
   - ファイル操作（touch、cp、mv、rm）
   - 権限管理（chmod、chown）

3. **開発環境構築**
   - Python 3.13インストール
   - VS Code連携設定
   - Git設定

4. **実践的な作業フロー**
   - プロジェクト作成
   - ファイル編集
   - コマンド実行

---

## 学習のコツ

### 💡 効率的な学習方法

#### 1. **実際に手を動かす**
```bash
# 読むだけでなく、実際にコマンドを打つ
$ pwd
/home/username

$ ls -la
total 20
drwxr-xr-x 5 username username 4096 Dec 10 10:00 .
drwxr-xr-x 3 root     root     4096 Dec 10 09:00 ..
```

#### 2. **エラーを恐れない**
```bash
# エラーが出ても大丈夫！
$ rm -rf /
rm: cannot remove '/': Permission denied

# エラーメッセージを読んで理解する習慣
```

#### 3. **日常的に使う**
```bash
# 毎日の作業をWSLで行う
$ cd ~/projects/daily-work
$ git pull
$ python analysis.py
```

### 📚 参考資料

#### 公式ドキュメント
- [Microsoft WSL Documentation](https://docs.microsoft.com/en-us/windows/wsl/)
- [Ubuntu 24.04 Documentation](https://help.ubuntu.com/)

#### コミュニティ
- Stack Overflow（WSLタグ）
- Reddit r/bashonubuntuonwindows
- Ubuntu Forums

---

## 次のステップ

### 🎯 WSL習得後の学習パス

1. **Week 0完了後**
   - Poetry基礎 → パッケージ管理
   - Git基礎 → バージョン管理
   - 統合実習 → 実践的なワークフロー

2. **Week 1以降**
   - 統計学基礎
   - Python基礎
   - データサイエンス実践

### 🚀 実務適用目標

#### 1ヶ月後
- [ ] WSL環境での日常的な開発
- [ ] 基本的なLinuxコマンドの習得
- [ ] VS Code + WSL連携の活用

#### 3ヶ月後  
- [ ] チーム開発でのWSL活用
- [ ] Docker等の高度なツール使用
- [ ] 本番環境との差異を意識した開発

---

💡 **新卒エンジニアへのアドバイス**:
- 最初は「なぜLinuxを使うのか」がピンと来ないかもしれません
- でも実際に使ってみると、その便利さと重要性がわかります
- 困ったときは遠慮なく先輩に質問しましょう！
- WSLは現代の開発現場では「必須スキル」です 🌟 