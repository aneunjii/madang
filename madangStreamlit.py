import pymysql
import pandas as pd
import streamlit as st

# DB 접속 정보는 secrets.toml에서 읽어옴 (배포할 때 비밀번호를 숨기기 위해)
cfg = st.secrets["mysql"]
dbConn = pymysql.connect(user=cfg["user"], password=cfg["password"], host=cfg["host"],
                         port=int(cfg["port"]), database=cfg["database"], charset='utf8')
cursor = dbConn.cursor(pymysql.cursors.DictCursor)

st.title("madang")
name = st.text_input("name")                  # 원본의 textEdit

if st.button("Search"):                       # 원본의 pushButton → search_click
    sql = "select o.orderid, c.name, b.bookname, o.saleprice, o.orderdate from Customer c, Orders o, Book b "
    sql += "where c.name='" + name + "' and c.custid=o.custid and b.bookid=o.bookid;"
    cursor.execute(sql)
    result = cursor.fetchall()
    result = pd.DataFrame(result)
    print(result)
    st.dataframe(result)                      # 원본의 tableWidget