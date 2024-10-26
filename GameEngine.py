import ast
from CharacterCreater import CharacterCreation

def CreateCharacter():
    import tkinter as tk
    from tkinter.filedialog import askopenfilename
    tk.Tk().withdraw()

    filepath = askopenfilename()
    CharacterCreation.genCha(filepath)

def CollectCharacters():
    print("Collecting Character Sheets in U_ChaShe364.txt")
    try:
        f = open("U_ChaShe364.txt", "r")
    except:
        f = open("U_ChaShe364.txt", "a")
        f = open("U_ChaShe364.txt", "r")
    text = f.read()
    print(text)
    if text == "":
        import tkinter as tk
        from tkinter.filedialog import askopenfilename
        tk.Tk().withdraw()

        filepath = askopenfilename()
        CharacterCreation.genCha(filepath)

    f = open("U_ChaShe364.txt", "r")
    Chars = f.readlines()
    print("read")
    for i in Chars:
        try:
            temp = ast.literal_eval(i)
            Chars.remove(Chars[0])
            Chars.append(temp)
        except:
            pass
    return Chars

def FIRSTMessage(Chars):
    Length = input("OneShot or Campaign: ")
    Theme = input("Theme: ")
    Characters = CollectCharacters()
    Message = "Create a " + Theme + "themed D&D 5e " + Length + ". There are " + str(len(Chars)) + "characters in this game. Here they are:" + str(Chars)