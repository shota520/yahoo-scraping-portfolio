# Yahooニュース スクレイピングツール

## 概要

Yahooニュースのトップページから最新の注目記事タイトルを10件取得し、CSVファイルとして保存します。

## 🚀 特徴 / Features

- requestsとBeautifulSoupによるHTML解析
- 上位10件の見出しを抽出
- `output/` フォルダに日付付きでCSV保存
- 仮想環境・依存管理対応（requirements.txt）

## 必要環境

- Python 3.10 以上

## セットアップ手順

1. 仮想環境の作成（任意）

python -m venv venv
.\venv\Scripts\activate

2. 必要ライブラリのインストール
pip install -r requirements.txt

3. スクリプトの実行
python yahoo_scraper.py

💡 応用アイデア / Future Possibilities
・LINEやSlack通知Botとの連携
・毎日定時で実行し、データ収集を自動化
・複数ニュースサイトを一括取得する汎用スクレイパー化
