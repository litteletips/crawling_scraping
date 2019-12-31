# Linked Open Dataからのデータ収集。
# データ同士をリンクさせ、容易に検索できる形で公開する為の方法論をLinked Dataと呼ぶ。

# Linked Dataにおけるデータ同士のリンクは、RDFというデータモデルで記述される。
# データを主語、述語、目的語の3組でモデル化。(日本(主語)、首都(述語)、東京(目的語))
# それぞれをURIで定義する。

# RDFのデータベースからデータを検索するために、SPARQLというクエリ言語が使える。
# クエリだけでなく、HTTPを使った通信の為のプロトコルも定義されており、SPARQLエンドポイントと呼ばれるサーバーにクエリを送信して、結果を取得できる。
# SPARQLによって、サーバーごとに異なるWebAPIの使い方を覚えることなく、統一されたインターフェイスでデータ取得できる。

# Wikipedia日本語版から情報を抽出して、Linked Open Dataとして提供するプロジェクト(DBpedia Japanese)
# DBpedia JapaneseからSPARQLで日本の美術館の情報を収集する。

# 実行方法
# python print_pdf_textboxes.py　000232384.pdf

from SPARQLWrapper import SPARQLWrapper  # pip install SPARQLWrapper

# SPARQLエンドポイントのURLを指定してインスタンスを作成する。
sparql = SPARQLWrapper('http://ja.dbpedia.org/sparql')
# 日本の美術館を取得するクエリを設定する。バックスラッシュを含むので、rで始まるraw文字列を使用している。
sparql.setQuery(r"""
SELECT * WHERE {
    ?s rdf:type dbpedia-owl:Museum ;
       prop-ja:所在地 ?address .
    FILTER REGEX(?address, "^\\p{Han}{2,3}[都道府県]")
} ORDER BY ?s
""")
sparql.setReturnFormat('json')  # 取得するフォーマットとしてJSONを指定する。
# query()でクエリを実行し、convert()でレスポンスをパースしてdictを得る。
response = sparql.query().convert()

for result in response['results']['bindings']:
    print(result['s']['value'], result['address']['value'])  # 抽出した変数の値を表示する。
