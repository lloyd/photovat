#!/usr/bin/env python

import os, hashlib

def calc_sig(path):
    try:
        fp = open(path, 'rb')
        try:
            sig = hashlib.sha256()
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
                sig = calc_sig(p)
                d = sig[:3]
                tgt_dir = os.path.join(linkDir, d)
                tgt = os.path.join(tgt_dir, sig[3:] + ".jpg")
                if not os.path.isdir(tgt_dir):
                    os.mkdir(tgt_dir)
                if not os.path.islink(tgt):
                    os.symlink(p, tgt)
                
