# -*- coding: utf-8 -*-
from pyautogui import locateCenterOnScreen, typewrite, hotkey, click, moveTo
from selenium import webdriver
import chromedriver_binary
import bs4
import requests
import pyperclip
from time import sleep

# google chromeで将棋ウォーズ棋譜検索を開く
browser = webdriver.Chrome()
browser.get('http://tk2-221-20341.vs.sakura.ne.jp/shogi/?per=50&query=luc22')

sleep(10) # 10秒待ち(chromeが開いてからでないと以降のコードが受け付られない)

# 一番上の棋譜の詳細ページへ飛ぶ
num = 2
elem_xpath = browser.find_element_by_xpath('//tr['+ str(int(num)) + ']/td/div/div/div[1]/button[@class="button arrow_icon is-small"]')
elem_xpath.click()
sleep(2)
elem2_xpath = browser.find_element_by_xpath('//tr['+ str(int(num)) + ']/td/div/div/div[3]/div/div[@class="is-paddingless has-link"]')
elem2_xpath.click()
elem3 = browser.find_element_by_xpath('//pre').text

'''
//tr[1]/td/div/div/div[1]/button[@class="button arrow_icon is-small"] -->正しいxpath

css セレクタを使う場合
elem = browser.find_element_by_css_selector("tr:nth-child(1) > td > div > div > div.dropdown-trigger > button.button.arrow_icon.is-small") # cssselector = 'tr:nth-child(i) > td > div > div > div.dropdown-trigger > button.button.arrow_icon.is-small' 時々チェックすること! 2020/02/10まで
elem2 = browser.find_element_by_css_selector("tr:nth-of-type(1) td > div> div> div> div> div.is-paddingless.has-link")


'''

# 詳細ページのURLを取得
cur_url = browser.current_url
sp = cur_url.split('/')
print(sp)
print(type(sp))
print(sp[-1])
print(type(sp[-1]))
print(cur_url)
print('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu\\' + sp[-1])

# kifファイルの作成
file_1 = open('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu\\' + sp[-1], 'w')
file_1.write(elem3)
file_1.close()
print('処理終了')

# ブラウザの終了
browser.quit()
print("ブラウザは閉じられました")
'''
# bs4でKIFデータをテキストでコピー
r = requests.get(cur_url)
soup = bs4.BeautifulSoup(r.text, "html.parser")
web_text = soup.select('pre.pre-wrap')
dl_text = ''.join(str(web_text))
pyperclip.copy(dl_text)

# クリップボードのテキストを将棋所へ張り付け
moveTo(970, 1044) #shogiGUIを開く
sleep(2)
click(970, 1044)
sleep(2)
'''
'''
issue...Windowsアプリを直接呼ぶことができたら？
    アプリがすでに起動しているを真として判定
    -->True...既存ウインドウでアプリを呼ぶ
    -->false...新規ウインドウでアプリを呼ぶ
'''
'''
if type(dl_text) is str: # テキストデータなのか、kifファイルか否かでT/F判定
    moveTo(1224, 26) #shogiGUIのウィンドウを触る
    click(1224, 26)
    sleep(1)
    hotkey('ctrl', 'v')
else:
    print("kifファイルではありません")
'''