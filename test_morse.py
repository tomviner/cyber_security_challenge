from morse import encode, decode


class TestSOS(object):
    morse_sos = '... --- ...'

    def test_sos_decode(self):
        assert decode(self.morse_sos) == 'SOS'

    def test_sos_encode(self):
        assert encode('SOS') == self.morse_sos


class TestWords(object):
    morse_12_23 = '.---- ..---  ...-- ....-'

    def test_words_encode(self):
        assert encode('12 34') == self.morse_12_23

    def test_words_decode(self):
        assert decode(self.morse_12_23) == '12 34'
