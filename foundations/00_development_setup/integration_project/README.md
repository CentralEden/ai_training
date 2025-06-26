# Poetry + Git 統合実習プロジェクト

## 🎯 実習の目標
PoetryとGitを組み合わせた実際のデータ分析プロジェクトを通じて、現代的な開発フローを体験します。

## ⏱️ 所要時間: 2時間

---

## 📋 プロジェクト概要

### 🎪 シナリオ
小売業のECサイトの売上データを分析し、季節性トレンドと顧客セグメンテーションを行うプロジェクトを、Poetry + Git で管理します。

### 🎯 成果物
1. **データ分析パイプライン**: 読み込み、前処理、分析、可視化
2. **バージョン管理**: 機能別開発、履歴管理
3. **環境管理**: 依存関係の確実な管理
4. **ドキュメント**: README、コメント、分析レポート

---

## 🚀 Step 1: プロジェクト初期化

### Poetry + Git セットアップ
```bash
# 作業ディレクトリ作成
mkdir ec-sales-analysis
cd ec-sales-analysis

# Poetryプロジェクト初期化
poetry init

# 対話式設定（以下の情報を入力）
# Package name [ec-sales-analysis]: ec-sales-analysis
# Version [0.1.0]: 0.1.0
# Description []: ECサイト売上データの分析プロジェクト
# Author [Your Name <you@example.com>]: あなたの名前 <your@email.com>
# License []: MIT
# Compatible Python versions [^3.13]: ^3.13

# 必要なパッケージを対話式で追加
# Would you like to define your main dependencies interactively? (yes/no) [no] yes
# Package to add or search for (leave blank to continue): pandas
# Package to add or search for (leave blank to continue): numpy
# Package to add or search for (leave blank to continue): matplotlib
# Package to add or search for (leave blank to continue): seaborn
# Package to add or search for (leave blank to continue): 

# 開発用パッケージの追加
# Would you like to define your development dependencies interactively? (yes/no) [no] yes
# Package to add or search for (leave blank to continue): jupyter
# Package to add or search for (leave blank to continue): pytest
# Package to add or search for (leave blank to continue): black
# Package to add or search for (leave blank to continue): 

# Gitリポジトリ初期化
git init
```

### 初期ファイル構成
```bash
# プロジェクト構造作成
mkdir -p src/ec_sales_analysis
mkdir -p data/raw data/processed
mkdir -p notebooks
mkdir -p tests
mkdir -p docs

# 初期ファイル作成
touch src/ec_sales_analysis/__init__.py
touch src/ec_sales_analysis/data_loader.py
touch src/ec_sales_analysis/analyzer.py
touch src/ec_sales_analysis/visualizer.py
touch tests/test_data_loader.py
touch notebooks/exploratory_analysis.ipynb
```

---

## 📊 Step 2: サンプルデータ作成機能

### データ生成機能の実装
```bash
# ブランチを作成して機能開発
git checkout -b feature/data-generation

# データ生成スクリプト作成
cat > src/ec_sales_analysis/data_generator.py << 'EOF'
"""
サンプルデータ生成モジュール
"""
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_sales_data(n_records=1000, start_date='2023-01-01'):
    """
    ECサイトの売上サンプルデータを生成
    """
    np.random.seed(42)
    
    # 日付範囲生成
    start = datetime.strptime(start_date, '%Y-%m-%d')
    dates = [start + timedelta(days=x) for x in range(365)]
    
    # カテゴリマスタ
    categories = ['Electronics', 'Clothing', 'Books', 'Home', 'Sports']
    regions = ['Tokyo', 'Osaka', 'Nagoya', 'Fukuoka', 'Sapporo']
    
    # サンプルデータ生成
    data = []
    for i in range(n_records):
        record = {
            'order_id': f'ORD{i+1:06d}',
            'date': np.random.choice(dates),
            'category': np.random.choice(categories),
            'region': np.random.choice(regions),
            'amount': np.random.lognormal(mean=6, sigma=1),
            'quantity': np.random.poisson(lam=2) + 1,
            'customer_age': np.random.randint(18, 70),
            'is_member': np.random.choice([True, False], p=[0.7, 0.3])
        }
        data.append(record)
    
    df = pd.DataFrame(data)
    df['revenue'] = df['amount'] * df['quantity']
    
    return df

def save_sample_data(output_path='data/raw/sales_data.csv'):
    """
    サンプルデータを生成してCSVファイルに保存
    """
    df = generate_sales_data()
    df.to_csv(output_path, index=False)
    print(f"サンプルデータを {output_path} に保存しました")
    print(f"データ形状: {df.shape}")
    return df

if __name__ == "__main__":
    save_sample_data()
EOF

# データ生成実行
poetry run python src/ec_sales_analysis/data_generator.py

# 生成されたデータの確認
ls -la data/raw/
head -5 data/raw/sales_data.csv
```

### コミットとマージ
```bash
# 変更をコミット
git add .
git commit -m "データ生成機能実装: ECサイト売上サンプルデータ作成"

# mainブランチにマージ
git checkout main
git merge feature/data-generation
git branch -d feature/data-generation
```

---

## 🔧 Step 3: データ処理パイプライン

### データ読み込み機能
```bash
# 新しいブランチで開発
git checkout -b feature/data-processing

# データ読み込みモジュール実装
cat > src/ec_sales_analysis/data_loader.py << 'EOF'
"""
データ読み込み・前処理モジュール
"""
import pandas as pd
import numpy as np

class DataLoader:
    def __init__(self, data_path='data/raw/sales_data.csv'):
        self.data_path = data_path
        self.df = None
    
    def load_data(self):
        """CSVファイルからデータを読み込み"""
        try:
            self.df = pd.read_csv(self.data_path)
            self.df['date'] = pd.to_datetime(self.df['date'])
            print(f"データ読み込み完了: {self.df.shape}")
            return self.df
        except Exception as e:
            print(f"データ読み込みエラー: {e}")
            return None
    
    def validate_data(self):
        """データの基本的な検証"""
        if self.df is None:
            print("データが読み込まれていません")
            return False
        
        print("=== データ検証結果 ===")
        print(f"行数: {len(self.df)}")
        print(f"列数: {len(self.df.columns)}")
        print(f"欠損値: {self.df.isnull().sum().sum()}")
        print(f"期間: {self.df['date'].min()} - {self.df['date'].max()}")
        
        return True
    
    def clean_data(self):
        """データクリーニング"""
        if self.df is None:
            print("データが読み込まれていません")
            return None
        
        # 異常値の除去
        self.df = self.df[self.df['amount'] > 0]
        self.df = self.df[self.df['quantity'] > 0]
        
        # 月・曜日情報の追加
        self.df['month'] = self.df['date'].dt.month
        self.df['weekday'] = self.df['date'].dt.day_name()
        
        print("データクリーニング完了")
        return self.df
    
    def get_summary(self):
        """データサマリーの取得"""
        if self.df is None:
            return None
        
        summary = {
            'total_revenue': self.df['revenue'].sum(),
            'avg_order_value': self.df['revenue'].mean(),
            'total_orders': len(self.df),
            'categories': self.df['category'].nunique(),
            'regions': self.df['region'].nunique()
        }
        
        return summary
EOF

# テストファイル作成
cat > tests/test_data_loader.py << 'EOF'
"""
DataLoaderのテスト
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from ec_sales_analysis.data_loader import DataLoader

def test_data_loader():
    loader = DataLoader()
    df = loader.load_data()
    assert df is not None
    assert len(df) > 0
    
    # データ検証
    assert loader.validate_data() == True
    
    # データクリーニング
    cleaned_df = loader.clean_data()
    assert cleaned_df is not None
    
    # サマリー取得
    summary = loader.get_summary()
    assert summary is not None
    assert 'total_revenue' in summary

if __name__ == "__main__":
    test_data_loader()
    print("全テスト成功！")
EOF

# テスト実行
poetry run python tests/test_data_loader.py
```

---

## 📈 Step 4: 分析・可視化機能

### 分析機能の実装
```bash
# 分析モジュール実装
cat > src/ec_sales_analysis/analyzer.py << 'EOF'
"""
データ分析モジュール
"""
import pandas as pd
import numpy as np

class SalesAnalyzer:
    def __init__(self, df):
        self.df = df
    
    def monthly_trend(self):
        """月別売上トレンド分析"""
        monthly_sales = self.df.groupby('month').agg({
            'revenue': 'sum',
            'order_id': 'count'
        }).rename(columns={'order_id': 'order_count'})
        
        return monthly_sales
    
    def category_analysis(self):
        """カテゴリ別分析"""
        category_stats = self.df.groupby('category').agg({
            'revenue': 'sum',
            'amount': 'mean',
            'quantity': 'sum'
        }).round(2)
        
        return category_stats
    
    def customer_segmentation(self):
        """顧客セグメンテーション"""
        segments = self.df.groupby(['is_member', 'category']).agg({
            'revenue': 'mean',
            'order_id': 'count'
        }).rename(columns={'order_id': 'order_count'})
        
        return segments
    
    def regional_performance(self):
        """地域別パフォーマンス"""
        regional_stats = self.df.groupby('region').agg({
            'revenue': ['sum', 'mean'],
            'order_id': 'count'
        })
        
        regional_stats.columns = ['total_revenue', 'avg_revenue', 'order_count']
        return regional_stats.round(2)
EOF

# 可視化モジュール実装
cat > src/ec_sales_analysis/visualizer.py << 'EOF'
"""
データ可視化モジュール
"""
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# 日本語フォント設定
plt.rcParams['font.family'] = 'DejaVu Sans'

class SalesVisualizer:
    def __init__(self, df):
        self.df = df
        plt.style.use('seaborn-v0_8')
    
    def plot_monthly_trend(self, save_path=None):
        """月別トレンドの可視化"""
        monthly_data = self.df.groupby('month')['revenue'].sum()
        
        plt.figure(figsize=(12, 6))
        plt.plot(monthly_data.index, monthly_data.values, marker='o', linewidth=2)
        plt.title('Monthly Sales Trend', fontsize=16)
        plt.xlabel('Month', fontsize=12)
        plt.ylabel('Revenue', fontsize=12)
        plt.grid(True, alpha=0.3)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_category_comparison(self, save_path=None):
        """カテゴリ別比較"""
        category_data = self.df.groupby('category')['revenue'].sum().sort_values(ascending=False)
        
        plt.figure(figsize=(10, 6))
        bars = plt.bar(category_data.index, category_data.values)
        plt.title('Revenue by Category', fontsize=16)
        plt.xlabel('Category', fontsize=12)
        plt.ylabel('Revenue', fontsize=12)
        plt.xticks(rotation=45)
        
        # 値をバーの上に表示
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:,.0f}', ha='center', va='bottom')
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
    
    def plot_correlation_heatmap(self, save_path=None):
        """相関行列のヒートマップ"""
        numeric_cols = ['amount', 'quantity', 'customer_age', 'revenue']
        corr_matrix = self.df[numeric_cols].corr()
        
        plt.figure(figsize=(8, 6))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0)
        plt.title('Correlation Matrix', fontsize=16)
        
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
EOF

# メインスクリプト作成
cat > run_analysis.py << 'EOF'
"""
メイン分析スクリプト
"""
from src.ec_sales_analysis.data_loader import DataLoader
from src.ec_sales_analysis.analyzer import SalesAnalyzer
from src.ec_sales_analysis.visualizer import SalesVisualizer

def main():
    print("=== ECサイト売上データ分析 ===")
    
    # データ読み込み
    loader = DataLoader()
    df = loader.load_data()
    loader.validate_data()
    df = loader.clean_data()
    
    # 基本統計
    summary = loader.get_summary()
    print("\n=== 基本統計 ===")
    for key, value in summary.items():
        print(f"{key}: {value:,.2f}" if isinstance(value, float) else f"{key}: {value}")
    
    # 分析実行
    analyzer = SalesAnalyzer(df)
    
    print("\n=== 月別トレンド ===")
    monthly_trend = analyzer.monthly_trend()
    print(monthly_trend)
    
    print("\n=== カテゴリ別分析 ===")
    category_analysis = analyzer.category_analysis()
    print(category_analysis)
    
    # 可視化
    visualizer = SalesVisualizer(df)
    visualizer.plot_monthly_trend()
    visualizer.plot_category_comparison()
    visualizer.plot_correlation_heatmap()
    
    print("\n分析完了！")

if __name__ == "__main__":
    main()
EOF

# 分析実行
poetry run python run_analysis.py
```

---

## 🎯 Step 5: 最終統合とドキュメント

### プロジェクトの最終化
```bash
# .gitignore作成
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebook
.ipynb_checkpoints

# Poetry
poetry.lock

# データファイル（生成されるため除外）
data/processed/
*.png
*.jpg

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db
EOF

# README作成
cat > README.md << 'EOF'
# ECサイト売上データ分析プロジェクト

## プロジェクト概要
小売業ECサイトの売上データを分析し、季節性トレンドと顧客セグメンテーションを行うプロジェクトです。

## 環境構築

### 必要なツール
- Python 3.8+
- Poetry
- Git

### セットアップ
```bash
# リポジトリクローン
git clone <repository-url>
cd ec-sales-analysis

# 依存関係インストール
poetry install

# サンプルデータ生成
poetry run python src/ec_sales_analysis/data_generator.py
```

## 使用方法

### 分析実行
```bash
# メイン分析の実行
poetry run python run_analysis.py
```

### テスト実行
```bash
# テストの実行
poetry run python tests/test_data_loader.py
```

## プロジェクト構成
```
ec-sales-analysis/
├── src/
│   └── ec_sales_analysis/
│       ├── data_generator.py    # サンプルデータ生成
│       ├── data_loader.py       # データ読み込み・前処理
│       ├── analyzer.py          # データ分析
│       └── visualizer.py        # データ可視化
├── tests/                       # テストファイル
├── data/
│   └── raw/                     # 生データ
├── notebooks/                   # Jupyter notebooks
├── docs/                        # ドキュメント
└── run_analysis.py              # メインスクリプト
```

## 分析結果
- 月別売上トレンド
- カテゴリ別パフォーマンス
- 顧客セグメンテーション
- 地域別分析

## 開発者向け情報

### 新機能追加
```bash
git checkout -b feature/new-feature
# 開発...
git commit -m "新機能: 説明"
git checkout main
git merge feature/new-feature
```

### 依存関係管理
```bash
# パッケージ追加
poetry add package-name

# 開発用パッケージ追加
poetry add --group dev package-name
```
EOF

# 全ての変更をコミット
git add .
git commit -m "分析・可視化機能実装とプロジェクト最終化"

# 履歴確認
git log --oneline --graph
```

---

## ✅ 実習成果チェックリスト

### 技術スキル
- [ ] Poetry による依存関係管理
- [ ] Git による バージョン管理
- [ ] ブランチ戦略の実践
- [ ] モジュール化されたコード設計
- [ ] テスト駆動開発の基礎

### 実務スキル
- [ ] プロジェクト構造の設計
- [ ] ドキュメント作成
- [ ] コードレビュー可能な品質
- [ ] 再現性のある分析環境

### データ分析スキル
- [ ] データ生成・読み込み
- [ ] 前処理・クリーニング
- [ ] 探索的データ分析
- [ ] 可視化によるインサイト抽出

---

## 🚀 発展課題

### 1. 機能拡張
```bash
# 新しい分析機能を追加
git checkout -b feature/advanced-analytics
# - 時系列分析
# - 異常値検出
# - 予測モデル
```

### 2. テスト充実
```bash
# より包括的なテストを追加
git checkout -b feature/comprehensive-tests
# - ユニットテスト拡張
# - 統合テスト追加
# - テストカバレッジ測定
```

### 3. 自動化
```bash
# CI/CD パイプライン追加
# - GitHub Actions設定
# - 自動テスト実行
# - コードフォーマット確認
```

---

## 🎓 まとめ

### 習得したスキル
1. **現代的な開発環境**: Poetry + Git の連携
2. **プロジェクト管理**: 構造化、文書化、テスト
3. **データ分析パイプライン**: 読み込み → 分析 → 可視化
4. **協調開発**: ブランチ戦略、コードレビュー対応

### 実務での活用
- 新しいデータ分析プロジェクトの標準テンプレート
- チーム開発での環境統一
- 品質保証とドキュメント整備
- 継続的な機能拡張

おめでとうございます！PoetryとGitを活用した本格的なデータ分析プロジェクトを完成させました。
この経験を活かして、実際の業務でも効率的で品質の高い開発を行ってください！
EOF

# 全ての変更をコミット
git add .
git commit -m "分析・可視化機能実装とプロジェクト最終化"

# 履歴確認
git log --oneline --graph
```

---

## ✅ 実習成果チェックリスト

### 技術スキル
- [ ] Poetry による依存関係管理
- [ ] Git による バージョン管理
- [ ] ブランチ戦略の実践
- [ ] モジュール化されたコード設計
- [ ] テスト駆動開発の基礎

### 実務スキル
- [ ] プロジェクト構造の設計
- [ ] ドキュメント作成
- [ ] コードレビュー可能な品質
- [ ] 再現性のある分析環境

### データ分析スキル
- [ ] データ生成・読み込み
- [ ] 前処理・クリーニング
- [ ] 探索的データ分析
- [ ] 可視化によるインサイト抽出

---

## 🚀 発展課題

### 1. 機能拡張
```bash
# 新しい分析機能を追加
git checkout -b feature/advanced-analytics
# - 時系列分析
# - 異常値検出
# - 予測モデル
```

### 2. テスト充実
```bash
# より包括的なテストを追加
git checkout -b feature/comprehensive-tests
# - ユニットテスト拡張
# - 統合テスト追加
# - テストカバレッジ測定
```

### 3. 自動化
```bash
# CI/CD パイプライン追加
# - GitHub Actions設定
# - 自動テスト実行
# - コードフォーマット確認
```

---

## 🎓 まとめ

### 習得したスキル
1. **現代的な開発環境**: Poetry + Git の連携
2. **プロジェクト管理**: 構造化、文書化、テスト
3. **データ分析パイプライン**: 読み込み → 分析 → 可視化
4. **協調開発**: ブランチ戦略、コードレビュー対応

### 実務での活用
- 新しいデータ分析プロジェクトの標準テンプレート
- チーム開発での環境統一
- 品質保証とドキュメント整備
- 継続的な機能拡張

おめでとうございます！PoetryとGitを活用した本格的なデータ分析プロジェクトを完成させました。
この経験を活かして、実際の業務でも効率的で品質の高い開発を行ってください！