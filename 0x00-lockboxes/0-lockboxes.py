#!/usr/bin/python3
"""Determines if boxes can be opened with key, starting with 0 = True"""

def canUnlockAll(boxes):
  #box zero in list of lists is unlocked (true)
  keyList = {
    0: True
  }

  loop = 0

  #all other boxes in list of lists are locked (false)
  for i in range(1, len(boxes)):
    keyList[i] = False

  #iterate through boxes in list of lists
  #while any box in keyList = false and loop = less than len
  while False in keyList and loop < len(boxes):
    for i in keyList:
      if keyList[i] is True:
        for k in boxes[i]:
          if k > 0 and k < len(boxes):
            #unlock values in current box of keyList
            keyList[k] = True
        
        loop += 1

  if False in keyList.values():
    return False
  
  return True
