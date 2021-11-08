import math
text = input("Please enter your age: ")


age = int(text)


max_rate = 220 - age
slowest = max_rate * 0.65
fastest = max_rate * 0.85

print(f'Your max heart will be {max_rate}, slowest is {slowest}, and your fastest is {fastest}')


