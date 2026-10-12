from pathlib import Path
import requests

nickname = []
cicl = True
while cicl:
    print("***********************************************")
    opros = input("*enter name for check (q for quit, / for start)*\n***********************************************\n")
    nickname.append(opros)
    if opros == "q":
        cicl = False
    elif opros == "/":
        cicl = False
        nickname.pop()
        for n in nickname:
            path = Path("found.txt")
            url = f"https://t.me/{n}"
            responde = requests.get(url)
            if len(n) < 5:
                print("тг ники минимум 5 символов")
            elif " " in n:
                print("пробелы в нике уберите")
            elif responde.status_code == 200:
                if "Contact" in responde.text:
                    print(f"[FREE] {n}")
                    with open(path, "a") as f:
                        f.write(f"{n}\n")
                else:
                    print(f"[TAKEN] {n}")
            else:
                print(f"[ERROR] {responde.status_code}")
