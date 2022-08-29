from pytest import raises

from hex2rgb import __version__, hex2rgb


def test_version():
    assert __version__ == "0.2.0"


def test_hex_len_hex2rgb() -> None:

    with raises(ValueError, match="Hex code length should be either 3 or 6"):
        assert hex2rgb("#FF")

    with raises(ValueError, match="Hex code length should be either 3 or 6"):
        assert hex2rgb("#F3FFF")


def test_white_hex2rgb() -> None:
    assert hex2rgb("#FFFFFF") == (255, 255, 255)


def test_black_hex2rgb() -> None:
    assert hex2rgb("#000000") == (0, 0, 0)


def test_aqua_hex2rgb() -> None:
    assert hex2rgb("#75D7EC") == (117, 215, 236)


def test_triplet_black_hex2rgb() -> None:
    assert hex2rgb("#000") == (0, 0, 0)


def test_triplet_white_hex2rgb() -> None:
    assert hex2rgb("#FFF") == (255, 255, 255)


def test_triplet_aqua_hex2rgb() -> None:
    assert hex2rgb("#75D") == (117, 215, 93)


def test_hex2rgb_case_insensitive() -> None:
    assert hex2rgb("#75d7Ec") == (117, 215, 236)
