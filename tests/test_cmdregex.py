import cmdregex
import pytest


def test_validate_regex():  # Anticipate argparse.ArgumentTypeError on invalid regex input
    with pytest.raises(cmdregex.argparse.ArgumentTypeError):
        cmdregex.validate_regex(r'[')


def test_run():  # Anticipate argparse.ArgumentTypeError when no input is provided
    with pytest.raises(cmdregex.argparse.ArgumentTypeError):
        test_args = cmdregex.argparse.Namespace(file_input=None)  # Mimic argparse args with no file input
        cmdregex.run(test_args, False)
