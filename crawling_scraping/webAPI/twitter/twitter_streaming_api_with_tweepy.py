# TweepyによるTwitter Streaming API の利用
# Tweepyを使ってサーバーから次々にメッセージが送られてくる
# ツイートを受信したときに、MyStreamListnerクラスのon_status()メソッドが呼び出される

# 実行方法
# forego run python twitter_rest_api_with_tweepy.py
# 上記のように実行するとforegoがカレントディレクトリに存在する「.env」という名前のファイルから環境変数を読み取ってプログラムにわたす。
# これを実行すると次々とツイートが表示される。キャンセルするには「ctrl-C」

import os

import tweepy

# 環境変数から認証情報を取得する。
TWITTER_API_KEY = os.environ['TWITTER_API_KEY']
TWITTER_API_SECRET_KEY = os.environ['TWITTER_API_SECRET_KEY']
TWITTER_ACCESS_TOKEN = os.environ['TWITTER_ACCESS_TOKEN']
TWITTER_ACCESS_TOKEN_SECRET = os.environ['TWITTER_ACCESS_TOKEN_SECRET']


def main():
    """
    メインとなる処理
    """
    # OAuthHandlerオブジェクトを作成し、認証情報を設定する。
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)

    # OAuthHandlerとStreamListenerを指定してStreamオブジェクトを取得する。
    stream = tweepy.Stream(auth, MyStreamListener())
    # 公開されているツイートをサンプリングしたストリームを受信する。
    # キーワード引数languagesで、日本語のツイートのみに絞り込む。
    stream.sample(languages=['ja'])


class MyStreamListener(tweepy.StreamListener):
    """
    Streaming APIで取得したツイートを処理するためのクラス。
    """

    def on_status(self, status: tweepy.Status):
        """
        ツイートを受信したときに呼び出されるメソッド。引数はツイートを表すStatusオブジェクト。
        """
        print('@' + status.author.screen_name, status.text)

if __name__ == '__main__':
    main()
