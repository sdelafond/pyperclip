# TODO - don't check this in. When I put the project all into a single file, this will go away.

import sys

from optparse import OptionParser # We use optparse instead of argparse to be compatible with Python 2.6.



def print_usage():
    print('Usage:') # TODO


def cli_cmd_copy():
    copy(sys.stdin.read().decode('utf-8'))


def cli_cmd_paste():
    sys.stdout.write(paste())


def main():
    # TODO - make it so that the user can pipe text in & out of the clipboard
    parser = OptionParser()
    parser.add_option('-i','--copy', action='store_const', const=cli_cmd_copy, dest='action', default=cli_cmd_copy)
    parser.add_option('-o','--paste', action='store_const', const=cli_cmd_paste, dest='action')
    opts, args = parser.parse_args()

    if len(args) == 0:
        print_usage()
        sys.exit(1)

    opts.action()

if __name__ == '__main__':
    main() # run this module as a cli command
