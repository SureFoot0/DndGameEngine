import ast
from CharacterCreater import CharacterCreation
import openai

def CreateCharacter():
    #Open a tkinter window which will take you to file browser for you to select a character sheet pdf
    import tkinter as tk
    from tkinter.filedialog import askopenfilename
    tk.Tk().withdraw()

    filepath = askopenfilename()
    CharacterCreation.genCha(filepath)

def CollectCharacters():
    """
    Tries to read U_ChaShe364. 
    If it exists, it will read the file.
    If it doesn't, it will create a new file and read the empty one
    """
    print("Collecting Character Sheets in U_ChaShe364.txt")
    try:
        f = open("U_ChaShe364.txt", "r")
    except:
        f = open("U_ChaShe364.txt", "a")
        f = open("U_ChaShe364.txt", "r")
    text = f.read()
    print(text)
    #Recognises an empty file so requests the characters and prepares a U_ChaShe364.txt
    if text == "":
        import tkinter as tk
        from tkinter.filedialog import askopenfilename
        tk.Tk().withdraw()

        filepath = askopenfilename()
        CharacterCreation.genCha(filepath)
    #Opens the not empty character sheet list
    f = open("U_ChaShe364.txt", "r")
    Chars = f.readlines()
    print("read")
    #Replaces string form of character to the appropriate data type
    for i in Chars:
        try:
            temp = ast.literal_eval(i)
            Chars.remove(Chars[0])
            Chars.append(temp)
        except:
            pass
    return Chars

def FIRSTMessage(Chars):
    API_KEY = input("GPT API Key: ")
    Length = input("OneShot or Campaign: ")
    Theme = input("Theme: ")
    Characters = CollectCharacters()
    Message = "Create a " + Theme + "themed D&D 5e " + Length + ". There are " + str(len(Chars)) + "characters in this game. Here they are:" + str(Chars)
    openai.api_key = API_KEY

    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role":"user", "content":Message}
        ]

    )
    assistant_response = response['choices'][0]['message']['content']
    print("Chat-GPT", assistant_response.strip("\n").strip())
