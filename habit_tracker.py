from datetime import datetime
hobbies=[]
today_hobbies=[]
def load_hobbies():
    with open ("hobbies.txt","r+")as file:
        hobbies = [line.strip() for line in file]
        today_hobbies=hobbies
        
        
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
    print("Please select an action to take from the given options !\n")
    print("1-Mark a hobby as done")
    print("2-Add a new hobby")
    print("3-See the consistency chart of a hobby")
    print("4-Show all hobbies")
    
def all_hobbies():
    print(f"{user}, your all hobbies are :\n")
    for hobby in hobbies:
        print(f"{hobbies[hobby]}")
        
def add_hobby():
    hobby=input("Enter your hobby ")
    hobby=hobby.lower()
    hobbies.append(hobby)
    with open ("hobbies.txt","w") as file:
        file.write(f"{hobby}\n")
    print("New hobby added succesfully !!")

def mark_done():
    all_hobbies()
    option=input("\nWhich hobby would you like to mark as done ? ")
    option=option.lower()
    for hobby in today_hobbies:
        if option==today_hobbies[hobby]:
            index=today_hobbies[hobby].index()
            today_hobbies[index]=f"{today_hobbies[index]} ✅"
            print("Today's updated hobby list is :")
            for hobby in today_hobbies:
                print(today_hobbies[hobby])
            
            

            
#incomplete yet 8/13/25
#hello world
    
    