import random
def primary():
 #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  last = 14
  rnd = random.randint(0, last)
  diff = random.randint(0, last)
  print(quotes[rnd])
  print(quotes[diff])

if __name__== "__main__":
  primary()
