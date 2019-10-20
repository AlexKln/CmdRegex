import re
from special_formats import FUNCS


class Format:

    def __init__(self, text, regex, filename, process_func):
        self.text = text
        self.regex = regex
        self.filename = filename
        self.process_func = process_func

    def format(self):
        if self.process_func == -1:  # No specific printing format, using default
            index = 0
            result_str = ""
            num_of_results = 0
            printed_lines = []
            for line in self.text.splitlines():
                results = re.findall(r'%s' % self.regex, line)
                if results and index not in printed_lines:  # results is not an empty list and line wasn't printed yet
                    print(line + " --- Line: " + str(index) + (", File: " + self.filename if self.filename else ""))
                    result_str += line + " --- Line: " + str(index) + \
                        (", File: " + self.filename if self.filename else "") + '\n'
                    num_of_results += len(results)
                    printed_lines.append(index)
                index = index + 1
            return result_str, num_of_results
        else:
            return self.process_func(self.text, self.filename, self.regex)


def make_process_func(underscore, color, machine):
    if underscore:
        return FUNCS['-u']
    elif color:
        return FUNCS['-c']
    elif machine:
        return FUNCS['-m']
    else:
        return -1
