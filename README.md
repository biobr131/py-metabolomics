# py-metabolomics

メタボロミクス研究のためのPython環境のテンプレートです。
基本的な統計解析に加え，バイオインフォマティクス用のライブラリも含まれています。
また，質量分析計から得られる生データや関連ファイルの読み込みにも対応しています。


## 主な機能

## 使用方法

### セットアップ

#### Dockerを使用する場合

```
docker compose build
```

#### ローカル環境にPythonをインストールする場合

```
python -m venv .venv
.venv/Scripts/activate  # Windowsの場合
pip install --upgrade pip
pip install -r requirements.txt
```
