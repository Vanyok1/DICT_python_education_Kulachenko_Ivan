import random

def get_friends_list(num_friends):
    """
    Create a dictionary of friends with initial share value 0.

    Parameters:
        num_friends (int): Number of friends including the user.

    Returns:
        dict: Dictionary where each key is a friend's name and value is 0.
    """
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num_friends):
        name = input()
        friends[name] = 0
    return friends

def split_amount_evenly(friends, total_amount):
    """
    Evenly split the total amount between all friends.

    Parameters:
        friends (dict): Dictionary of friends.
        total_amount (int): Total bill amount.

    Returns:
        dict: Updated dictionary with equal share assigned to each friend.
    """
    share = round(total_amount / len(friends), 2)
    for name in friends:
        friends[name] = share
    return friends

def apply_lucky_feature(friends, total_amount):
    """
    Apply the 'Who is lucky?' feature that selects one random friend
    who will pay 0, while the others split the total amount.

    Parameters:
        friends (dict): Dictionary of friends and their shares.
        total_amount (int): Total bill amount.

    Returns:
        dict: Updated dictionary with one friend having 0
              and others paying increased share.
    """
    answer = input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')

    if answer == "Yes":
        lucky = random.choice(list(friends.keys()))
        print(f"{lucky} is the lucky one!")

        new_share = round(total_amount / (len(friends) - 1), 2)
        for name in friends:
            friends[name] = 0 if name == lucky else new_share

        return friends

    print("No one is going to be lucky")
    return friends

def main():
    """
    Main program function that reads user input, collects friends,
    splits the bill evenly, applies lucky feature, and prints result.

    Parameters:
        None

    Returns:
        None
    """
    num_friends = int(input("Enter the number of friends joining (including you):\n"))

    if num_friends <= 0:
        print("No one is joining for the party")
        return

    friends = get_friends_list(num_friends)
    total_amount = int(input("Enter the total amount:\n"))

    friends = split_amount_evenly(friends, total_amount)
    friends = apply_lucky_feature(friends, total_amount)

    print(friends)

main()