file = open('フルパス¥¥ファイル名.kfk', 'r')
line = file.readline()
while line:
    if line in str('評価値'):
        print('存在します:' + str(line))
    else:
        print('存在しません')
file.close()
print('処理を終了しました')
