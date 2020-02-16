import shutil
import glob


def move_glob(dst_path, pathname, recursive=True):    # dst_path = 保存先のpath, pathname = 保存元のpath
    for p in glob.glob(pathname, recursive=recursive):
        shutil.move(p, dst_path)
