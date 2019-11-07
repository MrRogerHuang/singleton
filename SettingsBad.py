import json

class SettingsBad:
  def __init__(self):
    self.settings = {}

  def set(self, key, value):
    self.settings[key] = value

  def save(self):
    f = open('settingsBad.json', 'w')
    j = json.dumps(self.settings)
    f.write(j)
    f.close()