import re
def same(item, target):
  return len([c for (c, t) in zip(item, target) if c == t])

def build(pattern, words, seen, list):
  return [word for word in words
                 if re.search(pattern, word) and word not in seen.keys() and
                    word not in list]

def find(word, words, seen, target, path):
  list = []
  for i in range(len(word)):
    list += build(word[:i] + "." + word[i + 1:], words, seen, list)
  if len(list) == 0:
    return False
  list = sorted([(same(w, target), w) for w in list])
  for (match, item) in list:
    if match >= len(target) - 1:
      if match == len(target) - 1:
        path.append(item)
      return True
    seen[item] = True
  for (match, item) in list:
    path.append(item)
    if find(item, words, seen, target, path):
      return True
    path.pop()
##error handling, making sure the file name is valid, if not prompting again
while True:
  try:
    fname = input("Enter dictionary name: ")
    file = open(fname)
    break
  except:
    print("Please enter a valid dictionary name")
lines = file.readlines()
##error handling, making sure the start word given have no integers in them and will
##prompt for another input until it recieves a valid entry
while True:
  start = input("Enter start word:")
  if start.isalpha():
    words = []
    for line in lines:
      word = line.rstrip()
      if len(word) == len(start):
        words.append(word)
    break
  elif not start.isalpha():
    print("Please enter a valid start word")
##error handling, making sure the target given have no integers in them and will
##prompt for another input until it recieves a valid entry
while True:
    target = input("Enter target word:")
    if target.isalpha():
      break
    elif not target.isalpha():
      print("Please enter a valid target word")
count = 0
path = [start]
seen = {start : True}
if find(start, words, seen, target, path):
  path.append(target)
  print(len(path) - 1, path)
else:
  print("No path found")

