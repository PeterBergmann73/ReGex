# https://callumacrae.github.io/regex-tuesday/challenge1.html
# Repeated words
# Wrap repeated words in a <strong> element.
import re

# compile the pattern
pattern1 = re.compile(r'\b(\w+)\s+\1\b')


class RepeatedWordWrapper:

    def wrap1(self, text):
        print(text)
        m = pattern1.sub(text).group()
        print(m)
        if m == None:
            return text
        else:
            return m
