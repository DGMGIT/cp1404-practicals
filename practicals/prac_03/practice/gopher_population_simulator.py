import random


DEFAULT_POPULATION = 1000
YEARS = 10
# percentages
MIN_DEATHS = 10
MAX_DEATHS = 22
MIN_BIRTHS = 5
MAX_BIRTHS = 25


def main():
    population = DEFAULT_POPULATION
    print("Welcome to the Gopher Population Simulator!")
    print(f"Starting population: {population}")

    for year in range(1, YEARS + 1):
        deaths = int(population * random.randint(MIN_DEATHS, MAX_DEATHS) / 100)
        births = int(population * random.randint(MIN_BIRTHS, MAX_BIRTHS) / 100)
        population -= deaths
        population += births
        print("Year {}\n\n{} gophers were born. {} died\nPopulation: {}"
              .format(year, births, deaths, population))


if __name__ == "__main__":
    main()
