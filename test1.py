#!/usr/bin/python3
from SettingsBad import *
from SettingsGood import *
import asyncio
import time

async def F_1_1():
  print('F_1_1')
  s1 = SettingsBad()
  await asyncio.sleep(2)
  s1.set('p0', 0)
  await asyncio.sleep(1)

async def F_1_2():
  print('F_1_2')
  s2 = SettingsBad()
  await asyncio.sleep(1)
  s2.set('p1', 1)
  await asyncio.sleep(2)

async def F_2_1():
  print('F_2_1')
  await asyncio.sleep(2)
  SettingsGood.getInstance().set('p0', 0)
  await asyncio.sleep(1)

async def F_2_2():
  print('F_2_2')
  await asyncio.sleep(1)
  SettingsGood.getInstance().set('p1', 1)
  await asyncio.sleep(2)

async def main():
  await asyncio.wait([F_1_1(), F_1_2(), F_2_1(), F_2_2()])
  SettingsGood.getInstance().save()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
