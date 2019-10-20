#! /usr/bin/env python2.7
import argparse
import re
import sys
from formats import Format, make_process_func


def run(args, standard_input_flag):
    raw_text = ""
    stdin_condition = (args.file_input is None) or (args.file_input is not None and args.file_input[0] == "-")
    no_input_condition = (not standard_input_flag and stdin_condition)
    if no_input_condition:  # error if no input is given
        msg = 'No type of input was provided'
        raise argparse.ArgumentTypeError(msg)
    if stdin_condition:
        # -in not provided or provided with "-", using standard input
        f_in = sys.stdin.read().splitlines()
        for line in f_in:
            raw_text += line + '\n'
        process_func = make_process_func(args.underscore, args.color, args.machine)
        result_format = Format(raw_text, args.regex[0], False, process_func)
        print("============================ OUTPUT ============================")
        result_format.format()
    else:
        print("============================ OUTPUT ============================")
        for f in args.file_input:  # Iterate over file list
            f_in = open(f)
            for line in f_in:  # Iterate over single file content
                raw_text += line
            process_func = make_process_func(args.underscore, args.color, args.machine)
            result_format = Format(raw_text, args.regex[0], f, process_func)
            result_format.format()
            raw_text = ""


def main():
    parser = argparse.ArgumentParser(description="Regular expression finder for the command line")
    parser.add_argument("-in", help="input file or files", dest="file_input", type=str, nargs='+')
    parser.add_argument("-r", "--regex", help="regular expression to look for",
                        type=validate_regex, required=True, dest="regex", nargs=1)
    mutual_exclusive = parser.add_mutually_exclusive_group()
    mutual_exclusive.add_argument("-u", "--underscore", help="show results in underscore format",
                                  action="store_true", dest="underscore")
    mutual_exclusive.add_argument("-c", "--color", help="show results in colored format",
                                  action="store_true", dest="color")
    mutual_exclusive.add_argument("-m", "--machine", help="show results in machine format",
                                  action="store_true", dest="machine")
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args, not sys.stdin.isatty())


def validate_regex(regex):
    try:
        re.compile(r'%s' % regex)
        return regex
    except re.error:
        msg = r'%s' % regex + ' is not a valid regex'
        raise argparse.ArgumentTypeError(msg)


if __name__ == "__main__":
    main()
