# import argparse
# import os
# parser = argparse.ArgumentParser()
# subparsers = parser.add_subparsers(dest='subparser_name')
# subparser1 = subparsers.add_parser('1')
# subparser1.add_argument('-x')
# subparser2 = subparsers.add_parser('2')
# subparser2.add_argument('y')
# parser.parse_args(['2', 'frobble'])
# Namespace(subparser_name='2', y='frobble')
import slate

with open('./data/mars-pdf.pdf', 'rb') as f:
    doc = slate.PDF(f)