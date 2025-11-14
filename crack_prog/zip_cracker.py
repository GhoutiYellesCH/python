import pyzipper

zip_file = input("Enter Your Zip File:")
pass_list = input("Enter Your Password List:")

count = 1

with open(pass_list, "rb") as text:
    for i in text.readlines():
        password = i.strip()

        try:
            with pyzipper.AESZipFile(zip_file) as zf:
                zf.extractall(password)

                data = zf.namelist()[0]
                data_size = zf.getinfo(data).file_size
                print("\n[+] Password Found! %s" % (password.decode("utf8")))
                print(
                    "File: %s, Size: %d bytes"
                    % (zf.namelist()[0], zf.getinfo(data).file_size)
                )
                break

        except:
            number = count
            print("[x] Password Failed! %d. %s" % (count, password.decode("utf8")))
            count += 1
            pass
