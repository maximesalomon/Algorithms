#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batches = []
  for ing in recipe:
    if ing not in ingredients or recipe[ing] > ingredients[ing]:
      return 0
    else:
      batches.append(math.floor(ingredients[ing]/recipe[ing]))
  return min(batches) 

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 320, 'butter': 180, 'flour': 100 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))