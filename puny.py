#!/usr/bin/env python3
import argparse, sys, encodings, logging
'''
Python script for IDNA encode/decode
'''

# TODO Encoding from punycode error.
# TODO Logging improvement

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Encode to/decode from idna')
        parser.add_argument('domain',nargs='*', help='domain names (divided by space)')
        parser.add_argument('-i', '--input', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='input file (default stdin)')
        parser.add_argument('-o', '--output', nargs='?', type=argparse.FileType('w'), default=sys.stdout, help='output file (default stdout)')
        parser.add_argument('-r', '--reverse', action='store_true', help='decode from idna')
        parser.add_argument('-V', '--version', action='version', version='%(prog)s 0.2')
        parser.add_argument('-d', '--debug', action='store_true', help='debug output')
        args = parser.parse_args()
        if args.debug:
            logging.basicConfig(level=logging.DEBUG)
        if args.domain:
            logging.debug('Using {} as input and {} as output'.format(args.domain, args.output.name))
            user_input = args.domain
        else:
            logging.debug('Using {} as input and {} as output'.format(args.input.name, args.output.name))
            if args.input.name == '<stdin>':
                    logging.debug('Enter domain per line, and press ctrl+d')
            with args.input as sf:
                user_input = sf.read().splitlines()
                logging.debug('Read from input: ' + ' '.join(user_input))
        with args.output as df:
            if args.reverse:
                user_input = [l.encode('utf-8') for l in user_input]
                try:
                    user_input = [l.decode('idna') for l in user_input]
                except UnicodeDecodeError:
                    logging.error('Wrong input')
                    exit(1)
                logging.debug('Write to output: ' + ' '.join(user_input))
                df.writelines(l + '\n' for l in user_input)
            else:
                user_input = [l.encode('idna') for l in user_input]
                user_input = [l.decode('utf-8') for l in user_input]
                logging.debug('Write to output: ' + ' '.join(user_input))
                df.writelines(l + '\n' for l in user_input)
    except KeyboardInterrupt:
        logging.info('Abort')
        exit(1)
