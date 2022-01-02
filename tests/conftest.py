from .config import *
from redbaron import RedBaron
import pytest


def pytest_addoption(parser):
    parser.addoption("--set-expected", action="store_true",
        help="Write the epected output for the tests into fixtures/formattin_expected")

def pytest_generate_tests(metafunc):
    if "set_expected" in metafunc.fixturenames:
        if not FIXTURE_FORMATTING_EXPECTED.is_dir():
            FIXTURE_FORMATTING_EXPECTED.mkdir(parents=True, exist_ok=True)
        metafunc.parametrize("set_expected", [metafunc.config.option.set_expected], ids=["check-expected", "set-expected"].__getitem__)

@pytest.fixture
def red() -> RedBaron:
    with FIXTURE_FORMATTING_TARGET.open() as f:
        return RedBaron(f.read())
