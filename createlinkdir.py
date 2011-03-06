#!/usr/bin/env python

import 'os'

for root, dirs, files in os.walk('.'):
    for name in files:
        print os.join(root, name))
