import kif_handle
import kfkfilemove
import kfkfiling
import glob


if __name__ == '__main__':
    kif_handle.anakif()

if __name__ == '__main__':
    kif_handle.finana()

if __name__ == '__main__':
    kif_handle.savekif()

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

try:
    if __name__ == '__main__':
        kfkfilemove.move_glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\analysis','C:\\Users\\Ryota Okunishi\\pycharm_projects\\kifAnalysis\\*_ana.kfk')
except IndexError:
    print("kfkファイルは存在しません")