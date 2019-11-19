from abc import ABC, abstractmethod
import json

class Logger2(ABC):

  @abstractmethod
  def __init__(self):
    pass

  class _Logger2:
    def __init__(self):
      self.f = open('Logger2.log', 'w')

    def log(self, text):
      self.f.write(text)

  instance = _Logger2()

  @staticmethod
  def log(text):
      Logger2.instance.log(text)
    