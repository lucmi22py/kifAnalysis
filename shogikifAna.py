import kif_handle
import kfkfilemove
import kfkfiling
import glob
import os
import pathlib

print('回数を入力してください')
loop_num = int(input())
for num in range(1,loop_num + 1):
    if __name__ == '__main__':
        kif_handle.openkif()

    if __name__ == '__main__':
        kif_handle.anakif()

    if __name__ == '__main__':
        kif_handle.finana()

    if __name__ == '__main__':
        kif_handle.savekif()

    # 同名kifファイル移動
    path = 'C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu'
    A1 = glob.glob(os.path.join(path, '*_ana.*'))  # 対象1
    A1_list_str = A1[0]
    B = pathlib.Path(A1_list_str)
    Target1_deana = B.stem.rstrip("_ana")
    A2 = glob.glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu\\*.kif')  # 対象2
    for A2_element in A2:
        if Target1_deana in A2_element:
            if __name__ == '__main__':
                kfkfilemove.move_glob(r'C:\Users\Ryota Okunishi\OneDrive\棋譜\shogiwarskifu\rawkifu2',
                                      A2_element)
            break

    # kfkfilingによるkfk化は最後にすること
    # pyファイルのあるディレクトリへ対象ファイルを移動させるため
    # *_ana.kifファイルのkfk化
    f = glob.glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu\\*_ana.kif')
    try:
        f1 = f[0]
        if __name__ == '__main__':
            kfkfiling.change_suffix(f1, '.kif', '.kfk')
        else:
            print("file is not exist")
    except IndexError:
        print("*_ana.kifファイルは存在しません")
    except NameError:
        print("*_ana.kifファイルが見つからないので、f1は存在しません")

    # kfkファイル移動
    try:
        if __name__ == '__main__':
            kfkfilemove.move_glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\analysis','C:\\Users\\Ryota Okunishi\\pycharm_projects\\kifAnalysis\\*_ana.kfk')
    except IndexError:
        print("kfkファイルは存在しません")

    print('棋譜解析完了しました。:' + str(int(num)) + '局目')