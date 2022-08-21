import os

os.system("pip install pyarmor")
os.system("cls")

kuy = 'pyarmor pack -e" --onefile" '
hee = 'pyarmor o '


funcion = input(f"""

    [1] Pyarmor to EXE Obf

    [2] Pyarmor to py Obf

 >>> : """)

if funcion == "1":
    name = input("Location File >>> : ")

    os.system(f"{kuy}{name}")

elif funcion == "2":
    mk = input("Location File >>> : ")

    os.system(f"{hee}{mk}")



