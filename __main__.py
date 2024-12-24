# !/usr/bin/python

import time, os
import json
import subprocess
from prettytable import PrettyTable
from configparser import ConfigParser
from getpass import getpass

# Define
table = PrettyTable()
cfg = ConfigParser()

# Call: banner
def banner(program) -> None:
    # Clear Screen
    match os.name:
        case 'posix':
            subprocess.run('clear')
        case 'nt':
            subprocess.run('cls')
            
    progam_name: str = f"\033[93m{program}"
    print(f"""
\033[93m .d88b.   d888b     \033[00mName: Quiz Games
\033[93m.8P  Y8. 88' Y8b    \033[00mVersion: \033[93mv.Demo
\033[93m88    88 88         \033[00mAuthor: @tomsdroid
\033[93m88    88 88  ooo    \033[00mRepo: tomsdroid/quizGames
\033[93m`8P  d8' 88.  8~
\033[93m `Y88 Y8  Y888P     \033[92mCodeBlues ID Community
\033[00m{'-' * 15}| {progam_name} \033[00m|{'-' * 15}""")

# Call: loginQuiz
def loginQuiz() -> None:
    banner('Login Forms')
    
    cfg.read('.users.cfg')
    username: str = cfg['USERS']['username']
    passwd: str = cfg['USERS']['password']
    
    u_name = print(f"Username: {username}")
    password = getpass("Password: ")
    
    # Validate Data
    if password != passwd:
        print(f"\033[93mWARNING\033[00m Username atau Password Salah!")
        time.sleep(1)
        loginQuiz()
    else:
        time.sleep(0.50)
        print(f"\033[92mSuccess\033[00m Anda tidak akan diminta untuk login lagi!")
        with open('.users.cfg', 'r') as f:
            ck = f.read()
            if "True" not in ck:
                with open(".users.cfg", "w") as f:
                    cf = ck.replace("False", "True")
                    f.write(f"{cf}")
                time.sleep(1.5)
                main()
            else:
                main()
        

# Call: registQuiz
def registQuiz() -> None:
    banner("Regist Forms")
    # Ambil input user
    print(f"\033[93mWARNING\033[00m Kayaknya belum ada data deh...\n")
    u_name = input("Username: ")
    passwd = getpass("Password: ")
    
    cfg['USERS'] = {}
    cfg['USERS']['username']: str = u_name
    cfg['USERS']['password']: str = passwd
    cfg['USERS']['isLogin']: str = "False"
    
    # Process Data
    with open('.users.cfg', 'w') as fileCfg:
        cfg.write(fileCfg)
    
    time.sleep(0.9)
    loginQuiz()
    
# Call: main
def main() -> None:
    banner('Quiz Games')
    with open("questions.json",'r') as ctx:
        idx: int = 0
        opts: list[str] = ['A','B','C','D']
        data = json.load(ctx)
        for soal in data:
            idx += 1
            print(f"\n{idx}. {soal['questions']}")
            for i in range(0,4):
                print(f"   {opts[i]}. {soal['options'][i]}")
                time.sleep(0.10)
            time.sleep(0.5)
            u_choices = input("\n   Jawaban Anda: ").upper()
            
            table.field_names = ["No","JAWABAN ANDA", "JAWABAN BENAR"]
            table.add_row([idx, u_choices, soal['correct']])
            print(table)


if __name__ == '__main__':
    file: str = ".users.cfg"
    fileScan: os = os.listdir()
    if file not in fileScan:
        registQuiz()
    else:
        cfg.read(file)
        if cfg['USERS']['isLogin'] == True:
            loginQuiz()
        else:
            main()
