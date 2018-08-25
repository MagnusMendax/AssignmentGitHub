import unittest
#changes one letter at a time give a start word, target word and list of words
def bfs(start, target, words):
  alphabet = [chr(i) for i in range(97, 122)]
  seen = {start: None}
  source = [start]
  path = []
  while source:
    UserWord = source.pop(0)
    if UserWord == target:
      path = []
      while UserWord:
        path.insert(0, UserWord)
        UserWord = seen[UserWord]
      return path
    letters = list(UserWord)##contains [letter, letter, letter, letter]
    ##example [w, o, r, l, d] [0, 1, 2, 3, 4, 5]
    for unit, place in enumerate(letters):
      path.append(place)
      for letter in alphabet:##checks if any of the letters in the word are in the list alphabet
        test_word = "".join(letters[:unit]) +letter + "".join(letters[unit+1:])
        if test_word in words and test_word not in seen:##if word is in text file and not seen
          seen[test_word] = UserWord
          source.append(test_word)

##error handling, making sure the file name is valid, if not prompting again
while True:
  try:
    fname = input("Enter dictionary name: ")
    file = open(fname)
    break
  except:
    print("Please enter a valid dictionary name")
'''
##error handling, making sure the start word given have no integers in them and will
##prompt for another input until it recieves a valid entry
while True:
  start = input("Enter start word:")
  if start.isalpha():
    if start.islower():
      words = set([line.strip() for line in file.readlines()]) ##strips all words in file, places them into words, mutable.
      #can be used as list instead of set but increases search time
      break
    elif not start.islower():
      print("Error, invalid start word. Please enter a word in lowercase")
  elif not start.isalpha():
    print("Error, invalid start word. Please enter a word in lowercase")

##error handling, making sure the target given have no integers in them and will
##prompt for another input until it recieves a valid entry
while True:
    target = input("Enter target word:")
    if target.isalpha():
      if target.islower():
        break
      elif not target.islower():
        print("Error, invalid target word. Please enter a word in lowercase.")
    elif not target.isalpha():
      print("Error, invalid target word. Please enter a word in lowercase")

#call bfs to give the path length and path
print(bfs(start, target, words))
'''
words = set([line.strip() for line in file.readlines()])
class TestWord_Ladder(unittest.TestCase):
    def test_bfs(self):
        self.assertEqual(bfs("lead", "gold", words), ['lead', 'load', 'goad', 'gold'])
        self.assertEqual(bfs("hide", "seek", words), ['hide', 'bide', 'bids', 'beds', 'bees', 'sees', 'seek'])
        self.assertEqual(bfs("run", "fun", words), ['run', 'fun'])
        self.assertEqual(bfs("lead", "fun", words), None)
        self.assertIsInstance(words, set)

if __name__ == '__main__':##if run this, then run the conditional code (unittest.main()), this file name is __main__,
                          ##if imported into another file it would be word_ladder, this checks if it is imported or directly run
    unittest.main()




