import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
from jinja2 import Template
import os

# Open the Credentials From the Credentials.env
load_dotenv('credentials.env')
sender_email = os.getenv('username')
sender_password = os.getenv('password')

def load_html_email_format(file_path,**kwargs):
    with open(file_path, 'r', encoding='utf-8') as file:
        html_content =  file.read()
    # Create a Jinja2 Template object
    template = Template(html_content)
    
    # Render the template with provided kwargs
    return template.render(**kwargs)

def send_html_email(recipient_email,subject,html_content,attachments=[]):
    
    #email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    #HTML content
    msg.attach(MIMEText(html_content, 'html'))

    # Attach files
    for file_path in attachments:
        try:
            # Open the file in binary mode
            with open(file_path, 'rb') as file:
                #MIMEBase object
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)  # Encode the file in base64
                # Add header for the attachment
                # part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
                part.add_header('Content-Disposition', f'attachment; filename={"test_file"}')
                msg.attach(part)  # Attach the file to the message
        except Exception as e:
            print(f"Failed to attach {file_path}: {e}")

    # Set up the SMTP server
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Enable security
            server.login(sender_email, sender_password)  # Log in
            server.send_message(msg)  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

def send_email(recipient_name,recipient_email,html_file, attachments = []):
    
    # Get the email and name of the contact
    recipient_name = recipient_name
    email = recipient_email
        
    # Load the HTML content from the file
    html_content = load_html_email_format(html_file,name = recipient_name)
    
    send_html_email(recipient_email=email, subject="Welcome to Learning Utsav 2024", html_content=html_content)



# MAIN PROGRAM

if __name__ == "__main__":    
    
    #TO
    recipient_name = "Roshan"
    recipient_email = "kan078bct067@kec.edu.np"
    
    # CONTENT
    html_file = "./email_content.html"
    attachments = ['/Users/roshanpandey/Desktop/CLUB/Learning Utsav/Mail format/Community/index.html']
    
    # Send the email
    send_email(recipient_name,recipient_email,html_file=html_file,attachments=attachments)