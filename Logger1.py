import json

class Logger1:
  def log(self, text):
    f = open('Logger1.log', 'a')
    f.write(text)
    f.close()