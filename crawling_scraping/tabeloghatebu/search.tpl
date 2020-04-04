<!-- ページ上部に検索窓、その下に検索結果を表示するだけの簡単なWebページ -->
<!-- {{変数名}}は変数がバインディングされる。<% %>はPythonコードとして実行される -->

<!DOCTYPE HTML>
<html>
<head>
    <meta charset="utf-8">
    <title>Elasticsearchによる全文検索</title>
    <style>
    input { font-size: 120%; }
    h3 { font-weight: normal; margin-bottom: 0; }
    em { font-weight: bold; font-style: normal; }
    .link { color: green; }
    .fragment { font-size: 90%; }
    </style>
</head>
<body>
    <!-- 検索フォーム -->
    <form>
        <input type="text" name="q" value="{{ query }}">
        <input type="submit" value="検索する">
    </form>

    <!-- 検索結果 -->
    <% for page in pages: %>
    <div>
        <h3><a href="{{ page["_source"]["url"] }}">{{ page["_source"]["title"] }}</a></h3>
        <div class="link">{{ page["_source"]["url"] }}</div>
        <div class="fragment">{{! page["highlight"]["content"][0] }}</div>
    </div>
    <% end %>
</body>
</html>
