import pandas as pd
from collections import Counter


class Text:


    def __init__(self, path):
        self.path = path


    @property
    def delimiter(self):
        possible_delimiters = ['|', ';', ':', '\t', ',']

        with open(self.path) as f:
            content = f.read()
            count = Counter(content)

            delimiter_occurences = { delimiter: count[delimiter]
                                     for delimiter in possible_delimiters }

            return max(delimiter_occurences.items(), key=lambda k: k[1])[0]


    def get_dataframe(self):
        return pd.read_csv(self.path, delimiter=self.delimiter)
