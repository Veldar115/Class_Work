# Import the necessary module
from dotenv import load_dotenv
import os

# Load environment variables from the .env file (if present)
load_dotenv()

# Access environment variables as if they came from the actual environment
SECRET_KEY = os.getenv('EmailPassword')
print(SECRET_KEY)
# Import smtplib for the actual sending function
import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("iamhero114@gmail.com", SECRET_KEY)
# message to be sent
message = "Message_you_need_to_send"
# sending the mail
s.sendmail("ashalev@mail.ru", "iamhero114@gmail.com", message)
# terminating the session
s.quit()