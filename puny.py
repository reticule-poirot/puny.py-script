#!/usr/bin/env python3
import argparse, sys, encodings, logging
'''
Python script for IDNA encode/decode
'''

# TODO Encoding from punycode error.

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Encode to/decode from idna')
        parser.add_argument('-i', '--input', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='input file (default stdin)')
        parser.add_argument('-o', '--output', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='output file (default stdout)')
        parser.add_argument('-r', '--reverse', action='store_true', help='decode from idna')
        parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
        parser.add_argument('-d', '--verbose', action='store_true', help='debug output')
        args = parser.parse_args()
        if args.verbose:
            logging.basicConfig(level=logging.DEBUG)
            logging.debug('Using {} as input and {} as output'.format(args.input.name, args.output.name))
            if args.input.name == '<stdin>':
                logging.debug('Enter domain per line, and press ctrl+d')
        with args.input as sf:
            lines = sf.read().splitlines()
            logging.debug('Read from input: ' + ' '.join(lines))
            with args.output as df:
                if args.reverse:
                    lines = [l.encode('utf-8') for l in lines]
                    try:
                        lines = [l.decode('idna') for l in lines]
                    except UnicodeDecodeError:
                        logging.error('Error: wrong input')
                        exit(1)
                    logging.debug('Write to output: ' + ' '.join(lines))
                    df.writelines(l + '\n' for l in lines)
                else:
                    lines = [l.encode('idna') for l in lines]
                    lines = [l.decode('utf-8') for l in lines]
                    logging.debug('Write to output: ' + ' '.join(lines))
                    df.writelines(l + '\n' for l in lines)
    except KeyboardInterrupt:
        logging.info('Abort')
        exit(1)