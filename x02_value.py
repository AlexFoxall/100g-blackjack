#!python3
from x01_deck import *


def value():
  x = createDeck()
  hand = []
  
  for i in x:
    hand.append(i)

    print(hand)
    d = sum(hand)
    
  return hand

value()
print(value)
'''
def main():
  assert value(['AH','3D','4S']) ==[8,18]
  assert value(['KH','TD']) == 20
  assert value(['3D','8H']) == 11
  assert value(['KC','6S','QD']) == 26

if __name__ == "__name__":
  main()
'''