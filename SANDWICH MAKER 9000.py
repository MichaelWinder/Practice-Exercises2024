menu = {
    "bread": {
        "Wholemeal": 1.00,
        "White": 0.80,
        "Cheesy White": 1.20,
        "Gluten Free": 1.40
    },
    "meat": {
        "Chicken": 2.69,
        "Beef": 3.00,
        "Salami": 4.00,
        "Vegan Slice": 3.30
    },
    "garnish": {
        "Onion": 1.69,
        "Tomato": 1.00,
        "Lettuce": 2.00,
        "Cheese": 2.50
    }
}
def sammake():
    boption = ""
    moption = ""
    goption = ""
    print("WELCOME TO MICHAEL'S SANDWICH MAKER 9000!!\n")
    while boption not in menu["bread"]:
        boption = input(f"What is your bread\nWholemeal: $1.00, White: "
                        f"$0.80, Cheesy White: $1.20, Gluten Free: $1.40\n: ")\
        .title()
    while moption not in menu["meat"]:
        moption = input(f"What is your meat\nChicken: $2.69, Beef: $3.00, "
                        f"Salami: $4.00, Vegan Slice: $3.30\n: ")\
        .title()
    while goption not in menu["garnish"]:
        goption = input(f"What is your garnish\nOnion: $1.69, Tomato: "
                        f"$1.00, Lettuce: $2.00, Cheese: $2.50\n: ")\
        .title()
    option = input(f"Your sandwich consists of {boption, moption, goption}"
                   f"\n1: Go to checkout\n2: Change the samwhich\n:")
    if option == "2":
        sammake()
    else:
        price = menu['bread'][boption]+menu['meat'][moption]+menu['garnish'][
            goption]
        print(f"Nice sandwich!\nYour total cost is ${price:.2f}")
sammake()
