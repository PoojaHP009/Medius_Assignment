import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from django.shortcuts import render

from django.core.files.storage import FileSystemStorage

from Medius_prj.settings import BASE_DIR


# Create your views here.

def index(request):
    msg=""
    if (request.method == 'POST'):
        csv = request.FILES['file']

        fss = FileSystemStorage()
        file_name = 'csv_sample.csv'
        file_path = str(BASE_DIR) + "/Medius_app/static/input/" + file_name

        msg = "file inserted"
    return render(request,"index.html",{"msg":msg})

def send_mail(subject,body,tomail):
    sendermail=" " #mention here your mail id(From)
    senderpsw = " " #mention here pswd contain like example "asdf sdfg ghjk edft")
    msg = MIMEMultipart()
    msg['subject']=subject
    msg['From']=sendermail
    msg['To']=','.join(tomail)

    msg.attach(MIMEText(body, 'html'))

    image_path = "Medius_app/static/ouput/data.jpg"


    try:
        with open(image_path, 'rb') as img_file:
            img_data = img_file.read()

        image = MIMEImage(img_data, name=os.path.basename(image_path))
        image.add_header('Content-ID', '<image1>')
        msg.attach(image)
    except Exception as e:
        print(f"Error reading image file: {e}")

    with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
        smtp.login(sendermail,senderpsw)
        smtp.sendmail(sendermail,tomail,msg.as_string())

def mail(request):
    msg=""
    if(request.method=='POST'):
        email="" #mention here from whome your sending mail id
        subject = "Python Assignment - Pooja"

        body = """
        <html>
            <body>
                <p>Here is your image:</p>
            </body>
        </html>
        """
        emailsp = [email]
        send_mail(subject,body,emailsp)
        msg = "mail sent"
    return render(request,"mail.html",{'msg':msg})