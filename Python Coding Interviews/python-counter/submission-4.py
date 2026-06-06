from collections import Counter
from typing import Counter as CounterType
from collections import defaultdict
from typing import List, Dict


def count_chars(s1: str, s2: str) :

    s3 = s1 + s2
    
    freq = defaultdict(int)
    for token in s3:
        freq[token] = freq[token] + 1

    return freq
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
