# -*- coding: utf-8 -*-
from selenium import webdriver
import chromedriver_binary
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import pyperclip
import re
import os
import Game_per_Day

# 棋譜数カウント
gpd = Game_per_Day.game_per_day()
if gpd is None:
    print('取り込む棋譜の数を入力してください')
    loop_num = int(input())  # 取り込む棋譜の数
else:
    loop_num = gpd

# google chromeで将棋ウォーズ棋譜検索を開く
browser = webdriver.Chrome(executable_path=r'C:\Users\Ryota Okunishi\pycharm_projects\kifAnalysis\venv\Lib\site-packages\chromedriver_binary\chromedriver.exe')
browser.get('https://www.shogi-extend.com/w?per=50&query=luc22')
sleep(5)  # 5秒待ち(chromeが開いてからでないと以降のコードが受け付られない)

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
    sp3 = re.sub(r' ', '_',pre_sp3)
    title_kif = str(sp1 + '-' + sp2 + '-' + sp3 + '.kif')

    # ファイル保存
    new_kif_file = os.path.abspath(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu\\')
    file_kif = open(new_kif_file + title_kif, 'w')
    file_kif.write(pre_paste)
    file_kif.close()
    print("ファイル作成完了。title: " + title_kif)

    '''
    css セレクタを使う場合
    elem = browser.find_element_by_css_selector("tr:nth-child(1) > td > div > div > div.dropdown-trigger > button.button.arrow_icon.is-small") # cssselector = 'tr:nth-child(i) > td > div > div > div.dropdown-trigger > button.button.arrow_icon.is-small' 時々チェックすること! 2020/02/10まで
    elem2 = browser.find_element_by_css_selector("tr:nth-of-type(1) td > div> div> div> div> div.is-paddingless.has-link")
    
    〈issues〉
    例外処理…xpath変更差分が取れるようにする。
    '''
print("すべての処理は終了しました")
browser.quit()
