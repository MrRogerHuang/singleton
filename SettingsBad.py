import json

class SettingsBad:
  def __init__(self):
    try:
      f = open('settingsBad.json', 'r')
      self.j = json.loads(f.read())
      f.close()
    except:
      self.j = {}
    self.f = open('settingsBad.json', 'w')

  def set(self, key, value):
    self.j[key] = value
    self.f.write(json.dumps(self.j))
