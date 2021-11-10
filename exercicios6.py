import re
import nltk
from nltk.stem import WordNetLemmatizer

def number_valid(number):
    if re.search('[-|+]?\d+([.]\d+)?',number):
        return 'Valid'
    else:
        return 'Not valid'

def cell_or_fix(number):
    value = re.search("(([(]\d?\d{2}[)])|(\d?\d{2})) ?\d?\d{4}[ |-]?\d{4}", number)
    if value:
        if value[0] == number:
            return 'Valid'
    return 'Not valid'


print(cell_or_fix('8599912-3186'))


print(re.sub('3',' ', '3543'))
lemmatizer = WordNetLemmatizer()

print("rocks :", lemmatizer.lemmatize("rocks"))

