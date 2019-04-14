import sys
import argparse


class DefaultHelpParser(argparse.ArgumentParser):
    def error(self, message):
        print("ERROR: {message}.".format(message=message), file=sys.stderr)
        self.print_help()
        sys.exit(2)


def init_parser():
    parser = DefaultHelpParser(
        description='Pure-python command-line calculator.')
    parser.add_argument(
        'expression',
        action='store',
        type=str,
        metavar='EXPRESSION',
        help='expression string to evaluate')
    return parser


def process_expression(args):
    print(args.expression)


def handle_commands():
    parser = init_parser()
    args = parser.parse_args()
    process_expression(args)