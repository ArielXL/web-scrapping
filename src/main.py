from scrapper.scrapper import Scrapper

s1 = Scrapper('https://www.google.com', 5)
s1.startRequests()
print()

s2 = Scrapper('http://www.twitter.com', 4)
s2.startRequests()
print()

s4 = Scrapper('http://evea.uh.cu', 3)
s4.startRequests()
print()
