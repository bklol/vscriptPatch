import os
import mmap

# search: 55 48 89 E5 41 55 41 54 53 48 83 EC 08 83 FE 01
# 
class Patcher:

    def patch_vscript():
        if not Patcher.replace_bytes(
            "libvscript.so", b"\x55\x48\x89\xE5\x41\x55\x41\x54\x53\x48\x83\xEC\x08\x83\xFE\x01\x0F\x84\x0A\x02\x00\x00\x83\xFE\x02", b"\x55\x48\x89\xE5\x41\x55\x41\x54\x53\x48\x83\xEC\x08\x83\xFE\x02\x0F\x84\x0A\x02\x00\x00\x83\xFE\x01"
        ):
            print("failed to patch libvscript.so")
        else:
            print("your libvscript.so patched successful")

    def replace_bytes(filename, search_pattern, replace_bytes):
        try:
            with open(filename, "r+b") as f:
                mm = mmap.mmap(f.fileno(), 0)
                pos = mm.find(search_pattern)
                pos2 = mm.find(replace_bytes)
                if pos2 != -1:
                    print("your libvscript.so has already patched!")
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