import sqlite3

#데이터 입력 프로그램 구현

con,cur = None,None
data1,data2,data3,data4 = "","","",""
sql=""

#메인코드 부분

con = sqlite3.connect("/Users/tastebread/Desktop/pythonbeginner/ch13/naverDB")
cur = con.cursor()

while (True):
    data1 = input("사용자ID ==> ")
    if data1 == "":
        break;
    data2 = input("사용자이름 ==> ")
    data3 = input("이메일 ==> ")
    data4 = input("출생연도 ==> ")
    sql = "INSERT INTO userTable VALUES('" + data1 + "','"+ data2 +"','" + data3 +"',"+ data4 +")"
    cur.execute(sql)

con.commit()
con.close()