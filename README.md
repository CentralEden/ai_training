# 社内AI/データサイエンス研修プログラム

## 概要
本研修プログラムは、データサイエンティストのスキルレベルと専門分野に応じて体系的に学習できるコンテンツです。案件対応に直結する専門研修と、共通して必要な基礎知識を効率的に習得できます。

## 研修構造

### 📚 共通基礎コース（必修）
**対象**: 全データサイエンティスト  
**期間**: 5週間  
**内容**: 開発環境、統計学、Python、機械学習の基礎

### 🎯 専門分野別コース（選択）
**対象**: 担当案件に応じて選択  
**期間**: 3-4週間/分野  
**内容**: 専門技術の深度学習

### 📈 経験年数別上級コース（選択）
**対象**: シニア層・管理職  
**期間**: 2-6週間  
**内容**: マネジメント・コンサルティングスキル

---

## 📚 共通基礎コース詳細（5週間・必修）

### Week 0: 開発環境セットアップ
- [00_development_setup](./foundations/00_development_setup/) - 開発環境基礎
  - **Poetry基礎**: パッケージ管理、仮想環境、依存関係管理
  - **Git基礎**: バージョン管理、ブランチ操作、協調開発
  - **統合実習**: Poetry + Git を使った実践的開発フロー

### Week 1: 統計学基礎
- [01_descriptive_statistics](./foundations/01_descriptive_statistics/) - 記述統計学
- [02_probability_theory](./foundations/02_probability_theory/) - 確率論
- [03_statistical_inference](./foundations/03_statistical_inference/) - 統計的推定・検定

### Week 2: Python基礎
- [04_python_fundamentals](./foundations/04_python_fundamentals/) - Python基礎文法
- [05_data_manipulation](./foundations/05_data_manipulation/) - pandas・numpy
- [06_visualization](./foundations/06_visualization/) - matplotlib・seaborn

### Week 3: 機械学習基礎
- [07_ml_concepts](./foundations/07_ml_concepts/) - 機械学習概念
- [08_supervised_learning](./foundations/08_supervised_learning/) - 教師あり学習
- [09_unsupervised_learning](./foundations/09_unsupervised_learning/) - 教師なし学習

### Week 4: 実践基礎
- [10_data_preprocessing](./foundations/10_data_preprocessing/) - データ前処理
- [11_model_evaluation](./foundations/11_model_evaluation/) - モデル評価
- [12_foundations_project](./foundations/12_foundations_project/) - 基礎統合プロジェクト

---

## 🎯 専門分野別コース詳細（3-4週間・選択）

### 📈 時系列解析コース
**対象案件**: 需要予測、異常検知、金融分析  
**期間**: 4週間

- [ts_01_time_series_basics](./specializations/time_series/01_basics/) - 時系列データ基礎
- [ts_02_classical_methods](./specializations/time_series/02_classical/) - 古典的時系列分析
- [ts_03_modern_approaches](./specializations/time_series/03_modern/) - 機械学習・深層学習アプローチ
- [ts_04_forecasting_project](./specializations/time_series/04_project/) - 予測プロジェクト

### 🖼️ 画像認識・コンピュータビジョンコース
**対象案件**: 品質検査、医療画像診断、自動運転  
**期間**: 4週間

- [cv_01_image_processing](./specializations/computer_vision/01_processing/) - 画像処理基礎
- [cv_02_classical_cv](./specializations/computer_vision/02_classical/) - 古典的コンピュータビジョン
- [cv_03_deep_learning](./specializations/computer_vision/03_deep_learning/) - CNN・最新アーキテクチャ
- [cv_04_vision_project](./specializations/computer_vision/04_project/) - 画像認識プロジェクト

### 📝 自然言語処理コース
**対象案件**: チャットボット、文書分析、感情分析  
**期間**: 4週間

- [nlp_01_text_processing](./specializations/nlp/01_processing/) - テキスト処理基礎
- [nlp_02_classical_nlp](./specializations/nlp/02_classical/) - 古典的NLP手法
- [nlp_03_transformer_models](./specializations/nlp/03_transformers/) - Transformer・LLM
- [nlp_04_nlp_project](./specializations/nlp/04_project/) - NLPプロジェクト

### 🎯 レコメンデーションシステムコース
**対象案件**: ECサイト、コンテンツ推薦、マーケティング  
**期間**: 3週間

- [rec_01_recommendation_basics](./specializations/recommendation/01_basics/) - 推薦システム基礎
- [rec_02_collaborative_filtering](./specializations/recommendation/02_collaborative/) - 協調フィルタリング
- [rec_03_content_based](./specializations/recommendation/03_content_based/) - コンテンツベース推薦
- [rec_04_hybrid_systems](./specializations/recommendation/04_hybrid/) - ハイブリッド推薦システム

### 🔍 異常検知コース
**対象案件**: 設備監視、不正検知、品質管理  
**期間**: 3週間

- [ad_01_anomaly_detection_basics](./specializations/anomaly_detection/01_basics/) - 異常検知基礎
- [ad_02_statistical_methods](./specializations/anomaly_detection/02_statistical/) - 統計的手法
- [ad_03_machine_learning_methods](./specializations/anomaly_detection/03_ml_methods/) -機械学習手法
- [ad_04_anomaly_project](./specializations/anomaly_detection/04_project/) - 異常検知プロジェクト

### 🏭 データエンジニアリングコース
**対象案件**: データ基盤構築、パイプライン設計  
**期間**: 3週間

- [de_01_data_engineering_basics](./specializations/data_engineering/01_basics/) - データエンジニアリング基礎
- [de_02_data_pipelines](./specializations/data_engineering/02_pipelines/) - データパイプライン
- [de_03_cloud_platforms](./specializations/data_engineering/03_cloud/) - クラウドデータ基盤
- [de_04_de_project](./specializations/data_engineering/04_project/) - データ基盤構築プロジェクト

---

## 📈 経験年数別上級コース詳細

### 🎖️ シニアデータサイエンティストコース（3-5年経験）
**期間**: 3週間

- [senior_01_advanced_modeling](./advanced/senior/01_modeling/) - 高度なモデリング手法
- [senior_02_research_methods](./advanced/senior/02_research/) - 研究・実験手法
- [senior_03_technical_leadership](./advanced/senior/03_leadership/) - 技術リーダーシップ

### 🎯 プロジェクトマネージャーコース（5-8年経験）
**期間**: 4週間

- [pm_01_project_planning](./advanced/project_manager/01_planning/) - AIプロジェクト企画
- [pm_02_team_management](./advanced/project_manager/02_management/) - チームマネジメント
- [pm_03_stakeholder_management](./advanced/project_manager/03_stakeholder/) - ステークホルダー管理
- [pm_04_risk_management](./advanced/project_manager/04_risk/) - リスク管理

### 💼 コンサルタントコース（8年以上経験）
**期間**: 6週間

- [consultant_01_business_strategy](./advanced/consultant/01_strategy/) - ビジネス戦略
- [consultant_02_client_management](./advanced/consultant/02_client/) - クライアント対応
- [consultant_03_proposal_development](./advanced/consultant/03_proposal/) - 提案開発
- [consultant_04_industry_expertise](./advanced/consultant/04_industry/) - 業界専門知識
- [consultant_05_roi_analysis](./advanced/consultant/05_roi/) - ROI分析
- [consultant_06_consultant_capstone](./advanced/consultant/06_capstone/) - コンサル統合プロジェクト

## 環境構築（WSL + Poetry）

### 前提条件
- Windows 11/10 with WSL2
- Ubuntu 24.04 LTS (推奨)
- Python 3.13以上

### 1. WSL環境セットアップ
```bash
# WSL2のインストール（PowerShellで管理者権限）
wsl --install -d Ubuntu-24.04

# Ubuntu起動後、システム更新
sudo apt update && sudo apt upgrade -y

# Python関連ツールのインストール
sudo apt install -y python3-pip python3-venv python3-dev build-essential curl git
```

### 2. Poetryインストール
```bash
# Poetryの公式インストーラー使用
curl -sSL https://install.python-poetry.org | python3 -

# PATHに追加（~/.bashrcに追記）
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# インストール確認
poetry --version
```

### 3. プロジェクト環境構築
```bash
# リポジトリクローン
git clone <repository-url>
cd ai-ds-training-program

# 依存関係インストール
poetry install

# 開発用依存関係も含めてインストール
poetry install --with dev

# GPU環境の場合（オプション）
poetry install --with gpu

# 仮想環境をアクティベート
poetry shell
```

### 4. Jupyter環境起動
```bash
# JupyterLabの起動
poetry run jupyter lab

# またはJupyter Notebook
poetry run jupyter notebook

# 特定のポートで起動
poetry run jupyter lab --port=8888 --ip=0.0.0.0
```

### 5. 環境確認
```bash
# パッケージ一覧確認
poetry show

# 仮想環境の場所確認
poetry env info

# 依存関係ツリー表示
poetry show --tree
```

## 学習方法
1. 各フォルダの`README.md`で理論を学習
2. `notebook.ipynb`で実習を実施
3. `exercises/`で演習問題に取り組み
4. `projects/`で実践的なプロジェクトを完成

## 評価基準
- 理論テスト: 40%
- 実習課題: 40%
- 最終プロジェクト: 20%

## 受講パス選択ガイド

### 📋 基本的な受講フロー
```
1. 📚 共通基礎コース（4週間・必修）
   ↓
2. 🎯 専門分野別コース（3-4週間・案件に応じて選択）
   ↓
3. 📈 経験年数別上級コース（経験年数に応じて選択・任意）
```

### 🎯 専門分野選択の指針

| 担当案件の種類 | 推奨専門分野 | 期間 | 優先度 |
|----------------|--------------|------|--------|
| 売上予測・需要予測 | 📈 時系列解析 | 4週間 | 高 |
| 品質検査・画像診断 | 🖼️ 画像認識・CV | 4週間 | 高 |
| チャットボット・文書分析 | 📝 自然言語処理 | 4週間 | 高 |
| ECサイト・コンテンツ推薦 | 🎯 レコメンデーション | 3週間 | 中 |
| 設備監視・不正検知 | 🔍 異常検知 | 3週間 | 中 |
| データ基盤・パイプライン | 🏭 データエンジニアリング | 3週間 | 中 |

### 🎖️ 経験年数別キャリアパス

| 経験年数 | 役職 | コース | 主な学習内容 |
|----------|------|--------|--------------|
| 0-3年 | ジュニアDS | 共通基礎 + 専門分野 | 技術スキル習得 |
| 3-5年 | シニアDS | + シニアコース | 高度なモデリング・技術リーダーシップ |
| 5-8年 | プロジェクトマネージャー | + PMコース | チーム管理・プロジェクト推進 |
| 8年以上 | コンサルタント | + コンサルコース | ビジネス戦略・クライアント対応 |

### 🗓️ 受講スケジュール例

#### パターンA: 新人データサイエンティスト
```
Month 1: 共通基礎コース（4週間）
Month 2: 時系列解析コース（4週間）
→ 担当案件: 小売業売上予測プロジェクト
```

#### パターンB: 中堅データサイエンティスト
```
Month 1: 共通基礎コース（4週間）
Month 2: 画像認識コース（4週間）
Month 3: シニアコース（3週間）
→ 担当案件: 製造業品質検査システム開発リーダー
```

#### パターンC: 経験豊富なプロジェクトマネージャー
```
Month 1: 共通基礎コース（4週間）
Month 2: 異常検知コース（3週間）
Month 3: PMコース（4週間）
→ 担当案件: 金融機関不正検知システムPM
```

## 📚 関連ドキュメント

### 🌐 オンラインツール（GitHub Pages）
- [🎯 キャリア診断サイト](https://CentralEden.github.io/ai_training/) - **オンラインで診断ツールを利用！**
- [📊 インタラクティブ診断](https://CentralEden.github.io/ai_training/career_path_interactive.html) - **自動計算でリアルタイム診断！**

### 📖 ドキュメント
- [🚀 AIエンジニア キャリアパス別学習ガイド](docs/ai_career_paths_guide.md) - **将来のキャリア設計に必読！**
- [🎯 キャリアパス選択支援ツール](docs/career_path_selector.md) - **あなたに最適なキャリアを診断！**
- [社内限定運用ガイド](docs/internal_deployment_guide.md)
- [案件対応型研修設計](docs/case_based_learning_guide.md)
- [WSL環境セットアップ](docs/wsl_setup_guide.md)

## 社内学習サポート

### 質問・相談
- **技術的質問**: [Issues](../../issues)で受付
- **キャリア相談**: hr-ai@company.com
- **緊急連絡**: training@company.com

### 学習コミュニティ
- **Slack**: #ai-training-program
- **定期勉強会**: 毎週金曜 17:00-18:00
- **メンター制度**: 各パス経験者がサポート

### 学習環境
- **社内Jupyter Hub**: training.internal.company.com
- **GPU環境**: 申請制で利用可能
- **データセット**: 社内データ活用可能

## 受講管理

### 受講登録
1. 人事システムで受講申請
2. キャリア適性診断
3. 学習パス決定
4. 環境アクセス権付与

### 進捗管理
- **週次レポート**: 必須
- **中間評価**: 各Phase終了時
- **最終評価**: 修了時に認定証発行

## 運営体制
- **プログラム責任者**: [技術統括責任者]
- **実装者パス講師**: [シニアエンジニア陣]
- **コンサルパス講師**: [事業開発リーダー陣]
- **マネージャーパス講師**: [部長・マネージャー陣]

---
💡 **学習のコツ**: 毎日少しずつでも継続することが重要です！ 