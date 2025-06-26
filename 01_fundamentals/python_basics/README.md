# Python基礎 - AIエンジニア研修

## 学習目標
- Pythonの基本文法を理解する
- データ構造（リスト、辞書、セット）を使いこなす
- 関数とクラスの基本概念を習得する
- ファイル操作とエラー処理を学ぶ

## 前提知識
- プログラミングの基礎概念
- コマンドラインの基本操作

## 学習時間
- 座学: 3時間
- 実習: 5時間
- 演習: 4時間

---

## 1. Python環境構築

### インストール確認
```bash
python --version
pip --version
```

### 仮想環境セットアップ
```bash
python -m venv python_basics_env
source python_basics_env/bin/activate  # Linux/Mac
pip install jupyter pandas numpy matplotlib
```

## 2. 学習コンテンツ

### 2.1 基本文法
- **理論**: [basic_syntax.md](./theory/basic_syntax.md)
- **実習**: [01_basic_syntax.ipynb](./notebooks/01_basic_syntax.ipynb)
- **演習**: [exercises/syntax_exercises.py](./exercises/syntax_exercises.py)

### 2.2 データ構造
- **理論**: [data_structures.md](./theory/data_structures.md)
- **実習**: [02_data_structures.ipynb](./notebooks/02_data_structures.ipynb)
- **演習**: [exercises/data_structure_exercises.py](./exercises/data_structure_exercises.py)

### 2.3 関数とモジュール
- **理論**: [functions_modules.md](./theory/functions_modules.md)
- **実習**: [03_functions_modules.ipynb](./notebooks/03_functions_modules.ipynb)
- **演習**: [exercises/function_exercises.py](./exercises/function_exercises.py)

### 2.4 オブジェクト指向
- **理論**: [object_oriented.md](./theory/object_oriented.md)
- **実習**: [04_object_oriented.ipynb](./notebooks/04_object_oriented.ipynb)
- **演習**: [exercises/oop_exercises.py](./exercises/oop_exercises.py)

### 2.5 ファイル操作とエラー処理
- **理論**: [file_error_handling.md](./theory/file_error_handling.md)
- **実習**: [05_file_error_handling.ipynb](./notebooks/05_file_error_handling.ipynb)
- **演習**: [exercises/file_error_exercises.py](./exercises/file_error_exercises.py)

## 3. 実践プロジェクト

### プロジェクト: データ分析準備ツール
**目標**: CSVファイルを読み込んで基本統計を計算するツールを作成

**要件**:
- ファイル読み込み機能
- データ検証機能
- 基本統計計算機能
- 結果出力機能
- エラーハンドリング

**成果物**: [project/data_analyzer.py](./project/data_analyzer.py)

## 4. 評価基準

### 理論テスト (40点)
- [ ] 変数とデータ型の理解 (10点)
- [ ] 制御構造の理解 (10点)
- [ ] 関数の理解 (10点)
- [ ] クラスの理解 (10点)

### 実習課題 (40点)
- [ ] 基本文法実習 (10点)
- [ ] データ構造実習 (10点)
- [ ] 関数実習 (10点)
- [ ] OOP実習 (10点)

### プロジェクト (20点)
- [ ] 機能実装 (10点)
- [ ] コード品質 (5点)
- [ ] 文書化 (5点)

## 5. 次のステップ

### 推奨学習順序
1. ✅ Python基礎 ← **現在地**
2. ⬜ 数学基礎
3. ⬜ データ処理

### 補強学習リソース
- [Python公式チュートリアル](https://docs.python.org/ja/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Automate the Boring Stuff](https://automatetheboringstuff.com/)

## 6. トラブルシューティング

### よくある質問
- **Q**: 環境構築でエラーが出る
- **A**: [troubleshooting.md](./troubleshooting.md)を参照

### サポート
- 技術的質問: [Issues](../../../../issues)
- 改善提案: [Pull Request](../../../../pulls)
- 緊急連絡: training@company.com

---

💡 **学習のコツ**: 
- 理論 → 実習 → 演習の順序で進める
- 分からない部分は遠慮なく質問する
- 実際にコードを書いて動かしてみる 