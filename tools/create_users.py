#テキトーにユーザー25人作成(ただし、2回目使うとidかぶるのでだめか、、、)

from faker import Factory
import sqlite3
import hashlib

fake = Factory.create()

def create_fake_user(id, name, email, password):
    conn = sqlite3.connect('../databases/bottle_project.db')
    c = conn.cursor()
    insert = "insert into users(id,name,email,password) values(?,?,?,?)"
    user = (id,name,email,password)

    c.execute(insert, user)
    conn.commit()


if __name__ == "__main__":
    for i in range(25):
        create_fake_user(i+1,fake.name(),fake.email(),hash(fake.email()))