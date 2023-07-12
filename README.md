# ToDo

A simple command-line tool designed to help users manage their todo lists. It allows users to add, delete, and view their todo items directly from the terminal.

## Usage

The Todo script provides the following features:

`[item]` - Add new items to the todo list

`-[item number]` - Delete items from the todo list

`help` - Display a help message with available commands

`exit` - Exit the script

Note: When adding or deleting items, the changes are immediately saved to the todo list file.

## Setup

To set up the Todo script, follow these steps:

### Simple

Run `main.py` with python3 in the directory you want to store your todo list.


### Advanced

#### Use the script from anywhere
1. Change the `plan` variable in `main.py` to the absolute path of the file you want to store your todo list.
2. Add main.py to your PATH variable.

#### See your todo list every time you open a terminal

1. Add the following line to your startup file (e.g., .bashrc, .zshrc):
2. `echo "ToDo:"`
3. `cat ~/.plan`

This will display the header "ToDo:" followed by the contents of your todo list file (~/.plan). Save the file and restart your terminal for the changes to take effect.

## Future

This project is no longer being actively developed. However, if you would like to contribute, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the [GPL-3.0](LICENSE.md)
GNU General Public License - see the [LICENSE.md](LICENSE.md) file for details.