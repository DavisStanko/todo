import os
import sys

plan = f"{os.path.expanduser('~')}/.plan"

helpmessage = f"""Inputs:
\thelp
\t\tShow this help message\n
\t-[line number]
\t\tDelete the given line number from {plan}
\t\t\tThis runs [sed -i '[INPUT]d' {plan}] so if you are familiar with sed you can delete in other ways!
\t\t\tVisit https://www.gnu.org/software/sed/manual/sed.html for more information
\t[input]
\t\tAppend the given input to {plan}\n
\texit
\t\tExit the program"""

# Create the default file if it doesn't exist
try:
    with open(plan, 'x') as f:
        f.write()
except FileExistsError:
    pass


def main():
    print("ToDo:")
    os.system(f"cat -n {plan}")
    inp = input("\x1b[1;34m[ToDo]$ \x1b[0m")  # Prompt for input. Color is set to blue.

    # Exit
    if inp == "exit":
        sys.exit("Bye!")

    # Check if user wants help
    if inp == "help":
        print(helpmessage)
        main()

    # Delete a line from the plan
    if inp.startswith("-"):
        inp = inp.replace("-", "")
        print(f"sed -i '{inp}d' {plan}\n")
        os.system(f"sed -i '{inp}d' {plan}")

    # Append to the plan
    else:
        print(f"echo {inp} >> {plan}\n")
        os.system(f"echo {inp} >> {plan}")
    main()


main()
