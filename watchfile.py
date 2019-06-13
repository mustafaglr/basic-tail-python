import os

oldlinecount=0
oldsizeoffile=0
os.chdir("./log")

while(True):
    f = open("logfile2.log", "rb")
    linecount = f.readlines().__len__()
    sizeoffile = os.path.getsize("logfile2.log")

    if oldlinecount < linecount and oldsizeoffile < sizeoffile:
        f.seek(oldsizeoffile-sizeoffile, os.SEEK_END)
        oldsizeoffile = sizeoffile
        if oldlinecount != 0 and oldlinecount != linecount:
            for read in f.readlines():
                print(read.decode("UTF-8"))
        oldlinecount = linecount






