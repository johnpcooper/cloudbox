import pyperclip

def load_clipboard(string):
    """
    Add the string passed to load_clipboard
    to the system clipboard

    pyperclip uses OS-respective 
    OS commands and seems portable across
    different systems 
    """

    if type(string) == str:
        pyperclip.copy(string)
    else:
        print("not a string")