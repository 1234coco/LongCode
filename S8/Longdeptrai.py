import sqlite3

u = sqlite3.connect('customer.db')


C = u.cursor()


C.execute("""CREATE TABLE TEST (
    Tên text,
    Toán text,
    TH text
    AV text
    )""")

T ="Tên"
TN = "Toán"
TH = "Tin Học"
AN = "Anh văn"

DB = [
       ('Long', 'Lam', 'Anh'),
       ('8', '9', '7'),
       ('9', '8', '7'),
       ('8','7','10'),
    ]

C.executemany("INSERT INTO TEST VALUES (?,?,?)", DB)

u.commit()
C.execute("SELECT * FROM TEST")
CD = C.fetchall()


print(T +" "+CD[1]+" | "+CD[2]+" | "+CD[3])

print("\n------------------------------------------")

print(CD[4]+" "+CD[5]+" | "+CD[6]+" | "+CD[7])

print("\n------------------------------------------")

print(CD[8]+" "+CD[9]+" | "+CD[10]+" | "+ CD[11])
u.close()


