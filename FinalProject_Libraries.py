import random
import xlsxwriter
import string
import pandas as pd
from datetime import datetime
from datetime import timedelta

def randomString(stringLength=8):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#---Method for sign in
def signIn(df):
    try:
        print("Enter name: ")
        name = input()
        print("Enter password: ")
        pwd = input()
        df1 = df[df['Username'] == name]
        if df1.empty:
            print("\nIncorrect Username entered!")
            quit()
        for i in df1.index:
            df1_username = df['Username'][i]
            # print(df['Username'][i])
        for i in df1.index:
            df1_pwd = df['Password'][i]
            # print(df['Password'][i])
        if (name == df1_username and pwd == df1_pwd):
            print("Login successful")
            print('Your To do list')
            print('------------------------------')

            df_ToDo = pd.read_excel(name + '.xlsx', index_col=0)
            if not (df_ToDo.empty):
                print(df_ToDo)
            else:
                print('There are no items in the to do list')
            print('------------------------------')
            print('1 - Create new entry\n2 - Exit\n')
            accept_option = int(input())
            if (accept_option == 1):
                print("Enter title")
                title = input()
                print('Enter description')
                desc = input()
                date_of_creation = datetime.today()
                print('Enter deadline in days')
                days_deadline = input()
                print('Enter deadline in hours')
                hrs = input()
                deadline = datetime.today() + timedelta(days=int(days_deadline)) + timedelta(hours=int(hrs))
                # ---------------------------------
                if df_ToDo.empty:
                    df_newTodo = pd.DataFrame([[title, desc, date_of_creation, deadline]],
                                              index=['1'], columns=['Title', 'Description', 'Date of creation', 'Deadline'])
                    df_newTodo.to_excel(name + '.xlsx', sheet_name=name + 'TODO')
                else:
                    df_append_Todo = pd.DataFrame([[title, desc, date_of_creation, deadline]], index=[len(df_ToDo) + 1],
                                                  columns=['Title', 'Description', 'Date of creation', 'Deadline'])
                    df_new_Todo = df_ToDo.append(df_append_Todo)
                    # print(df_new_Todo)
                    df_new_Todo.to_excel(name + '.xlsx', index=True, header=True)
                print("To do item added successfully and your updated To do list")
                df_ToDo = pd.read_excel(name + '.xlsx', index_col=0)
                print(df_ToDo)
            else:
                pass
        else:
            print("Incorrect password entered!")
            """Code to reset password but need to set up email functionality
            print("1 - Reset password\n2 - Exit")
            else:
                quit()
            """
    except xlsxwriter.exceptions.FileCreateError as e:
        print("\nCould not save. Please make sure the file is not open!")
        #quit()
    except ValueError:
        print("\nOops!  That was not a valid entry.  Try again!")
    #except:
     #   print('There was an unexpected error. Please try again!')

#---Method for registration
def userRegistration(df):
    try:
            print("Enter Username: ")
            name = input()
            print("Enter password: ")
            pwd = input()
            print("Enter email address")
            email = input()
            print("Enter address")
            address = input()
            # append new user details to User_Login
            df_append = pd.DataFrame([[name, pwd, email, address]], index=[len(df) + 1],
                                     columns=['Username', 'Password', 'Email_ID', 'Address'])
            df_new = df.append(df_append)
            df_new.to_excel('User_Login.xlsx', index=True, header=True)
            print("\nNew user added successfully")
            # ----creating new empty excel sheet for To do items
            writer = pd.ExcelWriter(name + '.xlsx', engine='xlsxwriter')
            writer.save()
    except xlsxwriter.exceptions.FileCreateError as e:
        print("\nCould not save. Please make sure the file is not open!")
        #quit()
    except ValueError:
        print("\nOops!  That was not a valid entry.  Try again!")
    #except:
     #   print('There was an unexpected error. Please try again!')