def extendo():
    extension = input("File name: ").lower().strip()

    if extension[len(extension) - 4:len(extension)] == ".jpg" or extension[len(extension) - 5:len(extension)] == ".jpeg":
        print("image/jpeg")
    elif extension[len(extension) - 4:len(extension)] == ".gif":
        print("image/gif")
    elif extension[len(extension) - 4:len(extension)] == ".png":
        print("image/png")
    elif extension[len(extension) - 4:len(extension)] == ".pdf":
        print("application/pdf")
    elif extension[len(extension) - 4:len(extension)] == ".txt":
        print("text/plain")
    elif extension[len(extension) - 4:len(extension)] == ".zip":
        print("application/zip")

    else:
        print("application/octet-stream")



extendo()

