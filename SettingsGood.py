from abc import ABC, abstractmethod
import json

class SettingsGood(ABC):
  instance = None

  @abstractmethod
  def __init__(self):
    pass

  class _SettingsGood:
    def __init__(self):
      self.settings = {}

    def set(self, key, value):
      self.settings[key] = value

    def save(self):
      f = open('settingsGood.json', 'w')
      j = json.dumps(self.settings)
      f.write(j)
      f.close()

  @staticmethod
  def getInstance():
    if SettingsGood.instance == None:
      SettingsGood.instance = SettingsGood._SettingsGood()

    return SettingsGood.instance