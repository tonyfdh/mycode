#!/usr/bin/env python3

def main():

    # define the lists
    animals = ["Fox", "Fly", "Ant", "Bee", "Cod", "Cat", "Dog", "Yak", "Cow", "Hen", "Koi", "Hog", "Jay", "Kit"]
    animalC = []
    # print the animals
    print(animals)

    # Loops to pull out the C animals


    for item in animals:
        if item.startswith("C"):
            animalC.append(item)
    # print animals that start with the letter C
    print(animalC)

main()

