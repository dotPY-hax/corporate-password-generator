from crafter import PasswordCrafter

def cli():
    banner()
    file_path = "/tmp/minirock.txt"
    crafter = PasswordCrafter(file_location=file_path)
    if question("Do you want seasonal passwords? (June2020, Dec_21, etc)"):
        crafter.seasonal_passwords()
    if question("Do you want standard passwords? (Welcome2020, Start_21, etc)"):
        crafter.standard_passwords()
    if question("Do you want weak passwords? (Password123, Batman0 etc)"):
        crafter.weak_passwords()
    if len(crafter.passwords) > 0:
        crafter.write_to_file()
        print("File written to {}".format(file_path))
    else:
        print("No passwords to write :(")
    goodbye()

def question(question):
    possible_answers = ["y", "n"]
    answer = None
    question += str(possible_answers)
    while answer not in possible_answers:
        print(question)
        answer = input(":>").strip().lower()
    if answer == "y":
        return True
    if answer == "n":
        return False

def banner():
    print("Corporate Password Generator by dotPY")
    print("The passwords we see in every security talk")

def goodbye():
    print("Tschau mit au!")


cli()
