# crawling_scraping
scrapyを用いたcrawling/scrapingの為のツール

Project Organization
------------

    ├── LICENSE
    ├── Makefile               <- コマンド実行用のファイル(Mac用) (例)`make data` `make train`
    ├── README.md         
    ├── .gitignore        
    │
    └── crawling_scraping
        ├── beautiful_soup    <- Beautiful Soup4を使ったスクレイピング.
        ├── bin               
        ├── cash_validate     <- pythonでHTTPキャッシュを扱う、jsonschemaはJSON Schemaでバリデーション、reを使って正規表現でバリデーション.
        ├── crawler           <- Beautiful Soup4を使ったクローラーからMongoDBへ保存、lxmlを使ったクローラーからMongoDBへ保存.
        ├── csv_json_save     <- 様々なデータの扱い方整理、dict,join,csv,json.
        ├── error_handling    <- tenacityを用いたエラーハンドリング、requestsのエラーハンドリング.
        └── raw            <- 元の不変のデータダンプ.


--------
