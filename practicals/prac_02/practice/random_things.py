import random

random_number = random.randint(1, 2)
rand_bool = False
if random_number == 1:
    rand_bool = True
else:
    rand_bool = False

print(rand_bool)

rand_bool = random.choice([True, False])
print(rand_bool)