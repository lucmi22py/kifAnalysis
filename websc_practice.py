import glob
import kfkfilemove

kif_list = glob.glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\analysis\\*.kfk')

for num in range(10):
    file = kif_list[num]

    with open(file) as f:
        lines = f.readlines()
        f.close()
        for i in range(16):
            line_i = lines[i]
            if "先手：luc22" in line_i:
                if __name__ == '__main__':
                    kfkfilemove.move_glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\ana_sente', file)
                print('ana_senteへ移動しました')
                continue
            elif "後手：luc22" in line_i:
                if __name__ == '__main__':
                    kfkfilemove.move_glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\ana_gote', file)
                print('ana_goteへ移動しました')
                continue
    print(str(int(num + 1)) + '局目:' + file)
print('すべての処理が終了しました')
