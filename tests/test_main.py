from spled_docs.main import MyClass


def test_add():
    assert MyClass(2).add(1) == 3
