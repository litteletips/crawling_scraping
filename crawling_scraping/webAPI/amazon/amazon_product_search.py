# AmazonのProduct Advertising APIを使って商品情報を取得する
# 取得した商品情報の利用目的はAmazonのサイトにエンドユーザーを誘導し商品の販売を促進することに限定されている
# APIの利用にはAmazonアソシエイト・プログラムへの登録が必要。一定期間売上が発生しないと利用できなくなる場合があるので注意

# 実行方法
# forego run python amazon_product_search.py
# 上記のように実行するとforegoがカレントディレクトリに存在する「.env」という名前のファイルから環境変数を読み取ってプログラムにわたす。
# これを実行すると次々とツイートが表示される。キャンセルするには「ctrl-C」

import os

from amazon.api import AmazonAPI  # pip install python-amazon-simple-product-api

# 環境変数から認証情報を取得する。
AMAZON_ACCESS_KEY = os.environ['AMAZON_ACCESS_KEY']
AMAZON_SECRET_KEY = os.environ['AMAZON_SECRET_KEY']
AMAZON_ASSOCIATE_TAG = os.environ['AMAZON_ASSOCIATE_TAG']

# AmazonAPIオブジェクトを作成する。キーワード引数Regionに'JP'を指定し、Amazon.co.jpを選択する。
amazon = AmazonAPI(AMAZON_ACCESS_KEY, AMAZON_SECRET_KEY, AMAZON_ASSOCIATE_TAG, Region='JP')

# search()メソッドでItemSearch操作を使い、商品情報を検索する。
# キーワード引数Keywordsで検索語句を、SearchIndexで検索対象とする商品のカテゴリを指定する。
# SearchIndex='All'はすべてのカテゴリから検索することを意味する。
products = amazon.search(Keywords='kindle', SearchIndex='All')

for product in products:  # 得られた商品（AmazonProductオブジェクト）について反復する。
    print(product.title)      # 商品名を表示。
    print(product.offer_url)  # 商品のURLを表示。
    price, currency = product.price_and_currency
    print(price, currency)    # 価格と通貨を表示。
