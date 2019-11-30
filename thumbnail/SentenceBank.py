class SentenceBank():
    """List-like object of sentences"""
    def __init__(self):
        self._bank = []

    def __iter__(self):
        return iter(self._bank)

    def _load_from_file(self, filepath):
        with open(filepath, 'r') as f:
            self._bank += [line.rstrip().replace('\\n', '\n') for line in f]


def load(filepath):
    """Returns a list-like object of sentences fetched from a txt file"""
    bank = SentenceBank()
    bank._load_from_file(filepath)
    return bank
