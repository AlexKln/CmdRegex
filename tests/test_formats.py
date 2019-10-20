import formats
import pytest
import random
import string


def test_format():  # Compare number of results from vanilla format function vs python's count method
    results_1 = []
    results_2 = []
    for i in range(0, len(string.ascii_uppercase + string.ascii_lowercase + string.digits + ' ')):
        test_str = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + ' ') for _ in range(200))
        test_expression = r'%s' % ''.join(random.choice(string.ascii_uppercase +
                                                        string.ascii_lowercase + string.digits + ' ') for _ in range(1))
        test_format_class = formats.Format(test_str, test_expression, False, -1)
        results_1.append(test_format_class.format()[1])
        results_2.append(test_str.count(test_expression))
    assert results_1 == results_2
