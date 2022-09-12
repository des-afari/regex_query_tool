from django.test import TestCase
import re
# Create your tests here.
sentence = "This is a sentence"


pattern = re.compile(r'/w+')
print(pattern)

matches = pattern.finditer(sentence)

# for match in matches:
