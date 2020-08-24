#!/usr/bin/env python3
'''Python script for IDNA encode/decode'''
import argparse
import sys
import logging

logger = logging.getLogger('punny.py')
logging.basicConfig(format='%(name)s: %(message)s')

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='Encode to/decode from idna')
        parser.add_argument('domain', nargs='*', help='domain names (divided by space)')
        parser.add_argument('-i', '--input', nargs='?', type=argparse.FileType('r'),
                            default=sys.stdin, help='input file (default stdin)')
        parser.add_argument('-o', '--output', nargs='?', type=argparse.FileType('w'),
                            default=sys.stdout, help='output file (default stdout)')
        parser.add_argument('-r', '--reverse', action='store_true', help='decode from idna')
        parser.add_argument('-V', '--version', action='version', version='%(prog)s 0.2')
        parser.add_argument('-d', '--debug', action='store_true', help='debug output')
        args = parser.parse_args()
        if args.debug:
            logger.level = logging.DEBUG
        if args.domain:
            logger.debug('Using %s as input and %s as output', args.domain, args.output.name)
            user_input = args.domain
        else:
            logger.debug('Using %s as input and %s as output', args.input.name, args.output.name)
            with args.input as sf:
                if args.input.name == '<stdin>':
                    logger.debug('Enter domains divided by space')
                    user_input = sf.readline().split()
                else:
                    user_input = sf.read().splitlines()
                logger.debug('Read from input: %s', ' '.join(user_input))
        with args.output as df:
            if args.reverse:
                user_input = [l.encode('utf-8') for l in user_input]
                try:
                    user_input = [l.decode('idna') for l in user_input]
                except UnicodeDecodeError:
                    logger.error('Wrong input')
                    sys.exit(1)
                logger.debug('Write to output: %s', ' '.join(user_input))
                df.writelines(l + '\n' for l in user_input)
            else:
                user_input = [l.encode('idna') for l in user_input]
                user_input = [l.decode('utf-8') for l in user_input]
                logger.debug('Write to output: %s', ' '.join(user_input))
                df.writelines(l + '\n' for l in user_input)
    except KeyboardInterrupt:
        logger.info('Abort')
        sys.exit(1)
