#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import line_for_file

if __name__ == '__main__':
    args = sys.argv

    if len(args) != 3:
        print('Usage: python line_for_dir.py [input_directory] [output_directory]')
        sys.exit(-1)

    if not os.path.exists(args[1]):
        print('Input directory is not exists.')
        sys.exit(-1)

    if not os.path.exists(args[2]):
        print('Output directory is not exists.')
        sys.exit(-1)

    files = [f for f in os.listdir(args[1]) if os.path.isfile(os.path.join(args[1], f))]
    print(files)

    for f in files:
        line_for_file.SimpleLineNumber(os.path.join(args[1], f), os.path.join(args[2], f)).process()
