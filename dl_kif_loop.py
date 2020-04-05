# -*- coding: utf-8 -*-
from selenium import webdriver
import chromedriver_binary
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import pyperclip
import re
import os

print('取り込む棋譜の数を入力してください')
loop_num = int(input())  # 取り込む棋譜の数
for num in range(1, loop_num + 1):
    # google chromeで将棋ウォーズ棋譜検索を開く
    browser = webdriver.Chrome()
    browser.get('http://tk2-221-20341.vs.sakura.ne.jp/shogi/?per=50&query=luc22')

    sleep(5)  # 10秒待ち(chromeが開いてからでないと以降のコードが受け付られない)

    # コピーから取得する方法
    elem_copy = browser.find_element_by_xpath(
        '//tr[' + str(int(num)) + ']/td[4]/div/button[1]'
    )
    elem_copy.click()
    sleep(1.5)
    browser.quit()

    '''
    try:
        # 一番上の棋譜の詳細ページへ飛ぶ
        elem_xpath = browser.find_element_by_xpath(
            '//tr[' + str(int(num)) + ']/td/div/div/div/button')
        elem_xpath.click()
        sleep(2)
        elem2_xpath = browser.find_element_by_xpath(
            '//tr[' + str(int(num)) + ']/td[4]/div/div/div[3]/div/a[6]')
        elem2_xpath.click()
        elem3 = browser.find_element_by_xpath('//pre').text
    except NoSuchElementException:
        # コピーから取得する方法
        elem_copy = browser.find_element_by_xpath(
            '//tr[' + str(int(num)) + ']/td[4]/div/button[1]'
        )
        elem_copy.click()
        print('コピーOK')
        sleep(1.5)
        browser.quit()
    '''

    '''
    # 詳細ページのURLを取得
    name_xpath = browser.find_element_by_xpath(
        '/html/body/section/div/div/div[5]/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/div/div/div[3]/div/a[8]'
    )
    sp = name_xpath.split('/')
    '''
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
    xpathを使う場合
    //tr[1]/td/div/div/div[1]/button[@class="button arrow_icon is-small"] -->正しいxpath
    //*[@id="swars_battle_index"]/div[5]/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/div/div/div[3]/div/a[8]
    /html/body/section/div/div/div[5]/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/div/div/div[3]/div/a[8]

    //*[@id="swars_battle_index"]/div[5]/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/div/div/div[1]/button
    //*[@id="swars_battle_index"]/div[5]/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/div/div/div[3]/div/div[5]
    //*[@id="swars_battle_index"]/div[5]/div/div[2]/div[2]/table/tbody/tr[1]/td[4]/div/div/div[3]/div/div[6]

    css セレクタを使う場合
    elem = browser.find_element_by_css_selector("tr:nth-child(1) > td > div > div > div.dropdown-trigger > button.button.arrow_icon.is-small") # cssselector = 'tr:nth-child(i) > td > div > div > div.dropdown-trigger > button.button.arrow_icon.is-small' 時々チェックすること! 2020/02/10まで
    elem2 = browser.find_element_by_css_selector("tr:nth-of-type(1) td > div> div> div> div> div.is-paddingless.has-link")
    '''

'''
    # 詳細ページのURLを取得
    cur_url = browser.current_url
    sp = cur_url.split('/')

    # kifファイルの作成
    file_1 = open('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu\\' + sp[-1], 'w')
    file_1.write(elem3)
    file_1.close()
    print("ファイル作成完了。title: " + sp[-1])

    browser.quit()
'''
print("すべての処理は終了しました")
