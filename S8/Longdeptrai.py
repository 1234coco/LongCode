import sqlite3

u = sqlite3.connect('customer.db')


C = u.cursor()


C.execute("""CREATE TABLE TEST (
    Tên text,
    Toán text,
    TH text,
    AV text
    )""")

T ="Tên"
TN = "Toán"
TH = "Tin Học"
AN = "Anh văn"

DB = [
       ('Long','8', '9', '7'),
       ('Lam','9', '8', '7'),
       ('Anh','7','10','9'),
    ]

C.executemany("INSERT INTO TEST VALUES (?,?,?,?)", DB)

u.commit()
C.execute("SELECT * FROM TEST")
item = C.fetchall()
A = 0
print("\t"+T+"\t"+" | "+"\t"+TN+"\t"+" | "+"\t"+TH+"\t"+" | "+"\t"+AN)
for item in item:
    print("\t"+item[0]+"\t"+" | "+"\t"+ item[1]+ "\t"+" | "+"\t"+ item[2]+ "\t"+" | "+"\t"+ item[3])
    print("\n---------------------------------------------------------------")





