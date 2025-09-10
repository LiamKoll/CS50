from hello import hello

def default():
    assert hello() == "hello world"

def test_argument():
    assert hello("Liam") == "hello Liam"