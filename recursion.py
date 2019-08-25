"""A recursive search and replace

  text: the input text
  search: pattern to match
  repl: what to turn the pattern into

  Really only done this way because the exercise asked for recursion,
  and it seems like cheating to use str.replace. but as one line,
  the answer is just text.replace(search, repl), no need for recursion."""

def recursive(text, search, repl):
    while search in text:
         before, text = text.split(search, 1)
         return before + repl + recursive(text, search, repl)
    return text

def wrapper():
     string = input("Please enter a string: ")
     substr = input("Please enter the substring you wish to find here : ")
     replstr = input("Please enter a string to replace the given substring: ")
     return recursive(string, substr, replstr)

print ("Your new string is " + wrapper())
