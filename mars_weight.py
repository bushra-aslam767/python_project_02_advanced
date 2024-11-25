def main():

    earth_weight = float(input("Enter your weight on Earth (in kg): "))
    
    mars_weight = earth_weight * 0.378
    
    
    print(f"Your weight on Mars would be: {round(mars_weight, 2)} kg")

if __name__ == "__main__":
    main()
