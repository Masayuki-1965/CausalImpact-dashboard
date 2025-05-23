# Causal Impact分析アプリ リファクタリング計画

## 概要
- **目的**: app.py（1878行）の可読性・保守性・安全性向上
- **制約**: コア機能（データ処理・UI/UX・操作フロー）は絶対に変更しない
- **方針**: 外部ファイル化、定数化、モジュール化による整理

## リファクタリング対象

### 1. カスタムCSS（約250行）
**ファイル**: `styles/custom.css`
- 47行目～250行目の大量のCSS定義を外部ファイル化
- st.markdown()でCSSを読み込み

### 2. ヘルプ・ガイド文（約150行）
**ファイル**: `config/help_texts.py`
- データ形式ガイド、FAQ、説明文を定数化
- HTML含む長文テキストを外部化

### 3. 設定値・定数
**ファイル**: `config/constants.py`
- ファイルパス、デフォルト値、固定文言を定数化

### 4. 重複関数の統合
- app.py内の重複関数をutils_*.pyに移行
- load_and_clean_*系の関数整理

## 実行順序（安全性重視）

1. **Phase 1**: CSSの外部ファイル化
2. **Phase 2**: ヘルプ文の定数化  
3. **Phase 3**: 設定値の外部化
4. **Phase 4**: 重複関数の整理
5. **Phase 5**: 不要ファイルの削除

## 削除対象

### 確実に削除可能
- `__pycache__/` ディレクトリ（Pythonキャッシュ）
- `fonts/` ディレクトリ（空のフォルダ）
- `causal_impact_detail_*.csv`（サンプル出力ファイル）

### 検討対象
- `docs/delete_candidates.md`（リファクタリング後）
- `docs/refactoring_plan.md`（完了後）

## 注意事項
- 各Phase完了後は必ず動作確認
- セッション状態・データ処理ロジックは絶対に変更しない
- UI/UXの見た目・操作性を保持
- Streamlit Cloud デプロイに影響しない構成を維持 