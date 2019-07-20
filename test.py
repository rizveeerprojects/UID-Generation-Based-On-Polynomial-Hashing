my_alphabet = ['a', 'b', 'c']

def custom_key(word):
   numbers = []
   for letter in word:
      numbers.append(my_alphabet.index(letter))
   return numbers

x=['cbaba', 'ababa', 'bbaa']
x.sort(key=custom_key)
print(x)