# -*- coding: utf-8 -*-
from selenium import webdriver
import chromedriver_binary
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import pyperclip
import re
import os
import glob
import pathlib

import kif_handle
import kfkfilemove
import kfkfiling
import Game_per_Day


class DLKifClass:
    url = r'https://www.shogi-extend.com/?per=50&query='

    def __init__(self, user_name):
        self.name = user_name
        self.dl_url = r'https://www.shogi-extend.com/w?per=50&query=' + self.name

    def dl_kif(self):
        # 棋譜数カウント
        '''
        gpd = None
        if gpd is None:
            print('取り込む棋譜の数を入力してください')
            loop_num = int(input())  # 取り込む棋譜の数
        else:
            loop_num = gpd
        '''

        # google chromeで将棋ウォーズ棋譜検索を開く
        browser = webdriver.Chrome()
        browser.get(r'https://www.shogi-extend.com/w?per=50&query=anreichan')
        sleep(5)  # 5秒待ち(chromeが開いてからでないと以降のコードが受け付られない)

        loop_num = int(50)
        for num in range(1, loop_num + 1):
            # コピーから取得する方法
            elem_copy = browser.find_element_by_xpath(
                '//tr[' + str(int(num)) + ']/td[4]/div/button[1]'
            )
            elem_copy.click()
            sleep(2.5)

            # ファイル名整形
            pre_paste = pyperclip.paste()
            sp = pre_paste.split('\r\n')
            pre_sp1 = sp[0].split(' ')
            prep_sp1 = pre_sp1[0]
            sp1 = re.sub(r'先手：', '', prep_sp1)
            pre_sp2 = sp[1].split(' ')
            prep_sp2 = pre_sp2[0]
            sp2 = re.sub(r'後手：', '', prep_sp2)
            pre_sp3 = re.sub(r'開始日時：|/|:', '', sp[2])
            sp3 = re.sub(r' ', '_', pre_sp3)
            title_kif = str(sp1 + '-' + sp2 + '-' + sp3 + '.kif')

            # ファイル保存
            new_kif_file = os.path.abspath(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\studykif\\')
            file_kif = open(new_kif_file + title_kif, 'w')
            file_kif.write(pre_paste)
            file_kif.close()
            print("ファイル作成完了。title: " + title_kif)
        print("すべての処理は終了しました")
        browser.quit()

    def kifana(self, src_path, dest_path, loop_num):
        # 対象ファイルコピー
        for num in range(1, loop_num + 1):
            if __name__ == '__main__':
                kif_handle.openkif()

            if __name__ == '__main__':
                kif_handle.anakif()

            if __name__ == '__main__':
                kif_handle.finana()

            if __name__ == '__main__':
                kif_handle.savekif()

            # 同名kifファイル移動
            path = 'C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu'
            analyzed_kif = glob.glob(os.path.join(path, '*_ana.*'))  # 対象1
            try:
                A1_list_str = analyzed_kif[0]
            except IndexError:
                print('*_anaファイルは存在しません。bklogにエラーを保存しました。')
            B = pathlib.Path(A1_list_str)
            Target1_deana = B.stem.rstrip("_ana")
            A2 = glob.glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu\\*.kif')  # 対象2
            for A2_element in A2:
                if Target1_deana in A2_element:
                    if __name__ == '__main__':
                        kfkfilemove.move_glob(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu2',
                                              A2_element)
                    break

            # kfkfilingによるkfk化は最後にすること
            # pyファイルのあるディレクトリへ対象ファイルを移動させるため
            # *_ana.kifファイルのkfk化
            f = glob.glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu\\*_ana.kif')
            try:
                f1 = f[0]
                if __name__ == '__main__':
                    kfkfiling.change_suffix(f1, '.kif', '.kfk')
                else:
                    print("file is not exist")
            except IndexError:
                print("*_ana.kifファイルは存在しません")
            except NameError:
                print("*_ana.kifファイルが見つからないので、f1は存在しません")

            # kfkファイル移動
            try:
                if __name__ == '__main__':
                    kfkfilemove.move_glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\analysis',
                                          'C:\\Users\\Ryota Okunishi\\pycharm_projects\\kifAnalysis\\*_ana.kfk')
            except IndexError:
                print("kfkファイルは存在しません")

            print('棋譜解析完了しました。:' + str(int(num)) + '局目')


dl = DLKifClass('luc22')
print(dl.dl_url)
dl.kifana(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\python_kif\anreichan(yodan)',
              r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\python_anakif\anreichan(yodan)_ana',
          50)
