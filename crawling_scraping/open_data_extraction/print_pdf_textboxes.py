# PDFMiner.sixでPDFをパースし、テキストボックスを表示する。
# レイアウトはLTPageというPDFのページに対応するオブジェクトをルートとした木構造で表現されている。
# テキストボックス(LTTextBox)は、1行のテキストを表すテキストライン(LTTextLine)をグループ化したオブジェクト。

# 実行方法
# python print_pdf_textboxes.py　000232384.pdf

import sys
from typing import List

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTContainer, LTTextBox, LTComponent
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage


def main():
    """
    メインとなる処理。コマンドライン引数で指定したPDFファイルから、テキストボックスを抽出して中身を表示する。
    """
    laparams = LAParams(detect_vertical=True)  # Layout Analysisの設定で縦書きの検出を有効にする。
    resource_manager = PDFResourceManager()  # 共有のリソースを管理するリソースマネージャーを作成。
    # ページを集めるPageAggregatorオブジェクトを作成。
    device = PDFPageAggregator(resource_manager, laparams=laparams)
    interpreter = PDFPageInterpreter(resource_manager, device)  # Interpreterオブジェクトを作成。

    with open(sys.argv[1], 'rb') as f:  # ファイルをバイナリ形式で開く。
        # PDFPage.get_pages()にファイルオブジェクトを指定して、PDFPageオブジェクトを順に取得する。
        # 時間がかかるファイルは、キーワード引数pagenosで処理するページ番号（0始まり）のリストを指定するとよい。
        for page in PDFPage.get_pages(f):
            interpreter.process_page(page)  # ページを処理する。
            layout = device.get_result()  # LTPageオブジェクトを取得。

            boxes = find_textboxes_recursively(layout)  # ページ内のテキストボックスのリストを取得する。
            # テキストボックスの左上の座標の順でテキストボックスをソートする。
            # y1（Y座標の値）は上に行くほど大きくなるので、正負を反転させている。
            boxes.sort(key=lambda b: (-b.y1, b.x0))

            for box in boxes:
                print('-' * 10)  # 読みやすいよう区切り線を表示する。
                print(box.get_text().strip())  # テキストボックス内のテキストを表示する。


def find_textboxes_recursively(component: LTComponent) -> List[LTTextBox]:
    """
    再帰的にテキストボックス（LTTextBox）を探して、テキストボックスのリストを取得する。
    """
    # LTTextBoxを継承するオブジェクトの場合は1要素のリストを返す。
    if isinstance(component, LTTextBox):
        return [component]

    # LTContainerを継承するオブジェクトは子要素を含むので、再帰的に探す。
    if isinstance(component, LTContainer):
        boxes = []
        for child in component:
            boxes.extend(find_textboxes_recursively(child))

        return boxes

    return []  # その他の場合は空リストを返す。

if __name__ == '__main__':
    main()
