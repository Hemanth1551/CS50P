#     University Student Information System (USIS)

import pandas as pd
from prettytable import PrettyTable
data = pd.read_csv("student.csv")

year_list = {20:2020, 21:2021, 22:2022, 23:2023, 24:2024}
clg_id_list = {"L1":"clg1", "L2":"clg2","L3":"clg3","L4":"clg4"}
branch_list = {101:"CSE", 102:"AIML", 102:"AIDS", 103:"EEE", 104:"ECE"}

# we create 3 funtions
# stu_on_uni()
# clg_on_uni()
# brch_on_uni()

df_id = data["stu_id"]
df_name = data["stu_name"]
df_clg = data["stu_clg"]
df_brch = data["stu_brch"]
df_year = data["stu_year"]
#print(data['stu_id'])

stu_ids = df_id.values.tolist()
stu_names = df_name.values.tolist()
stu_clgs = df_clg.values.tolist()
stu_brchs = df_brch.values.tolist()
stu_years = df_year.values.tolist()

def main():
    try:
        while(True):
            print("\n1. If Student Was In university")
            print("2. Search Students By Collage Id")
            print("3. Search Students By Branch")
            user_data = int(input("Select any operation : "))

            match user_data:
                case 1:
                    id = input("\nEnter Student Hall Ticket No : ")
                    user = stu_on_uni(id)
                    mytable = PrettyTable(["Student Id","Student Name","Year","Collage","Branch","Roll Id"])
                    mytable.add_row(user)
                    print(mytable)
                case 2:
                    id1 = input("\nEnter Collage Id : ")
                    ids,names = clg_on_uni(id1)
                    if(ids == 1):
                        print("\nCollage Was Not Assocciated With University\n")
                    else:
                        mytable = PrettyTable(["Roll Id","Student Name",])
                        text = []
                        for i in range(0,len(ids)):
                            text.append(ids[i])
                            text.append(names[i])
                            mytable.add_row(text)
                            text.clear()
                        print(mytable)
                case 3:
                    id2 = int(input("\nEnter Branch Id : "))
                    ids,clgs = brch_on_uni(id2)
                    if(ids == 1):
                        print("\nBranch Was Not Assocciated With University\n")
                    else:
                        mytable = PrettyTable(["Roll Id","Collage Id",])
                        text = []
                        for i in range(0,len(ids)):
                            text.append(ids[i])
                            text.append(clgs[i])
                            mytable.add_row(text)
                            text.clear()
                        print(mytable)
                case _:
                    print("try again...!")
    except:
        print("\ntry again...!\n")

def stu_on_uni(id):
    year = id[0:2]
    clg = id[2:4]
    brch = id[4:7]
    roll = id[7:10]

    roll = int(roll)
    brch = int(brch)
    year = int(year)

    count = 0
    if(roll in stu_ids):
        row_id = stu_ids.index(roll)
        count = count+1
    else:
        print("Id Was Not Present")
    if(clg in stu_clgs):
        row_clg = stu_clgs.index(clg)
        if(row_id == row_clg):
            count = count+1
        else:
            print("Collage Was Not Present")
    if(brch in stu_brchs):
        row_brch = stu_brchs.index(brch)
        if(row_id == row_brch):
            count = count+1
        else:
            print("Branch Was Not Present")
    if(year in stu_years):
        row_year = stu_years.index(year)
        if(row_id == row_year):
            count = count+1
        else:
            print("Year Was Not present")
#print(count)

    if(count == 4):
        print("\nStudent Was Present In University\n")
        text = [id,stu_names[row_id],year_list[year],clg_id_list[clg],branch_list[brch],roll]
        return text
    else:
        print("\n")
        return "Student Was not Present In University"


def clg_on_uni(dd):
    stu_ids = data["stu_id"].values.tolist()
    stu_names = data["stu_name"].values.tolist()
    stu_clgs = data["stu_clg"].values.tolist()

    if dd in stu_clgs:
        print("College Was Associated With University")
        ids = []
        names = []
        for i in range(len(stu_clgs)):
            if stu_clgs[i] == dd:
                ids.append(stu_ids[i])
                names.append(stu_names[i])
        return ids, names
    else:
        return "College Was Not Associated With University"

def brch_on_uni(id2):
    if id2 in stu_brchs:
        print("\nBranch Was Associated With University\n")
        ids = []
        clgs = []
        for i in range(len(stu_brchs)):
            if stu_brchs[i] == id2:
                ids.append(stu_ids[i])
                clgs.append(stu_clgs[i])
        return ids, clgs
    else:
        return 1, 0

if __name__ == "__main__":
    main()
