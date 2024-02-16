'''LOGIN PAGE USING JSON'''
'''GOING GOOD'''
import json
file='login.json'

def isthere():
    try:
        with open(file) as f:
            fi=json.load(f)
    except:
        return None
    else:
        return fi
    
def new_user(name, password):
    y={}
    fi={}
    with open(file, 'r') as f:
        fi=json.load(f)
        y=fi
    with open(file, 'w') as f:
        x={name:password}
        y.update(x)
        json.dump(y, f)
    print("\t\nYOU ARE SUCCESSFULY SIGNED UP!!\nNEXT TIME, YOU JUST NEED TO LOGIN USING YOUR USERNAME AND PASSWORD\t\n")
def check(name, password):
    fi={}
    with open(file) as f:
        fi=json.load(f)
    while True:
        if name in fi.keys():
            print("Username confirmed\n")
            if fi[name]==password:
                print("Password confirmed\n")
                
            else:
                print("Wrong password, try again\n")
                login(name, password, value='password')
            break
        else:
            print("Wrong username, try again\n")
            login(name, password, value='name')
            break
            
def login(name, password, value='checking'):
    if value=='password':
        while True:
            answer=input("Are you sure you are already signed up? answer 'yes' for yes and 'no' for no\n")
            if answer.lower()=='yes':
                password=input('Enter the correct password\n')
                check(name, password)
                break
            elif answer.lower()=='no':
                signup()
                break
            else:
                print("wrong key\n")
    elif value=='name':
        answer=input("Are you sure you are already signed up? answer 'yes' for yes and 'no' for no\n")
        if answer.lower()=='yes':
            name=input('Enter the correct username\n')
            check(name, password)
    else:
        check(name, password)
 
    
def signup():
    print("Ok, let's get you signed up\n")
    name=input('What is your name sir/madam?\n')
    password=input('Enter your password:\n')
    new_user(name, password)
    
def homepage():
    i=isthere()
    if i:
        num=input('1. Log in\n2. Sign in\n')
        if num=='1':
            name=input('What is your name sir/madam?\n')
            password=input('Enter your password:\n')
            login(name, password)
        elif num=='2':
            signup()
        else:
            print('Wrong input\n')
            homepage()
    else:
        print("\n****Looks like you are the first one to sign up\n")
        print("****Ok, let's get you digned up\n")
        name=input('What is your name sir/madam?\n')
        password=input('Enter your password:\n')
        new_user(name, password)
        
if __name__=='__main__':
    homepage() 