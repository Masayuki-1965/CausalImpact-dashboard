<!--
【役割】
本ファイルは、Causal Impact分析アプリのStreamlitダッシュボード画面構成・技術構成・画面イメージ・ファイル構成例をまとめたドキュメントです。
【参照先】
- docs/requirements_spec.md（要件定義書）
- docs/development_checklist.md（進捗管理・TODOリスト）
- docs/current_status.md（開発状況）
- docs/environment_notes.md（Python環境・ライブラリ構成）
-->
# Streamlitアプリケーション ダッシュボード構成

## 概要
本アプリケーションは、マーケティングや広告施策の効果測定に特化した分析手法「Causal Impact」を活用したデータ分析ダッシュボードです。ユーザーは3つのステップでデータ分析を進めることができます。

---

## 構成概要

### STEP 1：データ取り込み／可視化
- CSVファイルから処置群・対照群データをアップロード
- データのプレビュー表示（テーブル形式）
- 処置群・対照群を組み合わせたデータセットの作成
- 折れ線グラフ等による時系列データの可視化

### STEP 2：分析期間／パラメータの設定
- 介入前期間・介入期間の設定（カレンダーUI等）
- Causal Impactに渡すパラメータの設定（例：標準化有無、トレンド・季節性パラメータ等）
- 設定内容の確認表示

### STEP 3：分析実行／結果確認
- 分析実行ボタン
- 外部PythonスクリプトによるCausal Impact分析の実行
- 予測結果のグラフ表示（実測値・予測値・信頼区間等）
- 効果の概要（summary）の表示
- 分析結果のダウンロード機能（CSV, PNG等）

---

## 技術的構成
- STEP 1・STEP 2：Streamlit UI上で実装
- STEP 3：分析処理は外部Pythonスクリプトで実装し、Streamlitから呼び出し
- 分析結果はStreamlit側で可視化・表示

---

## 画面イメージ（例）
1. サイドバー：データアップロード、パラメータ設定、分析期間設定
2. メイン画面：
   - データプレビュー
   - 時系列グラフ
   - 分析結果グラフ
   - summaryテキスト
   - ダウンロードボタン

---

## ファイル構成（例）
- `app.py`（Streamlitアプリ本体）
- `analyze.py`（Causal Impact分析処理）
- `docs/streamlit_dashboard_structure.md`（本ドキュメント）
- `data/`（サンプルデータ格納用） 