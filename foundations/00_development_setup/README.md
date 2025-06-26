# 開発環境セットアップ基礎 - 共通基礎コース

## 学習目標
- 現代的なPython開発環境の理解
- WSL2環境でのLinux開発手法の習得
- Poetryによるパッケージ管理の習得
- Gitによるバージョン管理の基本操作
- プロジェクト立ち上げから運用までの全体フロー理解

## 対象者
- **新卒エンジニア**: プログラミング経験はあるが、プロジェクト立ち上げ未経験
- **転職者**: 個人開発経験はあるが、チーム開発やモダンなツールチェーン未経験
- **学生**: 授業でプログラミングは学んだが、実際の開発現場のワークフロー未経験

## 前提知識
- 基本的なプログラミング経験（Python、Java、C++等何でも可）
- 基本的なコマンドライン操作（cd、ls、mkdir等）
- Windows PCの基本操作

## 学習時間
- **WSL基礎**: 2時間
- **Poetry基礎**: 2時間
- **Git基礎**: 3時間
- **統合実習**: 2時間
- **総合演習**: 1時間

---

## なぜこれらのツールが重要なのか？

### 🚫 学生時代のプログラミング
```
my_project/
├── main.py
├── main_backup.py
├── main_final.py
├── main_final_v2.py
└── requirements.txt  # ←これすらない場合も
```

**問題点**:
- 環境が人によって違う → "私の環境では動くのに..."
- バージョン管理なし → 変更履歴が不明
- 依存関係が曖昧 → 他の人が環境構築できない
- Windowsでの開発 → 本番環境（Linux）との差異

### ✅ 現代的な開発環境
```bash
# 1. WSL2でLinux環境
wsl --install -d Ubuntu-24.04

# 2. Poetryでパッケージ管理
poetry new my-project
poetry add pandas numpy

# 3. Gitでバージョン管理
git init
git add .
git commit -m "初回コミット"

# 4. 誰でも同じ環境を再現可能
git clone <repo-url>
poetry install
```

**メリット**:
- ✅ **環境統一**: 開発〜本番まで同じLinux環境
- ✅ **再現性**: 誰でも同じ環境を構築可能
- ✅ **履歴管理**: 変更を追跡、問題があれば戻せる
- ✅ **チーム開発**: 複数人での協調作業が可能

---

## 学習コンテンツ構成

### 1. WSL基礎（新卒エンジニア必修）
- **概要**: [wsl_basics/README.md](./wsl_basics/README.md)
- **実習**: [wsl_basics/hands_on.md](./wsl_basics/hands_on.md)

**学習内容**:
- WSL2とは何か？なぜ必要か？
- WindowsとLinuxの違いと使い分け
- Ubuntu 24.04のセットアップと基本操作
- ファイルシステムの理解
- 開発環境としてのWSLの活用

### 2. Poetry基礎
- **概要**: [poetry_basics/README.md](./poetry_basics/README.md)
- **実習**: [poetry_basics/hands_on.md](./poetry_basics/hands_on.md)

**学習内容**:
- Poetryとは何か？
- 依存関係管理の仕組み
- パッケージの追加・削除・更新
- 仮想環境の管理
- pyproject.tomlの理解

### 3. Git基礎
- **概要**: [git_basics/README.md](./git_basics/README.md)
- **実習**: [git_basics/hands_on.md](./git_basics/hands_on.md)

**学習内容**:
- Gitとは何か？
- 基本的なワークフロー（add, commit, push）
- ブランチの概念と使い方
- リモートリポジトリ操作
- 競合解決の基本

### 4. 統合実習
- **プロジェクト**: [integration_project/README.md](./integration_project/README.md)

**実習内容**:
- WSL + Poetry + Git を使った実際の開発フロー
- 新人エンジニアが最初に担当するような小規模プロジェクト
- 問題解決とトラブルシューティング

---

## 新卒エンジニアが理解すべき「プロジェクトライフサイクル」

### 📋 Phase 1: プロジェクト立ち上げ
```bash
# 1. 開発環境準備
wsl --install -d Ubuntu-24.04

# 2. プロジェクト初期化
mkdir my-data-project
cd my-data-project
poetry init
git init

# 3. 基本構造作成
mkdir src tests docs
touch README.md .gitignore
```

### 🔧 Phase 2: 開発環境構築
```bash
# 1. 依存関係定義
poetry add pandas numpy matplotlib
poetry add --group dev pytest black jupyter

# 2. 開発環境確認
poetry install
poetry shell

# 3. 初回コミット
git add .
git commit -m "初回コミット: プロジェクト基盤"
```

### 💻 Phase 3: 機能開発
```bash
# 1. 機能ブランチ作成
git checkout -b feature/data-analysis

# 2. コード実装
# src/data_analyzer.py を作成...

# 3. テスト作成
# tests/test_analyzer.py を作成...

# 4. コミット
git add .
git commit -m "データ分析機能実装"
```

### 🔄 Phase 4: 統合・デプロイ
```bash
# 1. メインブランチにマージ
git checkout main
git merge feature/data-analysis

# 2. 本番環境デプロイ準備
poetry export -f requirements.txt --output requirements.txt

# 3. リモートリポジトリにプッシュ
git push origin main
```

---

## 実践的な開発シナリオ

### 🎯 シナリオ: 「売上データ分析ツール開発」
**設定**: 新卒1年目、初めての単独プロジェクト担当

#### Week 0-1: 環境構築
- WSL2 + Ubuntu 24.04セットアップ
- Poetry + Gitの基本操作習得
- プロジェクト雛形作成

#### Week 0-2: 開発実践
- データ読み込み機能実装
- 基本的な分析機能実装
- テストコード作成

#### Week 0-3: 運用準備
- ドキュメント整備
- エラーハンドリング追加
- デプロイ準備

---

## 評価課題

### 最終課題: 「新人向けデータ分析プロジェクト構築」
**設定**: 新卒エンジニアとして初めてのプロジェクト立ち上げ
**時間**: 2時間
**要件**:

1. **環境構築** (30分)
   - WSL2環境でのプロジェクト作成
   - Poetry による依存関係管理
   - Git によるバージョン管理開始

2. **機能実装** (60分)
   - CSVデータ読み込み機能
   - 基本統計量計算機能
   - グラフ可視化機能
   - 適切なエラーハンドリング

3. **品質管理** (20分)
   - テストコード作成
   - README.md作成
   - 適切なコミットメッセージ

4. **発表準備** (10分)
   - 開発プロセスの振り返り
   - 学んだことの整理

**評価基準**:
- [ ] WSL環境での適切な開発 (20%)
- [ ] Poetry による依存関係管理 (20%)
- [ ] Git による適切なバージョン管理 (20%)
- [ ] 機能の実装品質 (20%)
- [ ] ドキュメントとテストの充実度 (20%)

---

## よくある新卒エンジニアの疑問

### 💭 Q: なぜWindowsじゃダメなの？
**A**: 本番環境の多くがLinuxだから
- Web サーバー: 90%以上がLinux
- データ分析基盤: ほぼLinux
- 機械学習環境: GPU活用でLinuxが主流
- 開発環境と本番環境を合わせることで問題を減らせる

### 💭 Q: なぜPoetryが必要？pipじゃダメ？
**A**: チーム開発での再現性のため
- pip: バージョンが曖昧、環境によって違うものがインストールされる
- Poetry: lockファイルで確実に同じ環境を再現
- 新人がプロジェクトに参加してもすぐに環境構築できる

### 💭 Q: なぜGitが必要？
**A**: 変更履歴とチーム開発のため
- 「昨日まで動いてたのに...」→ Gitで戻せる
- 複数人での開発→ 変更の競合を解決できる
- 機能追加→ ブランチで安全に開発できる

### 💭 Q: 覚えることが多すぎる...
**A**: 最初は基本操作だけでOK
- WSL: Ubuntu環境での基本操作
- Poetry: add, install, run の3コマンド
- Git: add, commit, push の3コマンド
- 慣れてから高度な機能を学習

---

## トラブルシューティング

### 新卒エンジニアがハマりがちな問題

#### WSL関連
- **問題**: WSLが起動しない
- **原因**: Windows の機能が有効化されていない
- **解決**: Windows機能の有効化 → 再起動

#### Poetry関連
- **問題**: "poetry command not found"
- **原因**: PATHが通っていない
- **解決**: ~/.bashrc の確認・再読み込み

#### Git関連
- **問題**: "Author identity unknown"
- **原因**: ユーザー情報が未設定
- **解決**: user.name と user.email の設定

#### 統合問題
- **問題**: "仮想環境内でgitが使えない"
- **原因**: グローバルGit設定の問題
- **解決**: Git設定の確認・再設定

詳細は各セクションのトラブルシューティングを参照してください。

---

## 次のステップ

### 推奨学習順序（新卒エンジニア向け）
1. ✅ **WSL基礎** ← まずはここから
2. ⬜ **Poetry基礎**
3. ⬜ **Git基礎** 
4. ⬜ **統合実習**
5. ⬜ **統計学基礎** (Week 1)

### 実務適用チェックリスト
- [ ] WSL環境での日常的な開発
- [ ] 個人プロジェクトでPoetry使用
- [ ] Gitでのバージョン管理習慣化
- [ ] チーム開発での協調作業
- [ ] 問題発生時の適切な対処

### キャリア発展への道筋
1. **3ヶ月後**: 基本的な開発フローを習得
2. **6ヶ月後**: 中規模プロジェクトの担当
3. **1年後**: 新人のメンター担当
4. **2年後**: プロジェクトリーダー候補

---

💡 **新卒エンジニアへのメッセージ**: 
- 最初は覚えることが多く感じるかもしれませんが、これらのツールは現代の開発現場では「当たり前」に使われています
- 今習得しておけば、どの会社に行っても通用するスキルです
- 実際にコマンドを打って、エラーを経験して、解決することで身につきます
- 困ったときは遠慮なく先輩エンジニアに質問しましょう！ 