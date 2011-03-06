#!/usr/bin/env python

import os, hashlib

def calc_md5(path):
    try:
        fp = open(path, 'rb')
        try:
            sig = hashlib.md5()
            while True:
                chunk = fp.read(1024 * 16)
                if not chunk: break
                sig.update(chunk)
            return sig.hexdigest()
        finally:
            fp.close()
    except IOError:
        return 'error'

linkDir = "linkdir"
os.mkdir(linkDir)

for root, dirs, files in os.walk('.'):
    for name in files:
        if name.endswith(".jpg") or name.endswith(".JPG"):
            p = os.path.abspath(os.path.join(root, name))
            if not os.path.islink(p): 
                md5 = calc_md5(p)
                d = md5[:2]
                tgt_dir = os.path.join(linkDir, d)
                tgt = os.path.join(tgt_dir, md5[2:] + ".jpg")
                if not os.path.isdir(tgt_dir):
                    os.mkdir(tgt_dir)
                if not os.path.islink(tgt):
                    os.symlink(p, tgt)
                
