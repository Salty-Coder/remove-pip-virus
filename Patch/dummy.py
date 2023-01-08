from adm4 import *

def is_Admin():
    is_admin = (os.getuid() == 0)
    return is_admin


def close():
    return "patched :|"

