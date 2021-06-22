import pywhatkit as kt
import smtplib
import ssl
import os
import time

def whatsapp():
    num = "+917498834253"
    msg = "Hi Ritika...Priyanka Here!"
    kt.sendwhatmsg_instantly(num, msg)
    print("Whatsapp Message sent successfully")

def mail():
    sender_email = "priyankabhidessk@gmail.com"
    receiver_email = "ritikaahuja868@gmail.com"
    password = ("bhide_p@173")
    message = """Alert! \n
    Hey ritika...someone is trying to use your mail"""

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print("Login Successful ")
    server.sendmail(sender_email, receiver_email, message)
    print("Email has been seen to ", receiver_email , "successfully")

def ec2Instnce():
    os.system("terraform -chdir=D:/TFWS/ec2 init")
    time.sleep(5)
    os.system("terraform -chdir=D:/TFWS/ec2 apply -auto-approve")
    

         
