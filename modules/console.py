from colorama import Fore, init
from threading import Lock

init(convert=True)

lock = Lock()

def success(text):
    lock.acquire()
    print(f"         {Fore.LIGHTGREEN_EX}[Success]{Fore.RESET} {Fore.LIGHTBLUE_EX}{text}{Fore.RESET}")
    lock.release()

def error(text):
    lock.acquire()
    print(f"         {Fore.LIGHTRED_EX}[Error]{Fore.RESET} {Fore.LIGHTBLUE_EX}{text}{Fore.RESET}")
    lock.release()

def retrying(text):
    lock.acquire()
    print(f"         {Fore.LIGHTYELLOW_EX}[Retrying]{Fore.RESET} {Fore.LIGHTBLUE_EX}{text}{Fore.RESET}")
    lock.release()

def solved(text):
    lock.acquire()
    print(f"         {Fore.LIGHTMAGENTA_EX}[Solved]{Fore.RESET} {Fore.LIGHTBLUE_EX}{text}{Fore.RESET}")
    lock.release()

def logo():
    print("")
    print(f"""
    {Fore.LIGHTCYAN_EX}

         ██████╗ ████████╗██████╗     ███████╗ ██████╗ ██████╗  ██████╗███████╗██████╗ 
        ██╔═══██╗╚══██╔══╝██╔══██╗    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝██╔══██╗
        ██║   ██║   ██║   ██████╔╝    █████╗  ██║   ██║██████╔╝██║     █████╗  ██████╔╝
        ██║   ██║   ██║   ██╔═══╝     ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  ██╔══██╗
        ╚██████╔╝   ██║   ██║         ██║     ╚██████╔╝██║  ██║╚██████╗███████╗██║  ██║
         ╚═════╝    ╚═╝   ╚═╝         ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝  ╚═╝
    {Fore.RESET}
    """)