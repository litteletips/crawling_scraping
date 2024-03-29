# matplotlibを用いたグラフによる可視化
# CSV/EXCELファイルから読み込んだデータをグラフとして描画
# matplotlibのサブプロットという、１つの図の中に複数のグラフを描画する昨日をt勝手、3つのグラフを立てに並べて比較
# 為替データ(https://www.stat-search.boj.or.jp/)
# 国債金利データ(https://www.mof.go.jp/jgbs/reference/interest_rate/index.htm)
# 有効求人倍率データ(https://www.mhlw.go.jp/toukei/list/114-1.html)
# の読み込み

# 日本政府や自治体が公開しているオープンデータがまとまっているサイト
# DATA GO JP (https://www.data.go.jp/)

# 実行方法
# python plot_historical_data.py

from datetime import datetime

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # 描画のバックエンドとしてデスクトップ環境が不要なAggを使う。
# 日本語を描画できるようMigMix 1Pフォントを指定する。
matplotlib.rcParams['font.sans-serif'] = 'MigMix 1P'
import matplotlib.pyplot as plt


def main():
    # 為替データの読み込み。
    df_exchange = pd.read_csv(
        'exchange.csv', encoding='cp932', header=1, names=['date', 'USD', 'rate'],
        index_col=0, parse_dates=True)
    # 国債金利データの読み込み。
    df_jgbcm = pd.read_csv(
        'jgbcm_all.csv', encoding='cp932', header=1, index_col=0, parse_dates=True,
        date_parser=parse_japanese_date, na_values=['-'])
    # 有効求人倍率データの読み込み。
    df_jobs = pd.read_excel('第3表.xls', skiprows=3, skipfooter=3, usecols='W,Y:AJ', index_col=0)
    # pandas 0.24以降では列ラベルに.1のような接尾辞がつくので、接尾辞がある場合は取り除く。
    df_jobs.columns = [c.split('.')[0] for c in df_jobs.columns]
    s_jobs = df_jobs.stack()
    s_jobs.index = [parse_year_and_month(y, m) for y, m in s_jobs.index]

    min_date = datetime(1973, 1, 1)  # X軸の最小値
    max_date = datetime.now()        # X軸の最大値

    # 1つ目のサブプロット（為替データ）
    plt.subplot(3, 1, 1)            # 3行1列の1番目のサブプロットを作成。
    plt.plot(df_exchange.index, df_exchange.USD, label='ドル・円')
    plt.xlim(min_date, max_date)    # X軸の範囲を設定。
    plt.ylim(50, 250)               # Y軸の範囲を設定。
    plt.legend(loc='best')          # 凡例を最適な位置に表示。
    # 2つ目のサブプロット（国債金利データ）
    plt.subplot(3, 1, 2)            # 3行1列の2番目のサブプロットを作成。
    plt.plot(df_jgbcm.index, df_jgbcm['1年'], label='1年国債金利')
    plt.plot(df_jgbcm.index, df_jgbcm['5年'], label='5年国債金利')
    plt.plot(df_jgbcm.index, df_jgbcm['10年'], label='10年国債金利')
    plt.xlim(min_date, max_date)    # X軸の範囲を設定。
    plt.legend(loc='best')          # 凡例を最適な位置に表示。
    # 3つ目のサブプロット（有効求人倍率データ）
    plt.subplot(3, 1, 3)            # 3行1列の3番目のサブプロットを作成。
    plt.plot(s_jobs.index, s_jobs, label='有効求人倍率（季節調整値）')
    plt.xlim(min_date, max_date)    # X軸の範囲を設定。
    plt.ylim(0.0, 2.0)              # Y軸の範囲を設定。
    plt.axhline(y=1, color='gray')  # y=1の水平線を引く。
    plt.legend(loc='best')          # 凡例を最適な位置に表示。

    plt.savefig('historical_data.png', dpi=300)  # 画像を保存。


def parse_japanese_date(s: str) -> datetime:
    """
    'H30.8.31' のような和暦の日付をdatetimeオブジェクトに変換する。
    """
    base_years = {'S': 1925, 'H': 1988, 'R': 2018}  # 昭和以降の元号の0年に相当する年を定義しておく。
    era = s[0]  # 元号を表すアルファベット1文字を取得。
    year, month, day = s[1:].split('.')  # 2文字目以降を .（ピリオド）で分割して年月日に分ける。
    year = base_years[era] + int(year)  # 元号の0年に相当する年と数値に変換した年を足して西暦の年を得る。
    return datetime(year, int(month), int(day))  # datetimeオブジェクトを作成する。


def parse_year_and_month(year: str, month: str) -> datetime:
    """
    ('X年', 'Y月') の組をdatetimeオブジェクトに変換する。
    """
    year = int(year[:-1])    # "年"を除去して数値に変換。
    month = int(month[:-1])  # "月"を除去して数値に変換。
    year += (1900 if year >= 63 else 2000)  # 63年以降は19xx年、63年より前は20xx年とみなす。
    return datetime(year, month, 1)  # datetimeオブジェクトを作成する。

if __name__ == '__main__':
    main()
