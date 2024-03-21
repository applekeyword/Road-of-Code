suffix = input("File name: ").rstrip().rsplit(".")[-1].lower()

if suffix in ["gif", "png"]:
    print("image/", suffix, sep="")
elif suffix in ["jpg", "jpeg"]:
    print("image/jpeg")
elif suffix in ["txt"]:
    print("text/plain")
elif suffix in ["pdf", "zip"]:
    print("application/", suffix, sep="")
else:
    print("application/octet-stream")
