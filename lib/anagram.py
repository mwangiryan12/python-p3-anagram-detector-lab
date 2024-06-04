# your code goes here!

class Anagram:
    def __init__(self,word):
        self.word = word
    def match(self,lst):
        self.lst = lst
        arr = []
        for wor in lst:
            lettersArr = [letter for letter in wor]
            if sorted(lettersArr) == sorted(list(self.word)):
              
                print(wor)
                arr.append(wor)
        return arr

word = Anagram("enlist")
print(word.match(["listen", "poison", "hello"]))
