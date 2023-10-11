import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('fileList.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files (\
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fileNames TEXT)")
    for filename in fileList:
        if(filename.endswith('.txt')):
            cur.execute("INSERT INTO tbl_files(col_fileNames) VALUES (?)", (fileList,))
            print(filename)
    conn.commit()
conn.close()


