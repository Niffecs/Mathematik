#!/usr/bin/env python3

import os
import ftplib
import sys
import hashlib
import shutil
import os.path

# Load env
FILE = sys.argv[1]
HOST = os.environ["FTP_SERVER"]
USER = os.environ["FTP_USER"]
PWD = os.environ["FTP_PWD"]


# Test PDF
if not "pdf" in FILE:
    print("no pdf")
    sys.exit(-1)

# Create Hash file
hash = hashlib.md5(sys.argv[1][:-4].encode('utf-8')).hexdigest()
shutil.copyfile(FILE, f"{hash}.pdf")
FILE2 = f"{hash}.pdf"

print(f"FILE 1 --> {FILE}")
print(f"FILE 2 --> {FILE2}")

# Test File exist
if os.path.isfile(f"{FILE}"):
    print(f"FILE 1 --> {FILE} --> exist")
else:
    print(f"FILE 1 --> {FILE} -->  not exist")

if os.path.isfile(f"{FILE2}"):
    print(f"FILE 2 --> {FILE2} --> exist")
else:
    print(f"FILE 2 --> {FILE2} --> not exist")


# Test OS 

print(f"FILE --> {hashlib.md5(FILE.encode('utf-8')).hexdigest()}")
print(f"HOST --> {hashlib.md5(HOST.encode('utf-8')).hexdigest()}")
print(f"USER --> {hashlib.md5(USER.encode('utf-8')).hexdigest()}")
print(f"PWD --> {hashlib.md5(PWD.encode('utf-8')).hexdigest()}")


# FTP Gedoens
ftp = ftplib.FTP(HOST, USER, PWD)
ftp.encoding = "utf-8"
with open(FILE, "rb") as file:
    ftp.storbinary(f"STOR {FILE}", file)
ftp.cwd("loader")
with open(FILE2, "rb") as file:
    ftp.storbinary(f"STOR {FILE2}", file)