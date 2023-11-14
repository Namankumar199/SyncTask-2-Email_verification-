import random
import smtplib

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('mca.namankumar@gmail.com','qbkn mnch xfgx osbx')
stored_otp = ''.join([str(random.randint(0,9)) for i in range(6)])
msg = 'Hello, Your OTP is ' + str(stored_otp)
server.sendmail('mca.namankumar@gmail.com','infonaman07676@gmail.com',msg)
server.quit()

def verify_otp():
    email_id = input(" Enter your email_Id : ")
    user_otp = input(" Enter the OTP you received : ")

    # Perform the verification logic here, such as comparing the entered OTP with the generated on
    # Example verification logic
    if user_otp == stored_otp: 
        print(" Your OTP verification is successfully Completed!")
    else:
        print(" OTP verification failed! You Insert wrong OTP")

verify_otp() 