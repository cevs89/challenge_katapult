from unicodedata import normalize


def normalize_frase(_text):
    _nomalize_text = normalize("NFC", _text)
    return _nomalize_text.lower().strip()
