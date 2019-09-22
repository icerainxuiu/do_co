import pytest


class TestLogin:
    platformName = "Android"

    @pytest.fixture(params=["1",'2','3','4'])
    def before(self):
        print("before")

    def setup_class(self):
        print("setup_class")

    def setup(self):
        print("setup")

    def teardown(self):
        print("teardown")
    @pytest.mark.skipif(True, reason=None)
    def test_01(self):
        print("test1")

    @pytest.mark.xfail(True, run=(platformName == "ios"))
    def teardown_class(self):
        print("teardown_class")

    @pytest.mark.parametrize("name", ["sisi","zhuzhu", "dfg"])
    def test_haha(self, name, before):
        print(name)
