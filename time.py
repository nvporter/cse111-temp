import math



length = float(input('What is the langth of the pendulum: '))

time = (2 * math.pi) * math.sqrt(length / 9.81)

print(f'Time, (seconds): {time:.2f}')



