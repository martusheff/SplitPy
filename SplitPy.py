# Creates a instance of a party member.
class Friend:
    def __init__(self, name, contribution):
        self.name = name
        self.contribution = int(contribution)

# Program starts here.
def main():

    # Creates global variables that are used throughout the program.
    global party_size
    global party
    global pool

    # Initializes pool to 0.
    pool = 0

    # Initializes a party size.
    party_size = int(input("How many of y'all ain't trynna do 50 different cash-app transfers?\n"))

    # Initializes list of party members.
    party = []
    print(f"{party_size} people... this is gonna be tough. Let's get some names.")

    # Initial party creation loop.
    for i in range(int(party_size)):
        name = input(f"First name of person #{i+1}\n")
        contribution = input(f"How much did {name} contribute?\n")

        name = Friend(name, contribution)
        party.append(name)
        pool += int(contribution)

        print("Alright... on to the next!")

    # Further user interaction lives within 'make_selection()' function.
    make_selection()

    # Exit Message
    print("I hope SplitPy was able to help! Until next time! :D")



# Returns list of party members name and contributions.
def check_contributions():
    for i in range(int(party_size)):
        print(f"{party[i].name} has contributed ${party[i].contribution}.")

# Determines pool $ total.
def get_total():
    print(f"The pool total is ${pool}.")

# Determines total amount owed.
def get_amounts_owed():
    global pool
    pool_average = pool/int(party_size)


    for i in range(int(party_size)):
        curr_contribution = int(party[i].contribution)
        if curr_contribution < pool_average:
            owed_to_pool = pool_average - curr_contribution
            print(f"{party[i].name} owes {owed_to_pool} to the pool.")
        elif curr_contribution > pool_average:
            owed_from_pool = curr_contribution - pool_average
            print(f"{party[i].name} is owed {owed_from_pool} from the pool.")
        else:
            print(f"{party[i].name} is good to go! :D")

# Adds party member.
def add_party_member():
    global pool
    global party
    global party_size

    name = input("Welcome to the party! What's your first name?\n")
    contribution = int(input((f"{name}!! oh my God that's right! Sorry,"
                              f"I'm not good with names. How much did you contribute? :)\n")))
    pool += contribution
    party_size += 1
    name = Friend(name, contribution)
    party.append(name)
    print("Well awesome, glad you could make it!\nParty member added.")

# Adds contribution.
def add_contribution():
    global party_size
    global pool

    new_contribution = int(input("Wow, that was wild! How much did that cost?\n"))
    who_payed = input(f"Who payed?\n")

    for i in range(party_size):
        if who_payed == party[i].name:
            party[i].contribution += new_contribution
        else:
            print(f"{who_payed} is not a member of your party.")

    pool += new_contribution

    print(f"Oh, {party[i].name} covered it?\nContribution updated.")


# Removes party member (takes acount for party member running on the bill/paying their share.)
def remove_party_member():
    global party_size
    global party
    global pool

    removed_member = input("Who left?\n")
    dine_n_dash = input("Did they run away without contributing?\n Enter 'y' for yes or 'n' for no.\n")
    if dine_n_dash == 'y':
        for i in range(party_size):
            if removed_member == party[i].name:
                party.remove(party[i])
                party_size -= 1
                return
            else:
                print(f"{removed_member} is not a member of your party.")

        print(f"Seriously.... why do we invite {removed_member}. Every time. We're going to have to pick up his tab."
              f"\nContributions updated.")
    elif dine_n_dash == "n":
        for i in range(party_size):

            if removed_member == party[i].name:
                difference = (pool/int(party_size) - int(party[i].contribution))
                total_contribution = int(party[i].contribution) + difference
                pool -= total_contribution
                party.remove(party[i])
                party_size -= 1
                return
        print(f"Wish you could've stayed longer {removed_member}. Take care!\nContributions Updated.")





# Python style switch case statement.
def make_selection():

    print("Main Screen: Select an option from the list below...")
    print("----------------------------------------------------")

    making_selection = True

    while making_selection:
        print("\n1. Check contributions.")
        print("2. Current cumulative total $ amount.")
        print("3. Calculate payments.")
        print("4. Add party member.")
        print("5. Add a contribution.")
        print("6. Remove party member.")
        print("q. Enter 'q' to exit.")

        selection = input("\n")

        match selection:
            case "1":
                check_contributions()
            case "2":
                get_total()
            case "3":
                get_amounts_owed()
            case "4":
                add_party_member()
            case "5":
                add_contribution()
            case "6":
                remove_party_member()
            case "q":
                making_selection = False
            case _:
                print("Invalid option.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()