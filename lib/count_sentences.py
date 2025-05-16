import re

class MyString:
    """
    A custom string class that supports sentence detection and counting.
    """
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    @property
    def value(self):
        """The string value stored in this MyString instance."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Set the string value, ensuring it is of type str, or print an error if not."""
        if not isinstance(new_value, str):
            print("The value must be a string.")
            return
        self._value = new_value

    def is_sentence(self):
        """Return True if the value ends with a period."""
        return self._value.endswith('.')

    def is_question(self):
        """Return True if the value ends with a question mark."""
        return self._value.endswith('?')

    def is_exclamation(self):
        """Return True if the value ends with an exclamation mark."""
        return self._value.endswith('!')

    def count_sentences(self):
        """
        Count the number of sentences in the string value. Sentences are considered
        to end with one or more of ., ?, or !. Consecutive punctuation counts as a
        single sentence boundary.
        """
        # Split on groups of sentence-ending punctuation
        parts = re.split(r'[\.\?!]+', self._value)
        # Filter out any empty strings or whitespace-only pieces
        sentences = [p for p in parts if p.strip()]
        return len(sentences)
