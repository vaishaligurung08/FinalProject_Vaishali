import pandas as pd
from FinalProject_Libraries import signIn
from FinalProject_Libraries import userRegistration
df = pd.read_excel('User_Login.xlsx', index_col=0)
print('1 - Sign In \n2 - Registration')
x = int(input())
if x == 1:
    signIn(df)
elif x == 2:
    userRegistration(df)
