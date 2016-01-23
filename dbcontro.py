import MySQLdb

conn=MySQLdb.connect(host='localhost',user='root',passwd='930122',db='python')
cur=conn.cursor()
sql="insert into user value(%s,%s)"
name=raw_input('input your name:')
password=raw_input('input your passwd:')
cur.execute(sql,(name,password))
cur.close()
conn.commit()
conn.close()
