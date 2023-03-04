#!/usr/bin/python3

for _ in range(97, 123):
    if chr(_) != 'e' and chr(_) != 'q':
        print('{}'.format(chr(_)), end='')
