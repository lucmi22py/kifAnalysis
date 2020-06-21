from pyautogui import locateCenterOnScreen, typewrite, hotkey, click, moveTo
from pyscreeze import ImageNotFoundException
import glob
import kfkfilemove
import subprocess
from selenium import webdriver
import chromedriver_binary
import bs4
import requests
import pyperclip
from time import sleep
import shutil


# 棋譜を開く
def openkif():
    moveTo(1224, 26)
    click(1224, 26)
    sleep(1)
    moveTo(45, 50)
    click(45, 50)
    moveTo(45, 107)
    click(45, 107)
    sleep(1)
    moveTo(483, 241)
    sleep(1)
    click(483, 241)
    moveTo(728, 749)
    sleep(1)
    click(728, 749)
    sleep(2)


# 棋譜解析を行う
def anakif():
    moveTo(1224, 26)
    click(1224, 26)
    sleep(3)
    moveTo(317, 47)
    click(317, 47)
    moveTo(317, 234)
    click(317, 234)
    sleep(1)
    moveTo(755, 897)
    click(755, 897)


# 棋譜解析終了判定
def finana():
    while True:
        try:
            d = locateCenterOnScreen('OK.png', grayscale=True)
            if not d ==None:
                x, y = locateCenterOnScreen('OK.png', grayscale=True)
                moveTo(x, y)
                click(x, y)
                break
        except ImageNotFoundException:
            sleep(10)


# 解析済みファイル保存(.kif)
def savekif():
    moveTo(1224, 26)
    click(1224, 26)
    moveTo(45, 50, duration=0.01)
    click(45, 50)
    sleep(1)
    moveTo(62, 184, duration=0.01)
    click(62, 184)
    sleep(1)
    moveTo(810, 642, duration=0.01)
    click(810, 644)
    sleep(1)
    hotkey('fn', 'end')
    typewrite(['backspace', 'backspace', 'backspace', 'backspace', '_', 'a', 'n', 'a'], 0.04)
    moveTo(735, 748, duration=0.01)
    click(735, 748)
    sleep(5)


# 将棋ウォーズ棋譜検索から一番上の棋譜をダウンロード
def dl_kif_top():
    # google chromeで将棋ウォーズ棋譜検索を開く
    browser = webdriver.Chrome()
    browser.get('http://tk2-221-20341.vs.sakura.ne.jp/shogi/?per=50&query=luc22')

    sleep(10)  # 10秒待ち(chromeが開いてからでないと以降のコードが受け付られない)

    # 一番上の棋譜の詳細ページへ飛ぶ
    elem = browser.find_element_by_css_selector("tr:nth-child(1) > td:nth-child(4) > div > div > div.dropdown-trigger > button.button.arrow_icon.is-small")
    elem.click()
    elem = browser.find_element_by_css_selector("div.is-paddingless.has-link > a")
    elem.click()

    '''
    # 詳細ページのURLを取得
    cur_url = browser.current_url
    print(cur_url)

    # bs4でKIFデータをテキストでコピー
    r = requests.get(cur_url)
    soup = bs4.BeautifulSoup(r.text, "html.parser")
    web_text = soup.select('pre.pre-wrap')
    dl_text = ''.join(str(web_text))
    pyperclip.copy(dl_text)
    '''

    # kifコピー
    hotkey('ctrl', 'a')
    sleep(2)
    hotkey('ctrl', 'c')

    # クリップボードのテキストを将棋所へ張り付け
    moveTo(970, 1044)  # shogiGUIを開く
    sleep(2)
    click(970, 1044)
    sleep(2)
    moveTo(1224, 26)  # shogiGUIのウィンドウを触る
    click(1224, 26)
    sleep(1)
    hotkey('ctrl', 'v')
    '''
    issue...Windowsアプリを直接呼ぶことができたら？
        アプリがすでに起動しているを真として判定
        -->True...既存ウインドウでアプリを呼ぶ
        -->false...新規ウインドウでアプリを呼ぶ
    '''
    '''
    if type(dl_text) is str:  # テキストデータなのか、kifファイルか否かでT/F判定
        moveTo(1224, 26)  # shogiGUIのウィンドウを触る
        click(1224, 26)
        sleep(1)
        hotkey('ctrl', 'v')
    else:
        print("kifファイルではありません")
    '''
    # ブラウザを閉じる
    browser.quit()
    print('ブラウザは閉じられました')


# 棋譜(kif)を先手と後手に分ける
def kif_classify():
    kif_list = glob.glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu2\\*.kif')
    loop_num = int(input())

    for num in range(loop_num):
        file = kif_list[num]

        with open(file) as f:
            lines = f.readlines()
            f.close()
            for i in range(8):
                line_i = lines[i]
                if "先手：luc22" in line_i:
                    if __name__ == '__main__':
                        kfkfilemove.move_glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\mykif_sente',
                                              file)
                    print('mykif_senteへ移動しました')
                    continue
                elif "後手：luc22" in line_i:
                    if __name__ == '__main__':
                        kfkfilemove.move_glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\mykif_gote',
                                              file)
                    print('mykif_goteへ移動しました')
                    continue
        print(str(int(num + 1)) + '局目:' + file)
    print('すべての処理が終了しました')


# ファイルを移動する
def move_glob(dst_path, pathname, recursive=True):    # dst_path = 保存先のpath, pathname = 保存元のpath
    for p in glob.glob(pathname, recursive=recursive):
        shutil.move(p, dst_path)


# 対象ファイル抽出
def file_rec():
    '''
    print('どんなデータを抽出しますか？\n'
          '1:対象年月を抽出\n'
          '2:対象を抽出\n'
          '3:hogehoge\n')
    '''
    #ent = 1
    #if ent == 1:
    print('pathを指定してください\n'
          '1:rawkifu2移動用path\n'
          '2:指定パスを入力\n')
    num_path = int(input())
    if num_path == 1:
        path = str(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu2')
        print("対象とする年月(yyyymm)をいれてください。ex)202003")
        file_name = str(r'\*') + str(input()) + str(r'*_*')
    elif num_path == 2:
        print('pathを入力してください\n')
        path = str(input())
        file_name = str(r'\*.kif')
    else:
        print('番号が違います。処理なし')
    now_path = path + file_name
    obj_list = glob.glob(now_path)
    return obj_list
