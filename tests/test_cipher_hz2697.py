from cipher_hz2697 import cipher_hz2697

def test_cipher():
    result = cipher_hz2697.cipher('love', shift = 1, encrypt = True)
    expected = 'mpwf'
    assert result == expected, 'result not equal to expected value'

