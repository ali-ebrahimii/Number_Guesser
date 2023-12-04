
def provide_hint(guess, actual_number):
    """
    Provide a hint based on the difference between guess and actual number
    """
    if guess < actual_number:
        print("Try a higher number!")
    else:
        print("Try a lower number!")
