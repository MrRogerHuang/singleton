#!/usr/bin/python3
from SettingsBad import *
from SettingsGood import *

b0 = SettingsBad()
b0.set('p0', 0)
b0.save()

b1 = SettingsBad()
b1.set('p1', 1)
b1.save()

g0 = SettingsGood.getInstance()
g0.set('p0', 0)
g0.save()

g1 = SettingsGood.getInstance()
g1.set('p1', 1)
g1.save()