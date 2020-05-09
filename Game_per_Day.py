from selenium import webdriver
import chromedriver_binary
import re
from time import sleep


def game_per_day():
    # 自分の棋譜検索ページを開く
    loop_num = 50  # 取り込む棋譜の数
    browser = webdriver.Chrome()
    browser.get('http://tk2-221-20341.vs.sakura.ne.jp/shogi/?per=50&query=luc22') # google chromeで将棋ウォーズ棋譜検索を開く
    sleep(5)  # 10秒待ち(chromeが開いてからでないと以降のコードが受け付られない)

    # 今日の日付の棋譜の数を数える
    for num in range(1, loop_num + 1):
        elem_xpath = browser.find_element_by_xpath('//tbody/tr[' + str(int(num)) + ']/td[3]').text
        m = re.fullmatch('\d{2}:\d{2}', elem_xpath)

        if re.fullmatch('\d{2}:\d{2}', elem_xpath) is None:
            max_loop_num = num
            break

    print('結果：//tr[' + str(int(max_loop_num)) + ']/td/div/div/div[3]/div/div[6]')
    print(str(int(max_loop_num)-1) + '局まで取得推奨')
    browser.quit()
    return int(max_loop_num)-1
    '''
    elem2_xpath = browser.find_element_by_xpath(
    '//tr[' + str(int(num)) + ']/td/div/div/div[3]/div/div[6]')
    elem2_xpath.click()
    elem3 = browser.find_element_by_xpath('//pre').text
    //*[@id="swars_battle_index"]/div[5]/div/div[2]/div[2]/table/tbody/tr[8]/td[4]/div/div/div[1]/button
    '''

    '''
    //*[@id="swars_battle_index"]/div[5]/div/div[2]/div[2]/table/tbody/tr[3]/td[3]/text()
    //*[@id="swars_battle_index"]/div[5]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]
    /html/body/section/div/div/div[5]/div/div[2]/div[2]/table/tbody/tr[1]/td[3]
    '''

    # 棋譜数を変数gpdに入れる
    # print(gpd)
