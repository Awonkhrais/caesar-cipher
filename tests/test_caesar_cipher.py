from caesar_cipher import __version__
from caesar_cipher.ceasar_cipher import decrypt, encrypt,crack


def test_version():
    assert __version__ == '0.1.0'


def test_encrypt():
    actual = encrypt("Heloo $1 my Friend 2*5", 3)
    expected = "Khorr $1 pb Iulhqg 2*5"
    assert actual == expected


def test_decrypt():
    actual = decrypt("Khorr $1 pb Iulhqg 2*5", 3)
    expected = "Heloo $1 my Friend 2*5"
    assert actual == expected

def test_crack():
    actual = crack("Lw zdv wkh ehvw ri wlphv, lw zdv wkh zruvw ri wlphv.")
    expected = "It was the best of times, it was the worst of times."
    assert actual == expected