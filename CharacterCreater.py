from fillpdf import fillpdfs
import re

class CharacterCreation():

    def genCha(filepath):
        x = fillpdfs.get_form_fields(filepath)

        character_sheet = {
            "Name": x["CharacterName"],
            "Race": x["Race "],
            "Class": re.findall(r'[a-zA-Z]+', x["ClassLevel"])[0],
            "Level": re.findall(r'[0-9]+', x["ClassLevel"])[0],
            "Alignment": x["Alignment"],
            "Max Hitpoints": x["HPMax"],
            "Attributes": {
                "Strength": x["STRmod"],
                "Dexterity": x["DEXmod "],      #must have weird space
                "Constitution": x["CONmod"],
                "Intelligence": x["INTmod"],
                "Wisdom": x["WISmod"],
                "Charisma": x["CHamod"],
            },
            "Proficiency Bonus": x["ProfBonus"],
            "Passive Wisdom": x["Passive"],
            "Personality Traits": x["PersonalityTraits "],            #must have weird space
            "Ideals": x["Ideals"],
            "Bonds": x["Bonds"],
            "Flaws": x["Flaws"],
            "Skills": [],
            "Saving Throws": [],
            "Features": x["Features and Traits"].replace(" ", "-").split(),
            "Equipment": (x["Equipment"].replace(" ", "-").split()),
            "Spellcasting Ability": x["SpellcastingAbility 2"],
            "SpellSaveDC": x["SpellSaveDC  2"],                #must have 2 spaces
            "Spell Attack Bonus": x["SpellAtkBonus 2"],
            "Spells Known": [],
            "Character Backstory": ""
        }

        for i in character_sheet["Features"]:
            print(i)
            temp = i.replace("-", " ")
            character_sheet["Features"].remove(character_sheet["Features"][0])
            character_sheet["Features"].append(temp)
        for i in character_sheet["Equipment"]:
            print(i)
            temp = i.replace("-", " ")
            character_sheet["Equipment"].remove(character_sheet["Equipment"][0])
            character_sheet["Equipment"].append(temp)

        SaveSelect = ["Check Box 11", "Check Box 18", "Check Box 19", "Check Box 20", "Check Box 21", "Check Box 22"]
        Saves = {"Check Box 11": "Strength", "Check Box 18":"Dexterity", "Check Box 19":"Constitution", "Check Box 20":"Intelligence", "Check Box 21":"Wisdom", "Check Box 22":"Charisma"}
        for i in SaveSelect:
            if x[i] == "Yes":
                character_sheet["Saving Throws"].append(Saves[i])


        SkillSelect = ['Check Box 23', 'Check Box 24', 'Check Box 25', 'Check Box 26', 'Check Box 27', 'Check Box 28', 'Check Box 29', 'Check Box 30', 'Check Box 31', 'Check Box 32', 'Check Box 33', 'Check Box 34', 'Check Box 35', 'Check Box 36', 'Check Box 37', 'Check Box 38', 'Check Box 39', 'Check Box 40']
        Skills = {'Check Box 23': 'Acrobatics', 'Check Box 24': 'Animal Handling', 'Check Box 25': 'Arcana', 'Check Box 26': "Athletics", 'Check Box 27': 'Deception', 'Check Box 28': 'History', 'Check Box 29': 'Insight', 'Check Box 30': 'Intimidation', 'Check Box 31': 'Investigation', 'Check Box 32': 'Medicine', 'Check Box 33': 'Nature', 'Check Box 34': 'Perception', 'Check Box 35': 'Performance', 'Check Box 36': 'Persuasion', 'Check Box 37': 'Religion', 'Check Box 38': 'Sleight of Hand', 'Check Box 39': 'Stealth', 'Check Box 40': 'Survival'}
        for i in SkillSelect:
            if x[i] == "Yes":
                character_sheet["Skills"].append(Skills[i])
        #"""
        for i in range(14, 1010):
            temp = str("Spells 10"+str(i))
            try:
                if x[temp] != '':
                    character_sheet["Spells Known"].append(x[temp])
            except:
                pass
        #"""

        f = open("U_ChaShe364.txt", "a")
        f.write(str(character_sheet))
        f.write("\n")