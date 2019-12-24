# Requests-OAuthlibを使ってTwitterのタイムラインを取得する
# OAuth 1.0aによる認証が必要なので、OAuth1Sessionクラスを使う
# OAuth1SessionクラスはRequestsのSessionを継承していて、コンストラクターにAPI Keyなど4つの値を指定してインスタンスを作成する
# インスタンス作成後は、認証を意識することなくRequestsのSessionオブジェクトと同じように扱える

# 認証情報は環境変数から取得する。 スクリプトの実行時に環境変数を渡すために、foregoというツールを使う。
# 'https://api.twitter.com/1.1/statuses/home_timeline.json'はユーザーのタイムラインを取得するもの

# 実行方法
# forego run python twitter_rest_api_with_requests.py
# 上記のように実行するとforegoがカレントディレクトリに存在する「.env」という名前のファイルから環境変数を読み取ってプログラムにわたす。

import os

from requests_oauthlib import OAuth1Session

# 環境変数から認証情報を取得する。
TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET_KEY = os.environ['TWITTER_API_SECRET_KEY']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

# 認証情報を使ってOAuth1Sessionオブジェクトを得る。
twitter = OAuth1Session(TWITTER_API_KEY,
                        client_secret=TWITTER_API_SECRET_KEY,
                        resource_owner_key=TWITTER_ACCESS_TOKEN,
                        resource_owner_secret=TWITTER_ACCESS_TOKEN_SECRET)

# ユーザーのタイムラインを取得する。
response = twitter.get('https://api.twitter.com/1.1/statuses/home_timeline.json')

# APIのレスポンスはJSON形式の文字列なので、response.json()でパースしてlistを取得できる。
# statusはツイート（Twitter APIではStatusと呼ばれる）を表すdict。
for status in response.json():
    print('@' + status['user']['screen_name'], status['text'])  # ユーザー名とツイートを表示する。
