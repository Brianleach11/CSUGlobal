#Write a program that calculates the total amount of a meal purchased at a restaurant. 
#The program should ask the user to enter the charge for the food and then calculate the amounts with an 18 percent tip and 7 percent sales tax. 
# Display each of these amounts and the total price.


def calculate_total_charge():
    tip = charge * 0.18
    tax = charge * 0.07
    total = charge + tip + tax
    print(f"The total charge is: ${total:.2f}")


charge = float(input("Enter the charge for the food: "))
calculate_total_charge()
