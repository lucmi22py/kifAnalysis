import pathlib
import shutil
import glob

f = glob.glob('C:\\Users\\Ryota Okunishi\\OneDrive\\棋譜\\shogiwarskifu\\rawkifu\\*_ana.kif')
# f1 = f[0]


def change_suffix(file_name, dst_path, from_suffix, to_suffix):
    # インスタンス化
    p = pathlib.Path(file_name)
    pp = pathlib.PurePath(file_name)
    # ファイルの拡張子を得る
    sf = pp.suffix

    # 変更対象かどうか判定する
    if sf == from_suffix:
        # ファイル名(拡張子除く)を得る
        st = pp.stem

        # 変更後のファイル名を得る
        to_name = st + to_suffix

        # ファイル名を変更する
        src_path = pp.parent
        set_file = src_path.joinpath(to_name)
        shutil.move(file_name, set_file)

        # ファイルを移動する
        # dst_file = p.replace(set_file)
        # dst_file.replace(dst_path + set_file.stem + set_file.suffix)
        # shutil.move(abs_file, dst_path)
