poly_words = ("оно", "питон", "непитон", "топот")
word = tuple(filter(lambda x: x == x[::-1], poly_words))
print(word)
