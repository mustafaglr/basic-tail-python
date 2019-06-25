import os

oldlinecount=0
oldsizeoffile=0
os.chdir("./log")
url="logfile2.log"
while(True):
    f = open(url, "rb")
    linecount = f.readlines().__len__()
    sizeoffile = os.path.getsize(url)

    if oldlinecount < linecount and oldsizeoffile < sizeoffile:
        f.seek(oldsizeoffile-sizeoffile, os.SEEK_END)
        oldsizeoffile = sizeoffile
        if oldlinecount != 0 and oldlinecount != linecount:
            for read in f.readlines():
                print(read.decode("UTF-8"))
        oldlinecount = linecount






