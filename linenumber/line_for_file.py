#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


class SimpleLineNumber:

    def __init__(self, input_file_name, output_file_name):
        self._input_file_name = input_file_name
        self._output_file_name = output_file_name

        # list of source file's lines
        self._lines = self._read_from_file()

        # make numbers list(from 1 to 999)
        self._numbers = map(lambda n: self._make_line_number(n), range(1, 1000))

    # function to add line number to single text
    @staticmethod
    def _make_line_number(number):
        number_strings = '   ' + str(number)

        start = len(number_strings) - 3
        end = len(number_strings)

        return number_strings[start:end] + '. '

    # open and read target source file
    def _read_from_file(self):
        # read file contents
        with open(self._input_file_name, 'r') as f:
            contents = f.read()

        text = contents.replace('\r', '')
        lines = text.split('\n')

        return lines

    # open and write to file
    def _write_to_file(self, text):
        with open(self._output_file_name, 'w') as f:
            f.write(text)
            f.flush()

    # search code block and add line numbers
    def process(self):
        # Python 2
        # text = map(lambda (n, s): n + s, list(zip(self._numbers, self._lines)))
        # Python 3
        text = [n + s for (n, s) in zip(self._numbers, self._lines)]
        self._write_to_file('\n'.join(text))


if __name__ == '__main__':
    args = sys.argv

    if len(args) != 3:
        print('Usage: python line_for_file.py [input] [output]')
        sys.exit(-1)

    SimpleLineNumber(args[1], args[2]).process()
