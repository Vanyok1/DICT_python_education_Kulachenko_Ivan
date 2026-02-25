class CoffeeMachine:
    """
    Represents a simple coffee machine simulation
    """

    def __init__(self):
        """
        Initialize the coffee machine with default resources.

        Returns:
        None
        """
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "action"

    def process(self, user_input):
        """
        Process user input and control the coffee machine actions.

        Parameters:
        user_input (str): Command entered by the user.

        Returns:
        bool: True to continue program, False to exit.
        """
        if self.state == "action":

            if user_input == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                self.state = "buy"

            elif user_input == "fill":
                print("Write how many ml of water do you want to add:")
                self.state = "fill_water"

            elif user_input == "take":
                self.take()

            elif user_input == "remaining":
                self.print_state()

            elif user_input == "exit":
                return False

        elif self.state == "buy":

            if user_input == "back":
                self.state = "action"
                return True

            self.make_coffee(user_input)
            self.state = "action"

        elif self.state.startswith("fill"):
            self.fill(user_input)

        return True

    def take(self):
        """
        Take all money from the coffee machine.

        Returns:
        None
        """
        print(f"I gave you {self.money}")
        self.money = 0

    def fill(self, user_input):
        """
        Add resources to the coffee machine.

        Parameters:
        user_input (str): Amount of resource entered by the user.

        Returns:
        None
        """
        if self.state == "fill_water":
            self.water += int(user_input)
            print("Write how many ml of milk do you want to add:")
            self.state = "fill_milk"

        elif self.state == "fill_milk":
            self.milk += int(user_input)
            print("Write how many grams of coffee beans do you want to add:")
            self.state = "fill_beans"

        elif self.state == "fill_beans":
            self.beans += int(user_input)
            print("Write how many disposable cups of coffee do you want to add:")
            self.state = "fill_cups"

        elif self.state == "fill_cups":
            self.cups += int(user_input)
            self.state = "action"

    def make_coffee(self, choice):
        """
        Prepare coffee based on the selected option.

        Parameters:
        choice (str): Coffee type selection (1, 2 or 3).

        Returns:
        None
        """
        if choice == "1":
            water_needed = 250
            milk_needed = 0
            beans_needed = 16
            cost = 4
        elif choice == "2":
            water_needed = 350
            milk_needed = 75
            beans_needed = 20
            cost = 7
        elif choice == "3":
            water_needed = 200
            milk_needed = 100
            beans_needed = 12
            cost = 6
        else:
            return

        if self.check_ingredients(water_needed, milk_needed, beans_needed):
            print("I have enough resources, making you a coffee!")
            self.use_ingredients(water_needed, milk_needed, beans_needed, cost)

    def check_ingredients(self, water, milk, beans):
        """
        Check if there are enough ingredients to make coffee.

        Parameters:
        water (int): Amount of water required.
        milk (int): Amount of milk required.
        beans (int): Amount of coffee beans required.

        Returns:
        bool: True if resources are sufficient, False otherwise.
        """
        if self.water < water:
            print("Sorry, not enough water!")
            return False

        if self.milk < milk:
            print("Sorry, not enough milk!")
            return False

        if self.beans < beans:
            print("Sorry, not enough coffee beans!")
            return False

        if self.cups < 1:
            print("Sorry, not enough disposable cups!")
            return False

        return True

    def use_ingredients(self, water, milk, beans, cost):
        """
        Deduct ingredients from the machine to make coffee.

        Parameters:
        water (int): Amount of water used.
        milk (int): Amount of milk used.
        beans (int): Amount of beans used.
        cost (int): Price of the coffee.

        Returns:
        None
        """
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= 1
        self.money += cost

    def print_state(self):
        """
        Display current resources of the coffee machine.

        Returns:
        None
        """
        print("\nThe coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money\n")


machine = CoffeeMachine()

while True:

    if machine.state == "action":
        print("Write action (buy, fill, take, remaining, exit):")

    user_input = input(" ")

    if not machine.process(user_input):
        break