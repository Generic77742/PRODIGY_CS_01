from colorama import Fore, Back, Style
import time

time.sleep(1)
print('''
██████╗░███████╗░█████╗░  ░█████╗░██████╗░██╗░░░██╗██████╗░████████╗
██╔══██╗██╔════╝██╔══██╗  ██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝
██║░░██║█████╗░░██║░░╚═╝  ██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░
██║░░██║██╔══╝░░██║░░██╗  ██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░
██████╔╝███████╗╚█████╔╝  ╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░
╚═════╝░╚══════╝░╚════╝░  ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░
                                           ↊ߤ𝘓𝘓𝘓 ɔᴉɹǝuǝ⅁ ʎꓭ                ''')
time.sleep(2)

with open('data.txt', 'r') as file:
    file_content = file.read().strip()
    alphabet = file_content.split(',')

def encodeText(text,choice,shift,operator):
    userText = text
    userShift = shift
    userOperator = operator
    userChoice = choice
    userChoice = choice.lower()
    new = []
    output = []
    for i in userText:
        new.append(i)
    
    for i in range(0,len(new)):
        for j in range(0,len(alphabet)):
            if new[i] == alphabet[j]:
                if userOperator == "+":
                    output.append(alphabet[j+userShift])
                elif userOperator == "-":
                    output.append(alphabet[j-userShift])
                else:
                    print(Fore.RED+"Invalid Operator Used ! Try Again"+Fore.RESET)

    
    result = "".join(output)

    if userChoice == "e":
        print(Fore.GREEN+(f"\nEncoded Output => {result}\n")+Fore.RESET)
        with open ('outputs.txt','a') as file:
            file.write(f"Input => {userinput} and Encoded text => {result}\n")
    elif userChoice == "d":
        print(Fore.GREEN+(f"\nDecoded Output => {result}\n")+Fore.RESET)
        with open ('outputs.txt','a') as file:
            file.write(f"Input => {userinput} and Decoded text => {result}\n")
    else:
        print(Fore.RED+"Invalid Option Selected! Try Again"+Fore.RESET)

userinput = input(Fore.YELLOW+ "\nEnter the Text : "+Fore.RESET)
userchoice = input("\nPress E to Encode or D to Decode : ")
usershift = int(input("\nEnter the Number of Shifts : "))
useroperator = input("\nEnter the Operator '+' or '-' : ")

encodeText(userinput,userchoice,usershift,useroperator)