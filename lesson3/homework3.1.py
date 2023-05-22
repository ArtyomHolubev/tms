two_word = 'два слова'
i = two_word.index(' ')
word1 = two_word[:i]
word2 = two_word[i+1:]

# Способ 1

two_word_edit = '!' + word2 + ' ! ' + word1 + '!'
print(two_word_edit)
print('*'*30)

# Способ 2

two_word_edit_2 = f"!{word2} ! {word1}!"
print(two_word_edit_2)
print('*'*30)

# Способ 3

two_word_edit_3 = '!{} ! {}!'.format(word2, word1)
print(two_word_edit_3)
