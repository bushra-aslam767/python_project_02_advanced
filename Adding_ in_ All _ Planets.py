def main():
    
    gravity_factors = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    earth_weight = float(input("Enter your weight on Earth (in kg): "))

    planet = input("Enter the name of a planet: ")

    if planet in gravity_factors:
        planet_weight = earth_weight * gravity_factors[planet]
        print(f"Your weight on {planet} would be: {round(planet_weight, 2)} kg")
    else:
        print("Invalid planet name. Please enter a valid planet.")

if __name__ == "__main__":
    main()
