from datetime import datetime 
import matplotlib.pyplot as plt

hobbies=[]
today_hobbies=[]

def load_hobbies():
    global hobbies, today_hobbies
    try:
        with open("hobbies.txt","r+") as file:
            hobbies = [line.strip() for line in file if line.strip()]
            today_hobbies = hobbies.copy()
    except FileNotFoundError:
        print("No hobbies file found. Starting fresh.")
        hobbies = []
        today_hobbies = []

def greet():
        now = datetime.now()      
        global today
        today = now.date()   
        print(f"\n{today}\n")
        global user
        user=input("Enter your name ! ")
        words=user.split()
        if len(words)>=2:
            
            words[0]=words[0].capitalize()
            words[1]=words[1].capitalize()
            user=words[0]+" "+words[1]
        else:
            user=user.capitalize()

        print(f"Hello {user},have a nice day !")
        
def menu():
    print("===MENU===")
    print("Please select an action to take from the given options !")
    print("1-Mark a hobby as done")
    print("2-Add a new hobby")
    print("3-Show today's hobby status")
    print("4-See the consistency chart of a hobby")
    print("5-Show all hobbies")
    print("6-Delete a hobby")
    print("7-Exit")
    
def show_all_hobbies():
    print(f"{user}, your all hobbies are :\n")
    if not hobbies:
        print("No hobbies found yet!")
    for idx, hobby in enumerate(hobbies, start=1):
        print(f"{idx}. {hobby}")
        
def add_hobby():
    global hobbies, today_hobbies
    hobby=input("Enter your hobby ")
    hobby=hobby.lower()
    if hobby and hobby not in hobbies:
        hobbies.append(hobby)
        today_hobbies.append(hobby)
        with open("hobbies.txt","a") as file:
            file.write(f"{hobby}\n")
        print("New hobby added succesfully !!")
    else:
        print("Invalid or duplicate hobby.")

def delete_hobby():
    global hobbies, today_hobbies
    show_all_hobbies()
    option=input("\nEnter the number of the hobby you want to delete: ")
    if option.isdigit():
        option = int(option)
        if 1 <= option <= len(hobbies):
            removed = hobbies.pop(option-1)
            today_hobbies = [h for h in today_hobbies if h.lower().replace(" ✅", "") != removed.lower()]
            with open("hobbies.txt","w") as file:
                for h in hobbies:
                    file.write(f"{h}\n")
            print(f"Hobby '{removed}' deleted successfully!")
        else:
            print("Invalid hobby number.")
    else:
        print("Please enter a valid number.")

def mark_done():
    global today_hobbies
    show_all_hobbies()
    option=input("\nEnter the number of the hobby you want to mark as done: ")
    if option.isdigit():
        option = int(option)
        if 1 <= option <= len(today_hobbies):
            hobby = today_hobbies[option-1]
            if "✅" not in hobby:
                today_hobbies[option-1] = f"{hobby} ✅"
                with open("progress.txt","a") as pfile:
                    pfile.write(f"{today},{hobby.lower()}\n")
            print("Today's updated hobby list is :")
            for h in today_hobbies:
                print(h if "✅" in h else f"{h} ❌")
        else:
            print("Invalid hobby number.")
    else:
        print("Please enter a valid number.")

def show_today_status():
    print(f"\n{user}, today's hobby status:\n")
    for hobby in today_hobbies:
        if "✅" in hobby:
            print(hobby)
        else:
            print(f"{hobby} ❌")

def show_chart():
    try:
        hobby_count = {hobby: 0 for hobby in hobbies}

        try:
            with open("progress.txt","r") as file:
                data = [line.strip().split(",") for line in file if line.strip()]
            for entry in data:
                if len(entry) == 2:
                    _, hobby = entry
                    hobby_clean = hobby.replace(" ✅", "").strip().lower()
                    if hobby_clean in hobby_count:
                        hobby_count[hobby_clean] += 1
        except FileNotFoundError:
            pass  

        plt.bar(hobby_count.keys(), hobby_count.values(), color="skyblue")
        plt.title("Habit Consistency Chart")
        plt.xlabel("Hobbies")
        plt.ylabel("Days Completed")
        plt.show()

    except Exception as e:
        print(f"Error showing chart: {e}")


if __name__ == "__main__":
    load_hobbies()
    greet()
    while True:
        menu()
        choice=input("\nEnter your choice: ")
        if choice=="1":
            mark_done()
        elif choice=="2":
            add_hobby()
        elif choice=="3":
            show_today_status()
        elif choice=="4":
            show_chart()
        elif choice=="5":
            show_all_hobbies()
        elif choice=="6":
            delete_hobby()
        elif choice=="7":
            print("Goodbye ! Have a nice day :)")
            break
        else:
            print("Invalid choice, please try again.")
    print("===MENU===")
    print("Please select an action to take from the given options !")
    print("1-Mark a hobby as done")
    print("2-Add a new hobby")
    print("3-Show today's hobby status")
    print("4-See the consistency chart of a hobby")
    print("5-Show all hobbies")
    print("6-Delete a hobby")
    print("7-Exit")