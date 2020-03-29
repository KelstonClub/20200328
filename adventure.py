def analyse_command(command):
    verb, noun = command.split()
    return verb, noun

def get_command():
    """Return verb, noun as uppercase
    """
    command = input("What now? ").upper()
    return analyse_command(command)

def act_on_command(verb, noun):
    print("I am about to", verb, "the", noun)

def move_actors():
    print("I'm doing nothing...")

while True:
    verb, noun = get_command()
    act_on_command(verb, noun)
    move_actors()