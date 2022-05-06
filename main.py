from colorama import *
import webbrowser
init()

print(Fore.RED + "What do you want to open?")
print(Fore.BLUE + "[D] Google Docs")
print(Fore.GREEN + "[S] Google Sheets")
print(Fore.YELLOW + "[L] Google Slides")
print("-------------Other Services-------------")
print(Fore.YELLOW + "[G] Google Drive")
print(Fore.RED + "[M] Mail")

selection = input("> ")
selection = selection.upper()
if selection == "D":
    print(Fore.GREEN + "Opening Google Docs...")
    webbrowser.open("https://docs.google.com/")
    
elif selection == "S":
    print(Fore.GREEN + "Opening Google Sheets...")
    webbrowser.open("https://docs.google.com/spreadsheets/")
    exit(0)
elif selection == "L":
    print(Fore.GREEN + "Opening Google Slides...")
    webbrowser.open("https://docs.google.com/presentation/")
    exit(0)
elif selection == "G":
    print(Fore.GREEN + "Opening Google Drive...")
    webbrowser.open("https://drive.google.com/")
    exit(0)
elif selection == "M":
    print(Fore.GREEN + "Opening Mail...")
    webbrowser.open("https://mail.google.com/")
    exit(0)
else:
    print(Fore.RED + "Invalid selection")
    exit(0)