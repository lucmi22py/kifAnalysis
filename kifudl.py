import re
import json

# kfkファイルを読み込む
#kfk_file = open("C:\\Users\\Ryota Okunishi\\Downloads\\piyo_20190210_151615.kfk")
#list = kfk_file.readlines()

# ヘッダーの削除
#del(list[0:9])
#print(list)

# 一行読み込んで判定する
# '評価値 xx' の文字列があった場合、数字部分を抽出してcsvシートに記録
with open('C:\\Users\\Ryota Okunishi\\Downloads\\piyo_20190210_151615.kfk') as sample:
    s = sample.readlines()

new_s = [i for i in s if '評価値' in i]
print(new_s)

with open('C:\\Users\\Ryota Okunishi\\Downloads\\piyo_20190210_151615.kfk', encording='utf-8') as sample2:
    s2 = sample2.readline()
while s2:
    if '評価値' in s2:

        s2 = sample2.readline()
        print(s2)


for i in s:
    if '評価値' in s:
        print("ok")
    print(i)

'''
def if_test_in(s):
    if '3' in s:
        print("ok")
    else:
        print("no")
'''






list2 = {}
l_eval = [l for l in list if '評価値' in l]
print(l_eval)
for j in list[0:4]:
    print(list2)
"""
for line in lines:
    print(line)
kfk_file.close()
"""

#linesの整形(カンマと\nの排除)

regex = '   2 ８四歩(83)        ( 0:00/00:00:00)' '**解析 ○ 時間 00:03.4 深さ 20/28 ノード数 1115190 評価値 103↑ 読み筋 ▲２六歩(27) '
kif_regex2 = re.search(r'\d\s\d+\w\w\S\d\d\S\s\s\s\s\s\s\s\s', regex)
#kif_regex = re.findall(r'\d\s\d+\w+^[\u4E00-\u9FD0]+$', lines)
print(kif_regex2)

"""
for i in lines:
    print(lines)
"""