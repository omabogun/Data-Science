def holiday_cost(city_flight, num_nights, rental_days): # this function calculates the total holiday costs, using three helper functions
      
    return plane_cost(city_flight) + hotel_cost(num_nights) + car_rental(rental_days)


def plane_cost(city_flight): # this function calculates the flight cost based on the argument city_flights from the user's selection
    for city in cities: # this loops through the dictionary cities which stores the plane cost for each city
        if city.lower() == city_flight.lower(): # ensures the dictionary entry matches the user's selection
            total_plane_cost = cities[city]
    print(f"Your plane cost is £ {total_plane_cost}")
    return total_plane_cost      


def hotel_cost(num_nights):  # this function calculates the hotel cost, it takes the argument num_nights from the user input
    total_hotel_cost = 300 * num_nights
    print(f"Your hotel accommodation cost for {num_nights} nights = £ {total_hotel_cost}")
    return total_hotel_cost


def car_rental(rental_days): # this function calculates the car rental cost, it takes the argument rental_days from the user's input
    total_car_rental = 50 * rental_days
    print(f"Your car rental cost for {rental_days} days = £ {total_car_rental}")
    return total_car_rental



# The program displays a friendly interactive menu and allows the user to make selections 
# and input values whilst using try: except: to catch any errors

print("== W E L C O M E   T O   T H E   H O L I D A Y   C O S T   C A L C U L A T O R  ==")
print("")

print("Select your holiday destination: ")
print("Enter 't' if you want to travel to Tokyo:")
print("Enter 'h' if you want to travel to Hong Kong:")
print("Enter 'n' if you want to travel to New York:")
print("Enter 'c' if you want to travel to Cape Town:")
print("")

# Below is a dictionary cities that stores the cities and the plane cost to those cities
cities = {
     "t": 2000,
     "h": 3000,
     "n": 1500,
     "c": 2500
}

#  This while loops ensures the user enters the right value that will be used to match the dictionary item
while True:
    city_flight = input("Enter your selection: ").lower()
    if city_flight in cities:
        if city_flight == "t":
            city = "Tokyo"            
        elif city_flight == "h":
            city = "Hong Kong"            
        elif city_flight == "n":
            city = "New York"            
        elif city_flight == "c":
            city = "Cape Town"            
        break
    else:
        print("You have entered an invalid input! Type the first letter of the city you want to visit")
        

# This while loop ensures the user enters a numeric value for number of nights for hotel accommodation
while True:
        print("Hotel accommodation costs £300 per night")
        num_nights = input("How many nights are you staying for: ")
        print("")
        if num_nights.isdigit():
            num_nights = int(num_nights)
            break
        else:
            print("You have entered an invalid input! You need to enter the exact number of nights you intend to stay for!")


# This while loop ensures the user enters a numeric value for the number of days for car rental
while True:
        print("Car rental costs £50 per day")
        rental_days = input("How many days are you hiring a car for: ")
        print("")
        if rental_days.isdigit():
            rental_days = int(rental_days)
            break
        else:
            print("You have entered an invalid input! You need to enter the exact number of days you want to hire the car!")

print(f"The city you selected is {city}")
print(f"The total cost of your holiday = £ {holiday_cost(city_flight, num_nights, rental_days)}")
