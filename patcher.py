import os
import mmap

# search: BE 01 ? ? ? 2B D6 74 61 3B D6
# 
class Patcher:

    def patch_vscript():
        if not Patcher.replace_bytes(
            "vscript.dll", b"\xBE\x01\x00\x00\x00\x2B\xD6\x74\x61\x3B\xD6", b"\xBE\x02\x00\x00\x00\x2B\xD6\x74\x61\x3B\xD6"
        ):
            print("failed to patch vscript.dll")
        else:
            print("your vscript.dll patched successful")

    def replace_bytes(filename, search_pattern, replace_bytes):
        try:
            with open(filename, "r+b") as f:
                mm = mmap.mmap(f.fileno(), 0)
                pos = mm.find(search_pattern)
                pos2 = mm.find(replace_bytes)
                if pos2 != -1:
                    print("your vscript.dll has already patched!")
                    return False
                if pos == -1:
                    return False
                mm[pos : pos + len(search_pattern)] = replace_bytes
            return True
        except IOError:
            print("failed to open: %s" % filename)
            return False


Patcher.patch_vscript()
input('press any key to exit...')