import math
import argparse

def incorrect_parameters():
    """
    Print error message and exit program.

    Returns:
    None
    """
    print("Incorrect parameters")
    exit()

def parse_parameters():
    """
    Parse command line arguments.

    Returns:
    dict: parsed parameters
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--type")
    parser.add_argument("--payment", type=float)
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)

    args = parser.parse_args()

    return {
        "--type": args.type,
        "--payment": args.payment,
        "--principal": args.principal,
        "--periods": args.periods,
        "--interest": args.interest
    }

def validate_parameters(parameters):
    """
    Validate input parameters.

    Parameters:
    parameters (dict): input parameters

    Returns:
    None
    """
    if parameters["--type"] not in ["annuity", "diff"]:
        incorrect_parameters()
    if parameters["--interest"] is None:
        incorrect_parameters()
    count = 0
    for value in parameters.values():
        if value is not None:
            count += 1
    if count < 4:
        incorrect_parameters()
    for key, value in parameters.items():
        if key != "--type" and value is not None:
            if value < 0:
                incorrect_parameters()
    if parameters["--type"] == "diff" and parameters["--payment"] is not None:
        incorrect_parameters()

def calc_diff(parameters, interest):
    """
    Calculate differentiated payments.

    Parameters:
    parameters (dict): input parameters
    interest (float): monthly interest rate

    Returns:
    None
    """
    principal = parameters["--principal"]
    periods = parameters["--periods"]
    total_payment = 0

    for month in range(1, periods + 1):
        payment = math.ceil(
            principal / periods +
            interest * (
                principal -
                (principal * (month - 1)) / periods
            )
        )

        total_payment += payment
        print(f"Month {month}: payment is {payment}")

    overpayment = int(total_payment - principal)

    print()
    print(f"Overpayment = {overpayment}")

def calc_annuity(parameters, interest):
    """
    Calculate annuity values.

    Parameters:
    parameters (dict): input parameters
    interest (float): monthly interest rate

    Returns:
    None
    """
    if parameters["--payment"] is None:
        principal = parameters["--principal"]
        periods = parameters["--periods"]

        payment = math.ceil(
            principal *
            (
                interest * math.pow(1 + interest, periods)
            ) /
            (
                math.pow(1 + interest, periods) - 1
            )
        )

        print(f"Your annuity payment = {payment}!")
        overpayment = payment * periods - principal
        print(f"Overpayment = {int(overpayment)}")

    elif parameters["--principal"] is None:
        payment = parameters["--payment"]
        periods = parameters["--periods"]

        principal = payment / (
            (
                interest * math.pow(1 + interest, periods)
            ) /
            (
                math.pow(1 + interest, periods) - 1
            )
        )

        principal = math.floor(principal)
        print(f"Your loan principal = {principal}!")
        overpayment = int(payment * periods - principal)
        print(f"Overpayment = {overpayment}")

    elif parameters["--periods"] is None:
        principal = parameters["--principal"]
        payment = parameters["--payment"]

        periods = math.ceil(
            math.log(
                payment / (payment - interest * principal),
                1 + interest
            )
        )

        years = periods // 12
        months = periods % 12

        if years == 0:
            print(f"It will take {months} months to repay this loan!")
        elif months == 0:
            if years == 1:
                print("It will take 1 year to repay this loan!")
            else:
                print(f"It will take {years} years to repay this loan!")
        else:
            year_text = "year" if years == 1 else "years"
            month_text = "month" if months == 1 else "months"
            print(
                f"It will take {years} {year_text} "
                f"and {months} {month_text} "
                f"to repay this loan!"
            )

        overpayment = int(payment * periods - principal)
        print(f"Overpayment = {overpayment}")

    else:
        incorrect_parameters()

def main():
    """
    Run loan calculator.

    Returns:
    None
    """
    parameters = parse_parameters()
    validate_parameters(parameters)
    interest = parameters["--interest"] / (12 * 100)

    if parameters["--type"] == "diff":
        calc_diff(parameters, interest)
    elif parameters["--type"] == "annuity":
        calc_annuity(parameters, interest)

if __name__ == "__main__":
    main()