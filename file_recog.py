import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
#%matplotlib inline
import re

# 行数を数える
file_dir = r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\analysis'
file_name = r'luc22-itukyuusan-20200502_233415_ana.kfk'
with open(file_dir + str('\\') + file_name, 'r') as file:
    for line_count, _ in enumerate(file, 1):
        pass
print("全行数: " + str(int(line_count)))
file.close()


with open(file_dir + str('\\') + file_name, 'r') as file:
    lines = file.readlines()
    file.close()
print("全行数: " + str(int(line_count)))
honpu_point = []
ana_point = []

try:
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
except AttributeError:
    pass
    # 処理なし

del honpu_point[0]
print(honpu_point)
print(len(honpu_point))

print(ana_point)
print(len(ana_point))

num_te = list(range(1, len(honpu_point) + 1))
print(num_te)

print("現前局面評価値-前局面評価値")
diff_list = [honpu_point[0]]
result = honpu_point[1]-honpu_point[0]
diff_list.append(result)
for i in range(1, len(honpu_point)):
    try:
        result = honpu_point[i+1]-honpu_point[i]
        diff_list.append(result)
    except IndexError:
        break

print(diff_list)
print('計数処理を終了しました')

# カラーリスト
color_list = ['#B0E0E6', '#FA8072', '#B0C4DE', '#00CED1']

# グラフ描画処理
plt.subplot(2, 1, 1)
plt.plot(num_te, honpu_point, color=color_list[3])
plt.grid(which='major')

plt.subplot(2, 1, 2)
plt.plot(num_te, diff_list, color=color_list[1])
plt.grid(which='major')

plt.show()
plt.savefig("test_ana.png")
