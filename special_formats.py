from __future__ import print_function
import re


def underscoreize(text, filename, regex):
    index = 0
    printed_lines = []
    underscored_line = ""
    result_str = ""
    for line in text.splitlines():
        results = re.finditer(regex, line)
        for i in range(0, len(line)):
            underscored_line += " "
        for match in results:
            s = match.start()
            e = match.end()
            if index not in printed_lines:
                print(line + " --- Line: " + str(index) + (", File: " + filename if filename else ""))
                result_str += line + " --- Line: " + str(index) + (", File: " + filename if filename else "") + '\n'
                printed_lines.append(index)
            for x in range(s, e):
                underscored_line = underscored_line[:x] + '^' + underscored_line[x + 1:]  # Fast char change in strings
        if '^' in underscored_line:
            print(underscored_line)
            result_str += underscored_line + '\n'
        underscored_line = ""
        index = index + 1
    result_str = result_str[:len(result_str) - 1]
    return result_str


def colorize(text, filename, regex):
    index = 0
    result_str = ""
    for line in text.splitlines():
        results = re.finditer(regex, line)
        results_copy = re.finditer(regex, line)
        iterator = 0
        results_length = 0
        match_iterator = 0
        for i in results_copy:  # get callable iterator length
            results_length = results_length + 1
        for match in results:
            s = match.start()
            e = match.end()
            highlighted_match = '\033[45m' + line[s:e] + '\033[0m'
            print(line[iterator:s] + highlighted_match, end='')
            result_str += line[iterator:s] + highlighted_match
            iterator = e
            if match_iterator == results_length - 1:  # Complete unfinished sentences
                print(line[e:len(line)], end='')
                result_str += line[e:len(line)]
                print(" --- Line: " + str(index) + (", File: " + filename if filename else ""))
                result_str += " --- Line: " + str(index) + (", File: " + filename if filename else "") + '\n'
            match_iterator = match_iterator + 1
        index = index + 1
    result_str = result_str[:len(result_str) - 1]
    return result_str


def machinize(text, filename, regex):  # format: file_name:no_line:start_pos:matched_text
    index = 0
    result_str = ""
    if not filename:
        filename = "standard_input"
    for line in text.splitlines():
        results = re.finditer(regex, line)
        for match in results:
            s = match.start()
            e = match.end()
            print('%s:%d:%d:%s' % (filename, index, s, line[s:e]))
            result_str += '%s:%d:%d:%s' % (filename, index, s, line[s:e]) + '\n'
        index = index + 1
    result_str = result_str[:len(result_str) - 1]
    return result_str


FUNCS = {
    '-u': underscoreize,
    '-c': colorize,
    '-m': machinize
}
