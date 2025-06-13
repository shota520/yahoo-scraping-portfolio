# Yahooニュース スクレイピングツール

## 概要

Yahooニュースのトップページから最新の注目記事タイトルを10件取得し、CSVファイルとして保存します。

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