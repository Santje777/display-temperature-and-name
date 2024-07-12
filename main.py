   
def greet_user(firstname, last_name):
    """Welcome the user"""
    full_name = firstname + " " + last_name
    print(f"Hallo {full_name}")

greet_user("Susanne","is Awesome")

def display_temperature(city, temperature, humidity=""):
    """Displays the temperature, city name and humidity"""
    if humidity:
        print(f"The temperature in {city} is currently {temperature} degrees, with a humidity of {humidity}%")
    else:
        print(f"The temperature in {city} is currently {temperature} degrees")

display_temperature("London", 7, 40)
display_temperature("New York", 10)

def display_full_name(first_name, last_name, middle_name=""):
    """Display a full name based on the first, last and middle name"""
    if middle_name:
        full_name = first_name + " " + middle_name + " " + last_name
    else:
     full_name = first_name + " " + last_name 
    return full_name

name = display_full_name("Susanne", "Susanna", "van Oosterom")
print("My full name is " + name)