import os
import time

choice = ""
final_desplay = "thanks for comming and good luck in next time"


def learncrypto():
    os.system("clear")
    time.sleep(1.5)
    print(
        """         	==== learning requare paper ====
            
    	from this stage we will start explain deferent type 

of cryptography methode but after each one we will delet every things

            	 i highly recommand to take note.
            
"""
    )
    time.sleep(10)
    os.system("clear")

    print(
        """
=================================== Identifying the hash types =====================================

A few notse on identifying hashes before we begin. Sometimes you’ll run a hash through a tool to identify 
it and multiple options will be displayed so you’ll have to trial and error your way through finding 
the correct one to crack it. Sometimes these tools will also output incorrect information. These are just 
a couple of the joys of hash cracking but the good news is I’m already starting to be able to identify 
several of the hash types just by looking at them since they have a general structure and format to them 
in most cases. Resources for identifying hash types

    """
    )
    time.sleep(40)
    os.system("clear")

    print(
        """
Also, before starting to crack passwords you’ll in many cases need to take some time and identify what type 
of password hash it is. You’ll then use that information with the tools so they know how to crack the hash.
    """
    )
    time.sleep(15)
    os.system("clear")

    print(
        """
Resources for identifying hash types

There are several tools and resources available to help with these tasks and I’ll list a few of them here:

    hashcat.net - A good listing and as a bonus it lists the hash mode number you plug in when using hashcat to crack the hash.
    
    hashes.com - A website with a simple interface. Just paste the hash into the box and it will attempt to identify it’s type.
    tunnelsup.com - Another website.
    
    name-that-hash - This is a command line python script that you can install via: sudo apt install name-that-hash. What’s great
     about this tool is it will list both the mode number for hashcat and format type for John the Ripper.
    """
    )
    time.sleep(30)
    os.system("clear")

    print(
        """
To get started I added all of these hashes to a single text file:


──(kali㉿kali)-[~/work]
└─$ cat hashes.txt
CBFDAC6008F9CAB4083784CBD1874F76618D2A97

1C8BFE8F801D79745C4631D09FFF36C82AA37FC4CCE4FC946683D7B336B63032

$2y$12$Dwt1BZj6pcyc3Dy1FWZ5ieeUznr71EeNkJkUlypTsgbX1H68wsRom

279412f945939ba78ce0758d3fd83daa

F09EDCB1FCEFC6DFB23DC3505A882655FF77375ED8AA2D1C13F640FCCC2D0C85

1DFECA0C002AE40B8619ECF94819CC1B

$6$aReallyHardSalt$6WKUTqzq.UQQmrm0p/T7MPpMbGNnzXPMAXi4bJMl9be.cfi3/qxIf.hsGpS41BqMhSrHVXgMpdjS6xeKZAs02.

e5d8870e5bdd26602cab8dbe07a942c8669e56d6:tryhackme


    """
    )
    time.sleep(10)
    os.system("clear")

    print(
        """

And then ran the file through the command line utility listed above called name-that-hash nth for
a list of possible types on each hash:

┌──(kali㉿kali)-[~/work]
└─$ nth -t "48bb6e862e54f2a795ffc4e541caed4d" --no-banner -a

48bb6e862e54f2a795ffc4e541caed4d
Most Likely
MD5, HC: 0 JtR: raw-md5 Summary: Used for Linux Shadow files.
MD4, HC: 900 JtR: raw-md4
NTLM, HC: 1000 JtR: nt Summary: Often used in Windows Active Directory.
Domain Cached Credentials, HC: 1100 JtR: mscach

Now that we have that information let’s move on to cracking.
    """
    )
    time.sleep(20)
    os.system("clear")

    print(
        """

And then ran the file through the command line utility listed above called name-that-hash nth for
a list of possible types on each hash:

┌──(kali㉿kali)-[~/work]
└─$ nth -t "48bb6e862e54f2a795ffc4e541caed4d" --no-banner -a

48bb6e862e54f2a795ffc4e541caed4d
Most Likely
MD5, HC: 0 JtR: raw-md5 Summary: Used for Linux Shadow files.
MD4, HC: 900 JtR: raw-md4
NTLM, HC: 1000 JtR: nt Summary: Often used in Windows Active Directory.
Domain Cached Credentials, HC: 1100 JtR: mscach

Now that we have that information let’s move on to cracking.
    """
    )
    time.sleep(20)
    os.system("clear")

    print(
        """
Cracking the hashes
I prefer to use hashcat for most of my password cracking due to how fast it is.

did you want to get a advice from hacker ?? 
    """
    )

    choice = input("y/n ")

    if choice == "y":
        print(
            """
    		TIP: You can greatly increase the speed of hashcat if you run it on your host machine instead of
			inside a virtual machine because it can take advantage of your video card. You’ll see the -D 2
			argument in all of my hashcat commands, and that tells it to use my video card.
    	
    	"""
        )

    time.sleep(20)
    os.system("clear")

    print(
        """
Resources for cracking the hashes
We have several tools and resources available when it comes to cracking password hashes. Two of the
more popular command line tools are:
John the Ripper
hashcat
And a popular website:
crackstation.net - This website uses rainbow tables for quick results.
    """
    )
    time.sleep(30)
    os.system("clear")

    print(
        """
            
As a FYI the command line tools have issues cracking multiple password hashes in a single file if
there are different types present, so at this point I created a separate file for each hash to use
with the command line tools.
For my own learning I went through and cracked all of these hashes using both John the Ripper and
hashcat, so you’ll see the commands necessary in both tools for each hash. I hope you find that
useful! I also let you know whether or not the crackstation website will crack the password or not.

    """
    )
    time.sleep(30)
    os.system("clear")
    printf()


def start_the_game():

    os.system("gedit /home/h7ck3r/Notes/code/python/game/gamer_place/hashes &")
    time.sleep(3)
    os.system("clear")

    print(
        """
to start the game you hase all tools instaled and i do create a way to get doc from tools:

	tab : alt + 2 o see hashcat manual tools 
	
	command : nth 
	
	command : hashcat
	
	"""
    )


def printf():

    print(
        """
Hash 1 - 48bb6e862e54f2a795ffc4e541caed4d"
Hash type identified: MD5
hashcat command: hashcat -m 0 -D 2 hash1.txt rockyou.txt
JtR command: john --wordlist=rockyou.txt --format=raw-md5 hash1.txt
crackstation website: Works
"""
    )


def main():
    os.system("clear")
    time.sleep(1.5)
    print("           ======= let start the game =======           ")
    print("")
    print(" here we will hack the plain text as known cryptography ")
    print("")
    print(" the hope was to create app but the time wasn't enoph   ")
    print("")
    print(" do you want to the next step ... ")
    print("")
    choice = input("y / n ? ")
    if choice == "y":
        os.system("clear")
        time.sleep(1.5)
        print("let play the game")

        print("for first do you love to learn about cryptography or continue ")

        choice = input("l/c ? ")

        if choice == "l":
            learncrypto()
            start_the_game()
        else:
            print("")
            start_the_game()

    else:
        print(final_desplay)


main()
