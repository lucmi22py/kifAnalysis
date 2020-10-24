# -*- coding: utf-8 -*-
# -*- 役割: chromewebdriverのダウンロード -*-

# -*- ライブラリ -*-
import os
import webbrowser
import pathlib
import shutil
import zipfile
import pprint

# -*- 処理部 -*-
def dl_webdriver():
    print("webdriverをダウンロードしますか？ [y/n]")
    alt = input()
    if alt == r'y':
        url = r"https://chromedriver.chromium.org/downloads"
        browser = webbrowser.get('"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %s')
        browser.open(url)

        dl_path = pathlib.Path(r'C:\Users\Ryota Okunishi\Downloads')
        dst_path = r'C:\Users\Ryota Okunishi\pycharm_projects\kifAnalysis\venv\Lib\site-packages'
        zip_path = r'C:\Users\Ryota Okunishi\Desktop\ローカル専用\chromedriver_zip'
        chromedriver_zip = str('**/chromedriver*.zip')
        dl_zip_path = dl_path.glob(chromedriver_zip)
        na = dl_zip_path

        zip_list = list([str(p) for p in dl_path.glob(chromedriver_zip)])
        for i in range(len(zip_list)):
            z_list = pathlib.Path(zip_list[i])
            prs_file = str(z_list.parent) + z_list.root + z_list.stem

            if os.path.isdir(prs_file) is False:
                os.mkdir(prs_file)
            with zipfile.ZipFile(zip_list[i]) as existing_zip:
                existing_zip.extractall(prs_file)
            shutil.move(zip_list[i], zip_path)

        chromedriver_list = list(dl_path.glob('**/chromedriver.exe'))
        if len(chromedriver_list) > 1:
            print('chromedriver.exeが複数あるようです。確認してください。')
            pprint.pprint(chromedriver_list)
            path_w = str(dl_path) + dl_path.root + str('errorlog.txt')
            with open(path_w, mode='w') as f:
                f.write('///chromedriver list///' + '\n')
                for i in range(len(chromedriver_list)):
                    f.write(str(chromedriver_list[i]) + '\n')

            print('最新のchromedriverを適用しますか？ [y/n]' )
            yn = input()
            if yn == r'y':
                #listの中で最新のものをsite-packagesに適用する
                for i in range(len(chromedriver_list)):
                    p_list = pathlib.Path(chromedriver_list[i])
                    p_list_stat = p_list.stat()
                    print(p_list_stat)
                p_list_stat = list(p_list_stat)
                pprint.pprint(p_list_stat)
                ""
        print('テスト終わり')
        print(dst_path)
        print('テスト終わり')
