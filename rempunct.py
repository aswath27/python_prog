
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

x = input("Enter a string: ")

# remove punctuation from the string
y = ""
for char in x:
   if char not in punctuations:
       y = y + char

# display the unpunctuated string
print(y)