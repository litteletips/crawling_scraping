# 食べログをクロールしてレストラン情報を収集する

# 　　LstCosT=2：昼の予算の上限が2000円
# 　　RDoCosTp=1：ランチの営業時間帯

# 一覧ページから詳細ページをクロールするには、CrawlSpiderが便利。ページをたどる為の正規表現は以下。
# 詳細ページの数値の桁数はレストランによって異なる可能性もあるので、\d{3}のように具体的な桁数を指定するのではなく、\d+として桁数が変わっても対応できるようにする
# 　　一覧ページの2ページ目以降：/\w+/rstLst/lunch/\d/
# 　　詳細ページ：/\w+/A\d+/A\d+/\d+/$

# 実行方法
# scrapy crawl tablelog

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from myproject.items import Restaurant


class TabelogSpider(CrawlSpider):
    name = 'tabelog'
    # allowed_domains：ここで指定しているドメインのみ許可する。
    allowed_domains = ['tabelog.com']
    # start_urls：ここで指定してるURLが開始するページになる
    start_urls = [
        # 東京の昼のランキングのURL。
        # 普通にWebサイトを見ていると、多くのクエリパラメーターがついているが、
        # ページャーのリンクを見ると、値が0のクエリパラメーターは省略できることがわかる。
        'https://tabelog.com/tokyo/rstLst/lunch/?LstCosT=2&RdoCosTp=1',
    ]

    rules = [
        # ページャーをたどる（最大9ページまで）。
        # 正規表現の \d を \d+ に変えると10ページ目以降もたどれる。
        Rule(LinkExtractor(allow=r'/\w+/rstLst/lunch/\d/')),
        # レストランの詳細ページをパースする。
        Rule(LinkExtractor(allow=r'/\w+/A\d+/A\d+/\d+/$'), callback='parse_restaurant'),
    ]

    def parse_restaurant(self, response):
        """
        レストランの詳細ページをパースする。
        """
        # Google Static Mapsの画像のURLから緯度と経度を取得。
        latitude, longitude = response.css(
            'img.js-map-lazyload::attr("data-original")').re(r'markers=.*?%7C([\d.]+),([\d.]+)')

        # キーの値を指定してRestaurantオブジェクトを作成。
        item = Restaurant(
            name=response.css('.display-name').xpath('string()').get().strip(),
            address=response.css('.rstinfo-table__address').xpath('string()').get().strip(),
            latitude=latitude,
            longitude=longitude,
            station=response.css('dt:contains("最寄り駅")+dd span::text').get(),
            score=response.css('[rel="v:rating"] span::text').get(),
        )

        yield item
