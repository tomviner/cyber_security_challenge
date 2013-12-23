import re


# From http://svn.python.org/projects/stackless/trunk/Demo/scripts/morse.py
CHAR_TO_MORSE = {
    "'": '.----.', '(': '-.--.-', ')': '-.--.-', ',': '--..--',
    '-': '-....-', '.': '.-.-.-', '/': '-..-.', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ':': '---...', ';': '-.-.-.', '?': '..--..',
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '_': '..--.-',
}

MORSE_TO_CHAR = {v:k for k,v in CHAR_TO_MORSE.items()}


def decode_to_words(s):
    """Takes a Morse code string and generates plaintext words"""
    words = re.split(r'\s{2,}', s)
    for i, word in enumerate(words):
        yield ''.join(MORSE_TO_CHAR.get(ch, ch) for ch in word.split(' '))

def decode(s):
    """Takes a Morse code string and returns plaintext"""
    return ' '.join(decode_to_words(s))


def encode_to_words(s):
    """Takes a plaintext string and generates Morse code words

    Morse letters are joined by a single space
    """
    words = s.split(' ')
    for i, word in enumerate(words):
        yield ' '.join(CHAR_TO_MORSE.get(ch, ch) for ch in word)

def encode(s):
    """Takes a plaintext string and returns Morse code

    Words are joined by a double space
    """
    return '  '.join(encode_to_words(s))
