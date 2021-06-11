from scrapper.scrapper import Scrapper

s1 = Scrapper('https://www.google.com')
s1.startRequests()
print()

s2 = Scrapper('http://www.twitter.com')
s2.startRequests()
print()

s3 = Scrapper('http://correo.estudiantes.matcom.uh.cu')
s3.startRequests()
print()

s4 = Scrapper('http://evea.uh.cu')
s4.startRequests()
print()
