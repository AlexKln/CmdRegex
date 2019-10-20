import special_formats
import pytest
import random
import string


def test_machinize():
    test_str = "tst is 27 years old" + "\n" \
               "tsts is 201 https://docs.python.org/2/howto/argparse.html" + "\n" \
               "tsttst is https://www.youtube.com/watch?v=sa-TUpSx1JA tsts years old" + "\n" \
               "tsttstts is 775 years old and tsts is 255 years old and t24 is 24 years old" + "\n" \
               "hello tst https://stackoverflow.com/questions/32395529/argparse-with-spaces tsts 445"
    test_expression = r'(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?'
    assert special_formats.machinize(test_str, "tst", r'%s' % test_expression) == \
        "tst:1:12:https://docs.python.org/2/howto/argparse.html\n" \
        "tst:2:10:https://www.youtube.com/watch?v=sa-TUpSx1JA\n" \
        "tst:4:10:https://stackoverflow.com/questions/32395529/argparse-with-spaces"


def test_colorize():
    with pytest.raises(AttributeError):
        special_formats.colorize(91, "tst", r'\d{1,3}')


def test_underscoreize():
    test_str = "tst tst 27 tst4" + "\n" \
               "TST tst" + "\n" \
               "21tst 999 tst26" + "\n" \
               "1 22 333 " + "\n" \
               "tst 445"
    test_expression = r'\d{1,3}'
    assert special_formats.underscoreize(test_str, False, r'%s' % test_expression) == \
        "tst tst 27 tst4 --- Line: 0\n" \
        "        ^^    ^\n" \
        "21tst 999 tst26 --- Line: 2\n" \
        "^^    ^^^    ^^\n" \
        "1 22 333  --- Line: 3\n" \
        "^ ^^ ^^^ \n" \
        "tst 445 --- Line: 4\n" \
        "    ^^^"
