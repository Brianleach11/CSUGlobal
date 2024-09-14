def get_rainfall_by_month(years):
    total = 0
    for i in range(years):
        for j in range(12):
            rainfall = int(input(f"Enter the rainfall for {i+1} year {j+1} month: "))
            total += rainfall
    return total

num_years = int(input("Enter the number of years: "))
total_rainfall = get_rainfall_by_month(num_years)
print(f"Total rainfall: {total_rainfall}")
print(f"Total months: {num_years * 12}")
print(f"Average rainfall: {total_rainfall / (num_years * 12)}")
