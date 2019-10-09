#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  array = []
  list = ['rock', 'paper', 'scissors']  
  def rps(n, results):
    if n == 0:
      array.append(results)
    else:
      for i in range(len(list)):
        rps((n - 1), results + [list[i]])

  rps(n,[])
  return array

# print(rock_paper_scissors(2))

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')