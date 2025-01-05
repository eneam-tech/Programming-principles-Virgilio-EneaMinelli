import os
import json

class Virgilio:
    def __init__(self, directory):
        self.directory = directory

        if not os.path.exists(directory):
            print("Inputted directory does not exist. Trying with default directory...")
            #Default directory value. Change if needed.
            directory = "/Users/eneaminelli/Desktop/Development/Python/Enea Minelli - Assignment Programming Principles/Chants"

    class CantoNotFound(ValueError):
        def __init__(self):
            super().__init__("canto_number must be between 1 and 34")

    def check_canto_number(self, canto_number, file_path):
        if type(canto_number) != int:
            print(f"Error while opening {file_path}")
            while type(canto_number) != int:
                try:
                    canto_number = int(input("Choose a new number: "))
                    file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
                except ValueError:
                    print("canto_number must be a int\n")
        return canto_number,file_path

    #1. This method opens the selected canto and saves it into a list
    def read_canto_lines(self, canto_number, strip_lines, num_lines = None):

        
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")

        canto_number, file_path = self.check_canto_number(canto_number, file_path)
        
        if type(canto_number) == int and canto_number > 34:
                try:
                    print(f"Error while opening {file_path}")
                    canto_number = int(input("canto_number must be between 1 and 34\n"))
                    file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
                except self.CantoNotFound as e:
                    print(e)

        
        lines = []

        while type(num_lines) != int: 
            try:
                num_lines = int(input("How many lines do you want to read?\n"))
            except ValueError:
                print("Value is non a number. Select another value.")
        

        #checking if the selected canto exists
        if not os.path.exists(file_path):
            raise ValueError(f"Error while opening {file_path}")
        else:
            with open(file_path, "r", encoding="utf-8") as file:                
                
                for i in range(num_lines):
                    line = file.readline()

                    if strip_lines == True:
                        line = line.strip()
 
                    #if input too high, don't append line and notify user
                    if len(line) == 0:
                        print("\nInputted number higher than verses number.\n")
                        break
                    else:
                        lines.append(line)
                    

        print(lines)

    #2. This method counts the verses in a canto
    def count_verses(self, canto_number):
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")

        canto_number, file_path = self.check_canto_number(canto_number, file_path)

        verses_number = 0

        #checking if the selected canto exists
        if not os.path.exists(file_path):
            raise ValueError(f"Il canto '{canto_number}' non esiste.")
        else:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    verses_number += 1
        print(verses_number)
    
    #3. This method counts the tercets
    def count_tercets(self, canto_number):
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")

        canto_number, file_path = self.check_canto_number(canto_number, file_path)

        verses_number = 0

        #checking if the selected canto exists
        if not os.path.exists(file_path):
            raise ValueError(f"Il canto '{canto_number}' non esiste.")
        else:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    verses_number += 1
        
        #Round number to nearest integer
        tercet_number = verses_number/3
        print(int(tercet_number))

    #4. This method counts the occurencies of a user selected word
    def count_word(self, canto_number):
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        canto_number, file_path = self.check_canto_number(canto_number, file_path)
        words = []

        #checking if the selected canto exists
        if not os.path.exists(file_path):
            raise ValueError(f"Il canto '{canto_number}' non esiste.")
        else:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    line = line.strip()
                    word = line.split(" ")
                    words.extend(word)
        print(words)

        count_word = input("Which word do you want to count the occurrencies?\n")

        print(words.count(count_word))
    
    #5. This method returns the first verse with the selected word
    def get_verse_with_word(self, canto_number, word):
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        canto_number, file_path = self.check_canto_number(canto_number, file_path)

        #checking if the selected canto exists
        if not os.path.exists(file_path):
            raise ValueError(f"Il canto '{canto_number}' non esiste.")
        else:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    if word in line:
                        print(line)
                        break

    #6. This method returns all the verses with the selected word
    def get_verses_with_word(self, canto_number, word):
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        canto_number, file_path = self.check_canto_number(canto_number, file_path)
        
        verses_with_word = []

        #checking if the selected canto exists
        if not os.path.exists(file_path):
            raise ValueError(f"Il canto '{canto_number}' non esiste.")
        else:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    if word in line:
                        verses_with_word.append(line)
        
        for i, item in enumerate(verses_with_word):
            print(f"{i+1} - {item}")

    #7. This method returns the longest verse within the selected canto
    def get_longest_verse(self, canto_number):
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")
        canto_number, file_path = self.check_canto_number(canto_number, file_path)
        lines = []
        line_len = 0
        longest_line = ""

        #checking if the selected canto exists
        if not os.path.exists(file_path):
            raise ValueError(f"Il canto '{canto_number}' non esiste.")
        else:
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file.readlines():
                    line = line.strip()
                    lines.append(line)
        
        for line in lines:
            i = len(line)
            if i > line_len:
                line_len = i
                longest_line = line

        
        print(f"Longest line: {line_len}\n{longest_line}")
        return(longest_line, line_len)

    # 8. This method creates a dictionary with the longest canto
    # and prints it to the terminal
    def get_longest_canto(self):

        canti_list = os.listdir(self.directory)

        longest_canto = {"canto number" : 0, "verses" : 0}

        selected_canto = {"canto number" : 0, "verses" : 0}

        verses_quantity = 0

        canti_count = 0
        for i in canti_list:
            canti_count +=1
            verses_quantity = self.count_verses(canti_count)
            selected_canto = {"canto number" : canti_count, "verses" : verses_quantity}
            if selected_canto["verses"] > longest_canto["verses"]:
                longest_canto["verses"] = selected_canto["verses"]
                longest_canto["canto number"] = selected_canto["canto number"]
        
        print(
            f"The longest canto is number {longest_canto['canto number']} " 
            f"with {longest_canto['verses']} verses."
            )
        
        return(longest_canto)

    #9. This method counts the occurrence of specified words in selected canto
    def count_words(self, canto_number, words):
        file_path = os.path.join(self.directory, f"Canto_{canto_number}.txt")

        canto_number, file_path = self.check_canto_number(canto_number, file_path)

        word_dictionary = {}

        for w in words:
            word_dictionary[w] = 0
        
        if not os.path.exists(file_path):
            raise ValueError(f"Il canto '{canto_number}' non esiste.")
        else:
            with open(file_path, "r", encoding="utf-8") as file:
                for key in word_dictionary.keys():
                    file.seek(0)
                    for line in file:
                        n = line.count(key)
                        word_dictionary[key] += n

        with open(file_path+"_json_dictionary.json", "w", encoding="utf-8") as file:
            json.dump(word_dictionary, file, indent=2)


        print(word_dictionary)
        return(word_dictionary)

    #10. This method creates a list with all the verses in all the 
    #canti inside the selected directory                         
    def get_hell_verses(self):
        canti_list = sorted(os.listdir(self.directory))

        verses_in_hell = []

        for selected_canto in canti_list:
            file_path = os.path.join(self.directory, selected_canto)
            #checking if the selected canto exists
            if not os.path.exists(file_path):
                raise ValueError(f"Il canto '{selected_canto}' non esiste.")
            else:
                with open(file_path, "r", encoding="utf-8") as file:
                    for line in file:
                        verses_in_hell.append(line.strip())

        print(verses_in_hell)
        return(verses_in_hell)    

    #11. this method counts all the verses in the canti
    # in the selected directory     
    def count_hell_verses(self):
        canti_list = sorted(os.listdir(self.directory))

        verses_in_hell = 0

        for selected_canto in canti_list:
            file_path = os.path.join(self.directory, selected_canto)
            #checking if the selected canto exists
            if not os.path.exists(file_path):
                raise ValueError(f"Il canto '{selected_canto}' non esiste.")
            else:
                with open(file_path, "r", encoding="utf-8") as file:
                    for line in file:
                        verses_in_hell += 1
        
        print(verses_in_hell)
        return(verses_in_hell)

    #12. This methos calculates the mean length of all
    # verses in hell
    def get_hell_verse_mean_len(self):
        canti_list = sorted(os.listdir(self.directory))

        verses_in_hell = 0
        char_verses_count = 0

        for selected_canto in canti_list:
            file_path = os.path.join(self.directory, selected_canto)
            #checking if the selected canto exists
            if not os.path.exists(file_path):
                raise ValueError(f"Il canto '{selected_canto}' non esiste.")
            else:
                with open(file_path, "r", encoding="utf-8") as file:
                    for line in file:
                        verses_in_hell += 1
                        char_verses_count += len(line)
        
        mean_verse_len = (char_verses_count/verses_in_hell)

        print(mean_verse_len)
        return(mean_verse_len)


default_canto = Virgilio("/Users/eneaminelli/Desktop/Development/Python/Enea Minelli - Assignment Programming Principles/Chants")

keep_cycle_alive = True

def check_cycle_state(keep_cycle_alive):
    user_input = input("Do you want to perform more operations? Y for yes, N for no.\n")
    if user_input.lower() == "y":
        keep_cycle_alive = True
        print("Choose a new option...\n")
    elif user_input.lower() == "n":
        keep_cycle_alive = False
        print("Ending program.")
    else:
        keep_cycle_alive = True
        print("Wrong input detected, keeping program alive.")
    
    return keep_cycle_alive

while keep_cycle_alive == True:
    user_choice = input("This program allows you to operate on the Canti of divina commedia, if provided with a directory.\n"
        "Choose what you want to do by pressing the number:\n"
        "1. this method allows you read and operate on the lines of a selected canto\n"
        "2. This method counts the verses in a canto\n"
        "3. This method counts the tercets"
        "4. This method counts the occurencies of a user selected word\n"
        "5. This method returns the first verse with the selected word\n"
        "6. This method returns all the verses with the selected word\n"
        "7. This method returns the longest verse within the selected canto\n"
        "8. This method creates a dictionary with the longest canto and prints it to the terminal\n"
        "9. This method counts the occurrence of specified words in selected canto\n"
        "10.This method creates a list with all the verses in all the canti inside the selected directory\n"
        "11.this method counts all the verses in the canti in the selected directory\n"
        "12.12. This methos calculates the mean length of all verses in Hell")

    if user_choice == "1":
        canto_number = input("Which canto you want to read? From 1 to 34.\n")
        strip_lines = input("Do you want to strip lines of characters? Y or 1 for yes, N or 0 for no.\n").lower()
        if strip_lines == "y" or strip_lines == "1":
            strip_lines = True
        elif strip_lines == "n" or strip_lines == "0":
            strip_lines = False
        else:
            print("Wrong input. Stripping lines anyway.\n")
        num_lines = input("How many lines you want to read?\n")
        default_canto.read_canto_lines(canto_number, strip_lines, num_lines)
        keep_cycle_alive = check_cycle_state(keep_cycle_alive)
    elif user_choice == "2":
        canto_number = input("Which canto you want to read? From 1 to 34.\n")
        default_canto.count_verses(canto_number)
        keep_cycle_alive = check_cycle_state(keep_cycle_alive)
    elif user_choice == "3":
        canto_number = input("Which canto you want to read? From 1 to 34.\n")
        default_canto.count_tercets(canto_number)
        keep_cycle_alive = check_cycle_state(keep_cycle_alive)
    elif user_choice == "4":
        canto_number = input("Which canto you want to read? From 1 to 34.\n")
        default_canto.count_word(canto_number)
        keep_cycle_alive = check_cycle_state(keep_cycle_alive)
    elif user_choice == "5":
        canto_number = input("Which canto you want to read? From 1 to 34.\n")
        word = input("Which word you want to look for?\n")
        default_canto.get_verse_with_word(canto_number, word)
        keep_cycle_alive = check_cycle_state(keep_cycle_alive)
    elif user_choice == "6":
        canto_number = input("Which canto you want to read? From 1 to 34.\n")
        word = input("Which word you want to look for?\n")
        default_canto.get_verses_with_word(canto_number, word)
        keep_cycle_alive = check_cycle_state(keep_cycle_alive)
    elif user_choice== "7":
        canto_number = input("Which canto you want to read? From 1 to 34.\n")
        default_canto.get_longest_verse(canto_number)
        keep_cycle_alive = check_cycle_state(keep_cycle_alive)
    elif user_choice == "8":
        default_canto.get_longest_canto()
        keep_cycle_alive = check_cycle_state(keep_cycle_alive)
    elif user_choice == "9":
        canto_number = input("Which canto you want to read? From 1 to 34.\n")
        words = []
        user_adding = True
        while user_adding == True:
            word = input("which word you want to add?")
            words.append(word)
            if input("Do you want to keep adding? Y for yes, N for no\n").lower() == "n":
                user_adding = False
            elif input("Do you want to keep adding? Y for yes, N for no\n").lower() == "y":
                print("Add another word.\n")
            else:
                print("Wrong input, keep adding.\n")
        default_canto.count_words(canto_number, words)
        keep_cycle_alive = check_cycle_state(keep_cycle_alive)
    elif user_choice == "10":
        default_canto.get_hell_verses()
        keep_cycle_alive = check_cycle_state(keep_cycle_alive)
    elif user_choice == "11":
        default_canto.count_hell_verses()
        keep_cycle_alive = check_cycle_state(keep_cycle_alive)
    elif user_choice == "12":
        default_canto.get_hell_verse_mean_len()
        keep_cycle_alive = check_cycle_state(keep_cycle_alive)