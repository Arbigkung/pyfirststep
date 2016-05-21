def greet_user(user):
    """Display a simple greeting."""
    print("Hello! " + user + "!")

greet_user("big")

# Full option
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()

while True:
    print("\nPleasetell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = raw_input("First name: ")
    if f_name == 'q':
        break

    l_name = raw_input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
