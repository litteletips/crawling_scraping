# crawling_scraping
scrapyを用いたcrawling/scrapingの為のツール

Project Organization
------------

    ├── LICENSE
    ├── Makefile                    <- コマンド実行用のファイル(Mac用) (例)`make data` `make train`
    ├── README.md         
    ├── .gitignore        
    │
    └── crawling_scraping
    |    ├── beautiful_soup         <- Beautiful Soup4を使ったスクレイピング.
    |    ├── bin               
    |    ├── cash_validate          <- pythonでHTTPキャッシュを扱う、jsonschemaはJSON Schemaでバリデーション、reを使って規表現でバリデーション.
    |    ├── crawler                <- Beautiful Soup4を使ったクローラーからMongoDBへ保存、lxmlを使ったクローラーかMongoDBへ保存.
    |    ├── csv_json_save          <- 様々なデータの扱い方整理、dict,join,csv,json.
    |    ├── error_handling         <- tenacityを用いたエラーハンドリング、requestsのエラーハンドリング.
    |    ├── flickere                <- flickerから人の画像を取得。画像解析して顔の部分だけ抽出。
    |    ├── include           
    |    ├── javascript_scraping    <- javascriptで作られたページのスクレイピング。
    |    ├── mecanicalsoup          <- mecanicalsoupを用いて、クックパットから最近調べたレシピを取ってくる。
    |    ├── open_data_extraction   <- openデータのCSVとかPDFから抽出する。
    |    ├── plot                   <- matplotlibで視覚化。
    |    ├── pyquery                <- PyqueryはjQueryと同じような使い方でHTMLからスクレイピングできる。
    |    ├── re_lxml                <- lxmlモジュールやreモジュールを使ったスクレイピング。
    |    ├── Requests               <- Requestsモジュールを用いたスクレイピング。
    |    ├── requests_lxml_csv      <- Requestsやlxmlで抜いたものをCSV形式で保存する。
    |    ├── requests_lxml_db       <- Requestsやlxmlで抜いたものをDBに保存する。
    |    ├── RSS_xml_scraping       <- RSSからクローリングする。
    |    ├── SQL_scraping           <- いろんなDBに保存する方法。(mongo,mysql,sqlite3)
    |    ├── tabeloghatebu          <- scrapyで食べログやハテブからスクレイピングする
    |    ├── webAPI                 <- いろんなAPIを用いてスクレイピングする。(Amazon,Twitter,youtube)
    |    ├── wikiextractor-master   <- wikiPediaからスクレイピングしてきて、Mecabで形態素解析する。
    |    └── yahoomap_bigquery      <- PARQLで美術館の情報を取得し、位置情報を持たない美術館については住所をジオコーディングし|位置情報を取得する。TwitterのStreamingAPIで取得したものをBigQueryにインポートする為のスクリプト。
    |
    └── django_scrapy              <- Djangoで作った画面上で、Scrapyを動かすためのモジュール
        ├── mariadb                <- mariadbを利用するための資材.
        |   ├── Dockerfile          <- 
        |   └── my.cnf             <- 
        ├── nginx                  <- nginxに関する資材.
        |   ├── Dockerfile          <- 
        |   ├── nginx.conf         <- 
        |   └── nginx.cnf          <- 
        ├── python3                <- scrapyに関するの資材.
        ├── docker-compose.yml     <- 
        ├── migrate.sh             <- 
        ├── resetdb.sh             <- 
        ├── start.sh               <- 
        └── Li                  <- 

--------


Scraping web site to save to DB in Docker

This sample uses [iHerb](https://www.iherb.com/) as target site.


--------

### Installation

  ```
  docker-compose up -d --build
  ```

### Run

  ```
  ./start.sh
  ```

### Access to DB by Django Admin

http://localhost/admin


Default user is
```
USERNAME: root
PASSWORD: initpass
```

### Access to DB

http://localhost/admin

### Configuration

Specify Environmental Valiable by docker-compose for Scrapy Configuration following

- SCRAPY_START_INDEX: 22419
- SCRAPY_NUM_ITEMS: 1000
- SCRAPY_CONCURRENT_ITEMS: 10000
- SCRAPY_CONCURRENT_REQUESTS: 2
- SCRAPY_DOWNLOAD_DELAY: 8.0
