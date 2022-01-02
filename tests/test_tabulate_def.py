from .config import *
from fix_my_functions import formatters
from redbaron import RedBaron
import pytest
import itertools


@pytest.mark.parametrize("do_interactive", [True, False], ids=["interactive", "non-interactive"])
@pytest.mark.parametrize("formatting_pass", formatters.FORMATTING_PASSES)
def test_single_formatting_pass(formatting_pass: formatters.FormattingPass, do_interactive: bool, red: RedBaron, set_expected):
    all_expected = set(FIXTURE_FORMATTING_EXPECTED.glob(f"_{formatting_pass.__name__}_{'interactive_*' if do_interactive else 'noninteractive'}.py"))
    counter = itertools.count()
    def compare_and_dump(red: RedBaron) -> bool:
        expected = FIXTURE_FORMATTING_EXPECTED / f"_{formatting_pass.__name__}_{'interactive_' + str(next(counter)) if do_interactive else 'noninteractive'}.py"
        if set_expected:
            with expected.open("w") as f:
                f.write(red.dumps())
        else:
            assert expected in all_expected
            all_expected.remove(expected)
            with expected.open("r") as f:
                assert red.dumps() == f.read()
        return False

    compare_and_dump(formatting_pass(red, interactive=compare_and_dump if do_interactive else False))
    if not set_expected:
        assert all_expected == set()
