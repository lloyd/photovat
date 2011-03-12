import sys
import os
import pyexiv2

for root, dirs, files in os.walk('.'):
    for name in files:
        if name.endswith(".jpg") or name.endswith(".JPG"):
            p = os.path.abspath(os.path.join(root, name))
            try:
                metadata = pyexiv2.ImageMetadata(p)
                metadata.read()
                print "---> %s" % name
                print metadata.dimensions
                print "keys: %d" %len(metadata.exif_keys)
            except IOError as e:
                pass

