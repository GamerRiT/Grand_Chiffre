import sqlite3

connect=sqlite3.connect('chiffre.db')
cursor=connect.cursor()


i=0
a=0
b=0
q=0
c=0
d=0
p=0
u=0
three=""
two_one=""
two_two=""
one_one=""
one_two=""
one_three=""
one=""
exit=""
text=""
exit1=""
text_=""
text_=input()
length=len(text_)
for i in range(0,length):
    check=0
    if text_[i]!=" " and u<length:
        u=u+1
        text=text+text_[i]
    if text_[i]==" " or u==length:
        w=(len(text)/3)
        while q<=w:
            b=a+3
            if b<=len(text):
                for i in range(a,b):
                    three=three+text[i]
            else: 
                if b-len(text)==1 or b-len(text)==2:
                    for i in range(a,len(text)):
                        three=three+text[i]
            cursor.execute("SELECT * FROM code_slogi")
            all_results=cursor.fetchall()
            check=0
            for i in range(14):
                if three == all_results[i][0]:
                    syp=all_results[i][1]
                    if p==0:
                        exit=str(syp)
                        p=1
                    else:
                        exit=exit+"-"+str(syp)
                    check=1
            q=q+1
            a=a+3
            if check==0 and len(three)>=2:
                for i in range(0,2):
                    two_one=two_one+three[i]
                two=two_one
                cursor.execute("SELECT * FROM code_slogi_1")
                all_results=cursor.fetchall()
                for i in range(199):
                    if two == all_results[i][0]:
                        syp=all_results[i][1]
                        if p==0:
                            exit=str(syp)
                            p=1
                        else:
                            exit=exit+"-"+str(syp)
                        check=1
                if check!=0 and len(three)>=3:
                    one=three[2]
                    cursor.execute("SELECT * FROM code_alfabet")
                    all_results=cursor.fetchall()
                    for i in range(33):
                        if one == all_results[i][0]:
                            syp=all_results[i][1]
                            if p==0:
                                exit=str(syp)
                                p=1
                            else:
                                exit=exit+"-"+str(syp)
                            check=1
                if check==0 and len(three)>=3:
                    one=three[0]
                    cursor.execute("SELECT * FROM code_alfabet")
                    all_results=cursor.fetchall()
                    for i in range(33):
                        if one == all_results[i][0]:
                            syp=all_results[i][1]
                            if p==0:
                                exit=str(syp)
                                p=1
                            else:
                                exit=exit+"-"+str(syp)
                            check=1
                    if check!=0:
                        for i in range(1,3):
                            two_two=two_two+three[i]
                            two=two_two
                            cursor.execute("SELECT * FROM code_slogi_1")
                            all_results=cursor.fetchall()
                            for i in range(199):
                                if two == all_results[i][0]:
                                    syp=all_results[i][1]
                                    if p==0:
                                        exit=str(syp)
                                        p=1
                                    else:
                                        exit=exit+"-"+str(syp)
                                    check=1

            if check==0 and len(three)>=1:
                one_one=three[0]
                one=one_one
                cursor.execute("SELECT * FROM code_alfabet")
                all_results=cursor.fetchall()
                for i in range(33):
                    if one == all_results[i][0]:
                        syp=all_results[i][1]
                        if p==0:
                            exit=str(syp)
                            p=1
                        else:
                            exit=exit+"-"+str(syp)
            if check==0 and len(three)>=2:
                one_two=three[1]
                one=one_two
                cursor.execute("SELECT * FROM code_alfabet")
                all_results=cursor.fetchall()
                for i in range(33):
                    if one == all_results[i][0]:
                        syp=all_results[i][1]
                        if p==0:
                            exit=str(syp)
                            p=1
                        else:
                            exit=exit+"-"+str(syp)
            if check==0 and len(three)>=3:
                one_three=three[2]
                one=one_three
                cursor.execute("SELECT * FROM code_alfabet")
                all_results=cursor.fetchall()
                for i in range(33):
                    if one == all_results[i][0]:
                        syp=all_results[i][1]
                        if p==0:
                            exit=str(syp)
                            p=1
                        else:
                            exit=exit+"-"+str(syp)
            check=1
            exit1=exit1+exit
            exit=""
            three=""
            two_one=""
            two_two=""
            one_one=""
            one_two=""
            one_three=""
            one=""
        i=0
        a=0
        b=0
        q=0
        c=0
        d=0
        text=""
        u=u+1
print(exit1)