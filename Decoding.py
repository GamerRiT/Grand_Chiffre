import sqlite3

connect=sqlite3.connect('chiffre.db')
cursor=connect.cursor()


text1=input()
digit=""
chiff=""
a=0
leg=len(text1)
for i in range(0,leg):
    if text1[i]!="-":
        a=a+1
        digit=digit+text1[i]
    if text1[i]=="-" or a==leg:
        cursor.execute("SELECT * FROM code_slogi")
        all_results=cursor.fetchall()
        smert=0
        for i in range(0,14):
            if digit == str(all_results[i][1]):
                exit1=all_results[i][0]
                chiff=chiff+str(exit1)
                smert=1
        if smert==0:
            cursor.execute("SELECT * FROM code_slogi_1")
            all_results=cursor.fetchall()
            smert=0
            for i in range(199):
                if digit == str(all_results[i][1]):
                    exit1=all_results[i][0]
                    chiff=chiff+str(exit1)
                    smert=1
        if smert==0:
            cursor.execute("SELECT * FROM code_alfabet")
            all_results=cursor.fetchall()
            smert=0
            for i in range(33):
                if digit == str(all_results[i][1]):
                    exit1=all_results[i][0]
                    chiff=chiff+str(exit1)
                    smert=1
        digit=""
        a=a+1
print(chiff)