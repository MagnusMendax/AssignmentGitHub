import unittest


# changes one letter at a time give a start word, target word and list of words
def dfs(start, target, words):
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
            #print(len(path) - 1)
            return path
        letters = list(UserWord)  ##contains [letter, letter, letter, letter]
        ##example [w, o, r, l, d] [0, 1, 2, 3, 4, 5]
        for unit, place in enumerate(letters):
            path.append(place)
            for letter in alphabet:  ##checks if any of the letters in the word are in the list alphabet
                test_word = "".join(letters[:unit]) + letter + "".join(letters[unit + 1:])
                if test_word in words and test_word not in seen:  ##if word is in text file and not seen
                    seen[test_word] = UserWord
                    source.append(test_word)

##error handling, making sure the file name is valid, if not prompting again
while True:
    try:
        fname = input("Enter dictionary name: ")
        file = open(fname)
        words = set([line.strip() for line in file.readlines()])##place word strip here for unit testing
        break
    except:
        print("Please enter a valid dictionary.")

##asks if use wants to add a dictionary of exemption words, if true then prompts for file and opens it
##otherwise will break, also reverts back to confirmation incase of accidental input
while True:
    try:
        userConfirm = input("Would you like to add a dictionary of exemption words? (y/n)")
    except:
        print("Please enter a valid response")
    if userConfirm == "y":
        try:
            userFile = input("Enter dictionary name: ")
            disallow = open(userFile)
            banned = set([line.strip() for line in disallow.readlines()])
            break
        except:
            print("Please enter a valid dictionary")
    elif userConfirm == "n":
        break

##if the user has input a banned words list remove them from words then call print dfs
if userConfirm == "y":
    for entry in banned:
        if entry in words:
            words.remove(entry)



# This is the unittesting portion, if wanting to test multiline comment out all while loops except for file input
##words = set([line.strip() for line in file.readlines()]) copy this into first file request when unittesting
##also remove the print(len(path)-1) in the dfs function
class TestWord_Ladder(unittest.TestCase):
    def test_dfs(self):
        if userConfirm == "n":
            self.assertEqual(dfs("lead", "gold", words), ['lead', 'load', 'goad', 'gold'])
            self.assertEqual(dfs("hide", "seek", words), ['hide', 'bide', 'bids', 'beds', 'bees', 'sees', 'seek'])
            self.assertEqual(dfs("run", "fun", words), ['run', 'fun'])
            self.assertEqual(dfs("lead", "fun", words), None)
            self.assertIsInstance(words, set)
        elif userConfirm == "y":
            self.assertEqual(dfs("lead", "gold", words), ['lead', 'head', 'held', 'geld', 'gold'])
            self.assertEqual(dfs("hide", "seek", words), ['hide', 'ride', 'rede', 'redd', 'reed', 'seed', 'seek'])
            self.assertIsInstance(banned, set)
if __name__ == '__main__':  ##if run this, then run the conditional code (unittest.main()), this file name is __main__,
    ##if imported into another file it would be word_ladder, this checks if it is imported or directly run
    unittest.main()
