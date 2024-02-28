# Capstone Project - Rafdiaufar Hazman
# JCDS - 2302 012

# List Data

dict_student ={
    24001 : ["Alfred", "Class 1", "M"],
    24002 : ["Bella", "Class 2", "F"],
    24003 : ["Charles", "Class 1", "M"],
    24004 : ["David", "Class 3", "M"],
    24005 : ["Elly", "Class 2", "F"],
    24006 : ["Fery", "Class 3", "M"],
    24007 : ["George", "Class 2", "M"],
    24008 : ["Halley", "Class 2", "F"],
    24009 : ["Irene", "Class 1", "F"],
    24010 : ["Jack", "Class 3", "M"]
}

list_subj = ["Physics", "Chemistry", "Biology", "Math", "Language"]

dict_score = {
    24001 : [70, 65, 80, 85, 90],
    24002 : [100, 80, 75, 85, 65],
    24003 : [90, 75, 100, 80, 100],
    24004 : [95, 60, 80, 85, 90],
    24005 : [75, 100, 75, 90, 60],
    24006 : [90, 60, 90, 85, 90],
    24007 : [70, 100, 70, 100, 65],
    24008 : [95, 70, 80, 60, 70],
    24009 : [100, 60, 65, 70, 90],
    24010 : [60, 85, 65, 80, 60]
}

temp_ranking = []

temp_score = []

# ================================================================================================================================
# List Function
# 1. Print Function

def main_menu():
    print()
    print("Student Exam Score\n")
    print("""Main Menu:
    1. Show Students Data
    2. Add New Students Data
    3. Update Students Data
    4. Delete Students Data
    5. Subject Menu
    6. Student Ranking Menu
    7. Exit Program""")

def menu_1():
    print()
    print("Student Data List:")
    print("""1. Select All Students Data
2. Select Specific Student Data
3. Back to Main Menu""")

def menu_2():
    print()
    print("Add New Students Data:")
    print("""1. Add New Student
2. Back to Main Menu""")
    
def menu_3():
    print()
    print("Update Students Data:")
    print("""1. Update Data for Specific Student
2. Back to Main Menu""")

def menu_4():
    print()
    print("Delete Students Data:")
    print("""1. Delete Data for Specific Student
2. Back to Main Menu""")

def menu_5():
    print()
    print("Subject Menu:")
    print("""1. Show Subject List
2. Add New Subject
3. Update Subject
4. Delete Subject
5. Back to Main Menu""")
    
def menu_6():
    print()
    print("Student Ranking Menu:")
    print("""1. Student Overall Ranking
2. Class Ranking
3. Back to Main Menu""")

def menu_3_2():
    print()
    print("Select which column to update : ")

def error_input():
    print("\nERROR : The option you entered is not valid")

def error_no_data():
    print("\nERROR : Data does not exist")

def error_duplicate():
    print("\nERROR : Data already exist")

# 2. Input Function

def input_menu_1():
    while True:
        menu_1()
        try:
            choice_2 = int(input("Input Menu Number To Run : "))
            return choice_2
        except:
            error_input()

def input_menu_1_2():
    if len(dict_student) < 1:
        error_no_data()
    else:
        while True:
            student_index()
            try:
                choice_3 = int(input("Input Student Index : "))
                if choice_3 in dict_student:
                    return choice_3
                else:
                    error_no_data()
            except:
                error_input()

def input_menu_2():
    while True:
        menu_2()
        try:
            choice_4 = int(input("Input Menu Number To Run : "))
            return choice_4
        except:
            error_input()

def input_menu_3():
    while True:
        menu_3()
        try:
            choice_5 = int(input("Input Menu Number To Run : "))
            return choice_5
        except:
            error_input()

def input_menu_3_2():
    while True:
        student_index()
        try:
            choice_6 = int(input("Input Student Index : "))
            if choice_6 in dict_student:
                return choice_6
            else:
                error_no_data()
        except:
            error_input()

def input_menu_4():
    while True:
        menu_4()
        try:
            choice_7 = int(input("Input Menu Number To Run : "))
            return choice_7
        except:
            error_input()

def input_menu_4_2():
    if len(dict_student) < 1:
        error_no_data()
    else:
        while True:
            student_index()
            try:
                choice_8 = int(input("Input Student Index : "))
                if choice_8 in dict_student:
                    return choice_8
                else:
                    error_no_data()
            except:
                error_input()

def input_menu_5():
    while True:
        menu_5()
        try:
            choice_9 = int(input("Input Menu Number To Run : "))
            return choice_9
        except:
            error_input()

def input_menu_6():
    while True:
        menu_6()
        try:
            choice_10 = int(input("Input Menu Number To Run : "))
            return choice_10
        except:
            error_input()

def input_menu_6_2():
    while True:
            choice_11 = input("Input Which Class to Rank : ").capitalize()
            if choice_11 == "Class 1" or choice_11 == "1":
                choice_11 = "Class 1"
                return choice_11
            elif choice_11 == "Class 2" or choice_11 == "2":
                choice_11 = "Class 2"
                return choice_11
            elif choice_11 == "Class 3" or choice_11 == "3":
                choice_11 = "Class 3"
                return choice_11
            else:
                error_input()

# 3. Menu Function

def add_student():
    try:
        choice_4 = int(input("Input Student Index : "))
        if choice_4 in dict_student:
            error_duplicate()
        elif choice_4 < 24001:
            error_input()
            print("Data entered must be higher than 24000")
        else:
            while True:
                name = input("Input Student Name : ").capitalize()
                if name.isalpha() == True:
                    break
                else:
                    error_input()
            while True:
                clas = input(f"Input {name}'s Class (Class 1 - 3): ").capitalize()
                if clas == "Class 1" or clas == "1":
                    clas = "Class 1"
                    break
                elif clas == "Class 2" or clas == "2":
                    clas = "Class 2"
                    break
                elif clas == "Class 3" or clas == "3":
                    clas = "Class 3"
                    break
                else:
                    error_input()
            while True:
                gender = input(f"Input {name}'s Gender (M/F) : ").capitalize()
                if gender == "Male" or gender == "M":
                    gender = "M"
                    break
                elif gender == "Female" or gender == "F":
                    gender = "F"
                    break
            for i in list_subj:
                while True:
                    score = input(f"Input {name}'s {i} exam score : ")
                    if score.isdigit() and int(score) >= 0 and int(score) <= 100:
                        temp_score.append(int(score))
                        break
                    else:
                        error_input()
            dict_student[choice_4] = [name, clas, gender]
            dict_score[choice_4] = temp_score[:]
            print()
            display_index(choice_4)
            while True:
                save = input("Save changes to student data (Y/N) : ").upper()
                if save == "Y":
                    print("Data has been saved")
                    break
                elif save == "N":
                    dict_student.pop(choice_4)
                    dict_score.pop(choice_4)
                    print("Data reverted to last saved data")
                    break
                else:
                    error_input()
            temp_score.clear()

    except:
        error_input()

def update_student(index):
    while True:
        display_index(index)
        print()
        change = input("Input column name to change : ").capitalize()
        if change == "ID" or change == "id" or change == "Id" or change == "iD":
            ori_value = index
            while True:
                try:
                    print()
                    change_2 = int(input("Input New Value : "))
                    if change_2 in dict_student:
                        error_duplicate()
                    elif change_2 < 24001:
                        error_input()
                    else:
                        dict_student[change_2] = dict_student.pop(index)
                        dict_score[change_2] = dict_score.pop(index)
                        display_index(change_2)
                        while True:
                            print()
                            save = input("Save changes to student data (Y/N) : ").upper()
                            if save == "Y":
                                print("Data has been updated")
                                break
                            elif save == "N":
                                dict_student[ori_value] = dict_student.pop(change_2)
                                dict_score[ori_value] = dict_score.pop(change_2)
                                print("Data reverted to last saved data")
                                break
                            else:
                                error_input()
                        break
                except:
                    error_input()
        elif change == "Name":
            ori_value = dict_student[index][0]
            while True:
                print()
                change_2 = (input(f"Input New Value for column {change} : ")).capitalize()
                if change_2.isalpha() == True:
                    dict_student[index][0] = change_2
                    display_index(index)
                    while True:
                        print()
                        save = input("Save changes to student data (Y/N) : ").upper()
                        if save == "Y":
                            print("Data has been updated")
                            break
                        elif save == "N":
                            dict_student[index][0] = ori_value
                            print("Data reverted to last saved data")
                            break
                        else:
                            error_input()
                    break
                else:
                    error_input()
        elif change == "Class":
            ori_value = dict_student[index][1]
            while True:
                print()
                change_2 = (input(f"Input New Value for column {change} (Class 1 - Class 3) : ")).capitalize()
                if change_2 == "Class 1" or change_2 == "1":
                    change_2 = "Class 1"
                    if change_2 == ori_value:
                        print("New Value is the same as Old Value")
                        break
                    else:
                        dict_student[index][1] = change_2
                        display_index(index)
                        while True:
                            print()
                            save = input("Save changes to student data (Y/N) : ").upper()
                            if save == "Y":
                                print("Data has been updated")
                                break
                            elif save == "N":
                                dict_student[index][1] = ori_value
                                print("Data reverted to last saved data")
                                break
                            else:
                                error_input()
                    break
                elif change_2 == "Class 2" or change_2 == "2":
                    change_2 = "Class 2"
                    if change_2 == ori_value:
                        print("New Value is the same as Old Value")
                        break
                    else:
                        dict_student[index][1] = change_2
                        display_index(index)
                        while True:
                            print()
                            save = input("Save changes to student data (Y/N) : ").upper()
                            if save == "Y":
                                print("Data has been updated")
                                break
                            elif save == "N":
                                dict_student[index][1] = ori_value
                                print("Data reverted to last saved data")
                                break
                            else:
                                error_input()
                    break
                elif change_2 == "Class 3" or change_2 == "3":
                    change_2 = "Class 3"
                    if change_2 == ori_value:
                        print("New Value is the same as Old Value")
                        break
                    else:
                        dict_student[index][1] = change_2
                        display_index(index)
                        while True:
                            print()
                            save = input("Save changes to student data (Y/N) : ").upper()
                            if save == "Y":
                                print("Data has been updated")
                                break
                            elif save == "N":
                                dict_student[index][1] = ori_value
                                print("Data reverted to last saved data")
                                break
                            else:
                                error_input()
                    break

                else:
                    error_input()
        elif change == "Gender":
            ori_value = dict_student[index][2]
            while True:
                print()
                change_2 = (input(f"Input New Value for column {change} (M/F): ")).capitalize()
                if change_2 == "Male" or change_2 == "M":
                    change_2 = "M"
                    if change_2 == ori_value:
                        print("New Value is the same as Old Value")
                        break
                    else:
                        dict_student[index][2] = change_2
                        display_index(index)
                        while True:
                            print()
                            save = input("Save changes to student data (Y/N) : ").upper()
                            if save == "Y":
                                print("Data has been updated")
                                break
                            elif save == "N":
                                dict_student[index][2] = ori_value
                                print("Data reverted to last saved data")
                                break
                            else:
                                error_input()
                    break
                elif change_2 == "Female" or change_2 == "F":
                    change_2 = "F"
                    if change_2 == ori_value:
                        print("New Value is the same as Old Value")
                        break
                    else:
                        dict_student[index][2] = change_2
                        display_index(index)
                        while True:
                            print()
                            save = input("Save changes to student data (Y/N) : ").upper()
                            if save == "Y":
                                print("Data has been updated")
                                break
                            elif save == "N":
                                dict_student[index][2] = ori_value
                                print("Data reverted to last saved data")
                                break
                            else:
                                error_input()
                    break
                else:
                    error_input()
        elif change in list_subj:
            for num, subj in enumerate(list_subj):
                if change == subj:
                    ori_value = dict_score[index][num]
                    while True:
                        change_2 = input(f"Input New Value for column {change} (0 - 100) : ")
                        if change_2.isdigit() and int(change_2) >= 0 and int(change_2) <= 100:
                            dict_score[index][num] = int(change_2)
                            display_index(index)
                            while True:
                                print()
                                save = input("Save changes to student data (Y/N) : ").upper()
                                if save == "Y":
                                    print("Data has been updated")
                                    break
                                elif save == "N":
                                    dict_score[index][num] = ori_value
                                    print("Data reverted to last saved data")
                                    break
                                else:
                                    error_input()
                            break
                        else:
                            error_input()
                else:
                    continue
        else:
            error_input()
        while True:
            another = input(f"Do you want to continue changing {dict_student[index][0]} data (Y/N) : ").upper()
            if another == "Y":
                break
            elif another == 'N':
                break
            else:
                error_input()
        if another == "Y":
            continue
        elif another == "N":
            break

def delete_student(index):  
    while True:
        display_index(index)
        delete = input("This student data will be deleted, do you want to proceed (Y/N) : ").upper()
        if delete == "Y":
            dict_student.pop(index)
            dict_score.pop(index)
            print("Data has been deleted")
            break
        elif delete == "N":
            break
        else:
            error_input()


def student_index():
    print()
    print("Students Data : ")
    print("ID    |Name     |Class   |Gender ")
    for key, value in dict_student.items():
        print(f"{key} |{value[0].ljust(9)}|{value[1].ljust(8)}|  {value[2].ljust(5)}")


def student_list():
    if len(dict_student) < 1:
        error_no_data()
    else:
        print()
        print("Student Data")
        print("ID    |Name     |Class   |Gender ", end=" ")
        for i in list_subj:
            print(f"|{i:^10}", end="")
        print()
        for key, value in dict_student.items():
            print(f"{key} |{value[0].ljust(9)}|{value[1].ljust(8)}|  {value[2].ljust(5)}", end=" ")
            for i in range(len(dict_score[key])):
                print(f"|{dict_score[key][i]:^9}", end=" ")
            print()
    
def display_index(x):
    print()
    print("ID    |Name     |Class   |Gender ", end=" ")
    for i in list_subj:
        print(f"|{i:^10}", end="")
    print()
    print(f"{x} |{dict_student[x][0].ljust(9)}|{dict_student[x][1].ljust(8)}|  {dict_student[x][2].ljust(5)}", end=" ")
    for i in range(len(dict_score[x])):
        print(f"|{dict_score[x][i]:^9}", end=" ")
    print()

def display_subject():
    print()
    print("Subject List : ")
    for i in list_subj:
        print(f"|{i:^10}", end="")
    print()

def add_subject():
    print()
    while True:
        display_subject()
        add = input("Input New Subject Name at Maximum of 9 Characters : ").capitalize()
        if add in list_subj:
            error_duplicate()
        elif len(add) > 9 or add.isalpha() == False:
            error_input()
        else:
            list_subj.append(add)
            print()
            display_subject()
            while True:
                save = input("Save changes to Subject List (Y/N) : ").upper()
                if save == "Y":
                    for i in dict_score.keys():
                        dict_score[i].append(0)
                    print("Data has been saved")
                    break
                elif save == "N":
                    list_subj.pop()
                    print("Data reverted to last saved data")
                    break
                else:
                    error_input()
        break
        
def update_subject():
    print()
    while True:
        display_subject()
        update = input("Input Subject Name to Change : ").capitalize()
        if update not in list_subj:
            error_no_data()
        for ind, subj in enumerate(list_subj):
            if subj == update:
                ori_value = subj
                ori_index = ind
                while True:
                    print()
                    update_2 = input("Input New Subject Name at Maximum of 9 Characters : ").capitalize()
                    if update_2 in list_subj:
                        error_duplicate()
                    elif len(update_2) > 9 or update_2.isalpha() == False:
                        error_input()
                    else:
                        list_subj[ori_index] = update_2
                        print()
                        display_subject()
                        while True:
                            save = input("Save changes to Subject List (Y/N) : ").upper()
                            if save == "Y":
                                print("Data has been saved")
                                break
                            elif save == "N":
                                list_subj[ori_index] = ori_value
                                print("Data reverted to last saved data")
                                break
                            else:
                                error_input()
                    break
            else:
                continue
        break

def delete_subject():
    while True:
        display_subject()
        delete = input("Input Subject to Delete : ").capitalize()
        if delete not in list_subj:
            error_no_data()
        for ind, subj in enumerate(list_subj):
            if subj == delete:
                while True:
                    save = input(f"{delete} subject and all of student score for the following subject will be deleted.\nDo you want to proceed (Y/N) : ").upper()
                    if save == "Y":
                        list_subj.pop(ind)
                        for i in dict_score.keys():
                            dict_score[i].pop(ind)
                        print("Data has been deleted")
                        break
                    elif save == "N":
                        break
                    else:
                        error_input()
        break

def overall_rank():
    for key, value in dict_student.items():
        total_score = 0
        for i in range(len(dict_score[key])):
            total_score += dict_score[key][i]
        temp_ranking.append([total_score, key])
    sort_score = sorted(temp_ranking, reverse=True)

    print()
    print("Student Overall Ranking")
    print("ID    |Name     |Class   |Gender ", end=" ")
    for i in list_subj:
        print(f"|{i:^10}", end="")
    x = "Total"
    y = "Ranking"
    print(f"|{x:^10}|{y:^10}", end="")
    print()

    for index, (value, key) in enumerate(sort_score):
        print(f"{key} ", end="")
        print(f"|{dict_student[key][0].ljust(9)}|{dict_student[key][1].ljust(8)}|  {dict_student[key][2].ljust(5)}", end=" ")
        for i in range(len(dict_score[key])):
            print(f"|{dict_score[key][i]:^9}", end=" ")
        print(f"|{value:^9} |{(index+1):^9}", end="")
        print()
    temp_ranking.clear()

def class_rank(clas):
    for key, value in dict_student.items():
        total_score = 0
        if value[1] == clas:
            for i in range(len(dict_score[key])):
                total_score += dict_score[key][i]
            temp_ranking.append([total_score, key])
    sort_score = sorted(temp_ranking, reverse=True)

    print()
    print("Student Class Ranking")
    print("ID    |Name     |Class   |Gender ", end=" ")
    for i in list_subj:
        print(f"|{i:^10}", end="")
    x = "Total"
    y = "Ranking"
    print(f"|{x:^10}|{y:^10}", end="")
    print()

    for index, (value, key) in enumerate(sort_score):
        if dict_student[key][1] == clas:
            print(f"{key} ", end="")
            print(f"|{dict_student[key][0].ljust(9)}|{dict_student[key][1].ljust(8)}|  {dict_student[key][2].ljust(5)}", end=" ")
            for i in range(len(dict_score[key])):
                print(f"|{dict_score[key][i]:^9}", end=" ")
            print(f"|{value:^9} |{(index+1):^9}", end="")
            print()
        else: 
            continue
    temp_ranking.clear()


# ====================================================================================

while True:
    main_menu()

    try:
        choice_1 = int(input("Input Menu Number To Run : "))
        if choice_1 == 1:
            while True:
                choice_2 = input_menu_1()
                if choice_2 == 1:
                    student_list()
                elif choice_2 == 2:
                    choice_3 = input_menu_1_2()
                    if len(dict_student) < 1:
                        continue
                    else:
                        display_index(choice_3)
                elif choice_2 == 3:
                    break
                else:
                    error_input()

        elif choice_1 == 2:
            while True:
                choice_4 = input_menu_2()
                if choice_4 == 1:
                    add_student()
                elif choice_4 == 2:
                    break
                else:
                    error_input()

        elif choice_1 == 3:
            while True:
                choice_5 = input_menu_3()
                if choice_5 == 1:
                    choice_6 = input_menu_3_2()
                    update_student(choice_6)
                elif choice_5 == 2:
                    break
                else:
                    error_input()
        elif choice_1 == 4:
            while True:
                choice_7 = input_menu_4()
                if choice_7 == 1:
                    choice_8 = input_menu_4_2()
                    if len(dict_student) < 1:
                        continue
                    else:
                        delete_student(choice_8)
                elif choice_7 == 2:
                    break
                else:
                    error_input()
        elif choice_1 == 5:
            while True:
                choice_9 = input_menu_5()
                if choice_9 == 1:
                    if len(list_subj) < 1:
                        error_no_data()
                        continue
                    else:
                        display_subject()
                elif choice_9 == 2:
                    add_subject()
                elif choice_9 == 3:
                    update_subject()
                elif choice_9 == 4:
                    if len(list_subj) < 1:
                        error_no_data()
                        continue
                    else:
                        delete_subject()
                elif choice_9 == 5:
                    break
                else:
                    error_input()
        elif choice_1 == 6:
            while True:
                choice_10 = input_menu_6()
                if choice_10 == 1:
                    overall_rank()
                elif choice_10 == 2:
                    choice_11 = input_menu_6_2()
                    class_rank(choice_11)
                elif choice_10 == 3:
                    break
                else:
                    error_input()
        elif choice_1 == 7:
            print("Quitting Program")
            break
        else:
            error_input()
    except:
        error_input()