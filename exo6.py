words = input("Enter a list of words (separated by spaces): ")

set_words = set(words.split())

dictionary = {}
for w in set_words:
  dictionary[w] = len(w)

print("Set of words (without duplicates):")
print(set_words)
print("Dictionary of words and their lengths:")
print(dictionary)