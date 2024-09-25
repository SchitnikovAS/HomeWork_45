from itertools import pairwise


def all_variants(text):
    result = pairwise(text)
    i = 0
    while i != len(text):
        yield text[i]
        i += 1
    for value in result:
        yield value[0] + value[1]
    yield text


a = all_variants("abc")
for i in a:
    print(i)
