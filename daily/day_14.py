import random


def estimate_pi() -> float:
    radius: int = 180
    random_tries: int = 100000
    total_in_circle: int = 0

    for dots in range(0, random_tries):
        x = random.randint(-radius, radius)
        y = random.randint(-radius, radius)

        #Apply Pythagoras Formula to find out the distance to the centre of the screen
        distance = (x**2 + y**2)**0.5

        #Check if dot is in the circle
        if distance < radius:
            total_in_circle += 1

    return round(4 * (total_in_circle / random_tries), 3)

print(estimate_pi())