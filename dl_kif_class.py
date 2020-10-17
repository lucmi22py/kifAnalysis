# -*- coding: utf-8 -*-
from selenium import webdriver
import chromedriver_binary
from time import sleep
import pyperclip
import re
import os
import glob
import pathlib
import shutil

# from kif_handle import KifHandle as KH
import kif_handle
import kfkfiling


class DLKifClass:
    url = r'https://www.shogi-extend.com/?per=50&query='

    def __init__(self, user_name):
        self.name = user_name
        self.dl_url = r'https://www.shogi-extend.com/w?per=50&query=' + self.name

    def dl_kif(self, save_path):
        # google chromeで将棋ウォーズ棋譜検索を開く
        browser = webdriver.Chrome(executable_path=r'C:\Users\Ryota Okunishi\pycharm_projects\kifAnalysis\venv\Lib\site-packages\chromedriver_binary\chromedriver.exe')
        browser.get(self.dl_url)
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
            new_kif_file = os.path.abspath(save_path)
            file_kif = open(new_kif_file + title_kif, 'w')
            file_kif.write(pre_paste)
            file_kif.close()
            print("ファイル作成完了。title: " + title_kif)
        print("すべての処理は終了しました")
        browser.quit()

    @staticmethod
    def kifana(src_path, dst_path, loop_num):
        # 対象ファイルコピー
        if loop_num is None:
            print('ループ回数を入力してください\n')
            loop_num = int(input())
        for num in range(1, loop_num + 1):
            '''
            KH.open_kif()
            KH.ana_kif()
            KH.fin_ana()
            KH.save_kif()
            '''
            # '''
            kif_handle.openkif()
            kif_handle.anakif()
            kif_handle.finana()
            kif_handle.savekif()
            # '''

            # 同名kifファイル移動
            # 比較元ファイル(複数)
            t_src_path = os.path.join(src_path, '*.kif')
            compare_file = glob.glob(t_src_path)
            # 比較対象ファイル(1つ)
            tana_src_path = os.path.join(src_path, '*_ana.*')
            analyzed_kif = glob.glob(tana_src_path)[0]
            pathlib_analyzed_kif = pathlib.Path(analyzed_kif)
            analyzed_kif_prename = pathlib_analyzed_kif.stem.rstrip('_ana')
            for file_num in range(len(compare_file)):
                pathlib_compare_file = pathlib.Path(compare_file[file_num])
                if analyzed_kif_prename == pathlib_compare_file.stem:
                    shutil.move(compare_file[file_num], dst_path)
                    break

            # kfkfilingによるkfk化は最後にすること
            # pyファイルのあるディレクトリへ対象ファイルを移動させるため
            # *_ana.kifファイルのkfk化
            ana_dst_path = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\analysis'
            try:
                kfkfiling.change_suffix(analyzed_kif, ana_dst_path, '.kif', '.kfk')
            except IndexError:
                print("*_ana.kifファイルは存在しません")
            except NameError:
                print("*_ana.kifファイルが見つからないので、f1は存在しません")

            # kfkファイル移動
            kfk_file = glob.glob(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu\*_ana.kfk')
            try:
                shutil.move(kfk_file[0], ana_dst_path)
            except IndexError:
                print("kfkファイルは存在しません")
            except shutil.Error:
                kfk_file_name = pathlib.Path(kfk_file[0]).name
                resave_path = ana_dst_path + r'\\' + kfk_file_name
                shutil.move(kfk_file[0], resave_path)

            print('棋譜解析完了しました。:' + str(int(num)) + '局目')
