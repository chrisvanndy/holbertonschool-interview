#!/usr/bin/python3
"""Contains function lockboxes function canUnlockAll"""

def canUnlockAll(boxes):
  """Determins if boxes can be opened
  
  Arguments:
    boxes: list of lists, all lists are empty or contain ints

  Returns:
    True if all boxes can be accessed with key, else False
  """

  if not boxes:
    return False

  #instatiate list of keys including zero
  keysList = [0]
  
  #enumerate boxes, which gives lenth of boxes
  for i, box in enumerate(boxes):
    if i in keysList:
      #appends keysList w key in box, if not in keys already
      [keysList.append(key) for key in box if key not in keysList]
    else:
      return False
      
  return True



