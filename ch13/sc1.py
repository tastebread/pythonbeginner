import sqlite3
con = sqlite3.connect("/Users/tastebread/Desktop/pythonbeginner/ch13/naverDB")
#데이터 베이스 연결 데이터파일이 없다면 자동적으로 생성해준다.

#커서 생성 : 커서는 데이터베이스 SQL문을 실행하거나 실행된 결과를 돌려받는 통로라고 생각하면 된다
cur = con.cursor()


#테이블 만들기
#cur.execute("CREATE TABLE userTable (id char(4), userName char(15), email char(20), birthYear int)")
cur.execute("INSERT INTO userTable VALUES('john', 'John Bann', 'john@naver.com', 1990)")
cur.execute("INSERT INTO userTable VALUES('kim', 'Kim Chi', 'kim@daum.net', 1992)")
cur.execute("INSERT INTO userTable VALUES('lee', 'Lee Pal', 'lee@paran.com', 1988)")
cur.execute("INSERT INTO userTable VALUES('park', 'Park Su', 'park@gmail.com', 1980)")

con.commit()
con.close()