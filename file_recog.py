import re

# 行数を数える
with open('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\analysis\\piyo_20200108_175545_ana.kfk', 'r') as file:
    for line_count, _ in enumerate(file, 1):
        pass
print(int(line_count))
file.close()


'''
file2 = open('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\analysis\\piyo_20200108_175545_ana.kfk', 'r')
lines = file2.readlines()
file2.close()
'''

with open('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\analysis\\piyo_20200108_175545_ana.kfk', 'r') as file:
    lines = file.readlines()
    file.close()
honpu_point = []
ana_point = []

for i in range(0, line_count):
    i_line = lines[i]
    if '解析' in i_line:
        m_honpu = re.search(r'評価値\s(-|)\d{1,5}', i_line)
        mp_honpu_list = m_honpu.group().split()
        mp_honpu = mp_honpu_list[1]
        t = int(str(mp_honpu))
        honpu_point.append(t)
        #print(honpu_point)
        continue
    elif '候補手' in i_line:
        m_ana = re.search(r'評価値\s(-|)\d{1,5}', i_line)
        mp_ana_list = m_ana.group().split()
        mp_ana = mp_ana_list[1]
        t2 = int(str(mp_ana))
        ana_point.append(t2)
        #t2 = int(str())
        #ana_point.append(t2)
        continue
del honpu_point[0]
print(honpu_point)
print(len(honpu_point))

print(ana_point)
print(len(ana_point))
print('処理を終了しました')
