# 研修コンテンツ公開・配信ガイド

## 1. GitHub活用戦略

### 基本構成
```
ai-training-program/
├── README.md                 # メインページ
├── docs/                     # 文書管理
│   ├── getting-started.md
│   ├── curriculum.md
│   └── faq.md
├── 01_fundamentals/          # Phase1: 基礎編
├── 02_machine_learning/      # Phase2: ML編
├── 03_deep_learning/         # Phase3: DL編
├── 04_practical/             # Phase4: 実践編
├── resources/                # 共通リソース
│   ├── datasets/
│   ├── templates/
│   └── tools/
└── .github/
    ├── workflows/            # CI/CD
    ├── ISSUE_TEMPLATE/       # 質問テンプレート
    └── PULL_REQUEST_TEMPLATE.md
```

### GitHub Features活用

#### Issues Templates
- **質問用**: 受講者からの技術的質問
- **バグ報告**: コンテンツの間違い報告
- **改善提案**: カリキュラム改善のアイデア

#### GitHub Actions
- **自動テスト**: ノートブックのコード実行テスト
- **ドキュメント更新**: READMEの自動生成
- **リンクチェック**: 外部リンクの生存確認

#### GitHub Pages
- **静的サイト生成**: Jekyll/Hugo使用
- **カスタムドメイン**: training.yourcompany.com
- **SSL対応**: 自動HTTPS化

## 2. 段階的公開戦略

### フェーズ1: 内部テスト（1-2ヶ月）
- **プライベートリポジトリ**で開始
- 社内エンジニア5-10名でパイロット実施
- フィードバック収集・改善

### フェーズ2: 限定公開（2-3ヶ月）
- **招待制パブリックリポジトリ**
- パートナー企業や関係者に限定公開
- 実際の研修で検証

### フェーズ3: 一般公開（継続）
- **完全パブリック化**
- ブランディング・採用効果
- オープンソースコミュニティ構築

## 3. 配信プラットフォーム比較

| プラットフォーム | メリット | デメリット | 適用場面 |
|---|---|---|---|
| **GitHub Pages** | 無料、簡単、Git連携 | 静的サイトのみ | 基本の文書公開 |
| **GitBook** | 美しいUI、検索機能 | 有料プラン必要 | 本格的な文書サイト |
| **Jupyter Book** | 実行可能、科学計算特化 | 技術者向け | 技術研修メイン |
| **Docusaurus** | 多機能、カスタマイズ性 | 初期設定複雑 | 企業サイト統合 |
| **Notion** | リアルタイム編集 | 外部公開制限 | 社内研修 |

## 4. 推奨構成パターン

### パターンA: オープンソース型
```yaml
目的: ブランディング・コミュニティ構築
プラットフォーム: GitHub Pages + Jekyll
特徴:
  - 完全無料
  - SEO対策済み
  - コミュニティからの貢献期待
```

### パターンB: 企業研修特化型
```yaml
目的: 社内研修・顧客向けサービス
プラットフォーム: GitBook + プライベートリポジトリ
特徴:
  - アクセス制御
  - 分析機能
  - プロフェッショナルな見た目
```

### パターンC: ハイブリッド型
```yaml
目的: 内外両方での活用
プラットフォーム: Docusaurus + 複数リポジトリ
特徴:
  - 公開/非公開コンテンツ分離
  - 高度なカスタマイズ
  - 企業サイトとの統合
```

## 5. 実装ステップ

### Step 1: リポジトリ構築
```bash
# テンプレートリポジトリ作成
gh repo create ai-training-program --template --public

# 基本構造作成
mkdir -p {docs,01_fundamentals,02_machine_learning,03_deep_learning,04_practical}
mkdir -p {resources/{datasets,templates,tools},.github/{workflows,ISSUE_TEMPLATE}}
```

### Step 2: CI/CD設定
```yaml
# .github/workflows/test.yml
name: Test Notebooks
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
      - run: pip install -r requirements.txt
      - run: pytest --nbval **/*.ipynb
```

### Step 3: GitHub Pages設定
```yaml
# .github/workflows/pages.yml
name: Deploy to GitHub Pages
on:
  push:
    branches: [main]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-node@v3
      - run: npm install
      - run: npm run build
      - uses: peaceiris/actions-gh-pages@v3
```

## 6. 受講者管理

### GitHub Classroom活用
- **自動リポジトリ作成**: 受講者ごとの作業環境
- **課題自動採点**: GitHub Actions連携
- **進捗管理**: コミット履歴で学習状況把握

### アナリティクス活用
- **GitHub Insights**: リポジトリアクセス分析
- **Google Analytics**: サイト訪問者分析
- **カスタムダッシュボード**: 学習進捗可視化

## 7. 成功指標

### 定量指標
- リポジトリスター数
- コンテンツ利用者数
- Issues/PRの活発度
- 完了率・離脱率

### 定性指標
- 受講者満足度
- スキル向上度
- 企業ブランド向上
- 採用効果

---

このガイドを参考に、貴社の状況に最適な配信戦略を選択してください。 