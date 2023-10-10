import sqlite3

conn = sqlite3.connect('fileList.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files (\
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    col_fileNames TEXT)")
    conn.commit()
conn.close()

    
def file_Function():
    fileList = ['information.docx', 'Hello.txt', 'myImage.png', 'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg']
    for filename in fileList:
        if(filename.endswith('.txt')):
            print(filename)

file_Function()

                
