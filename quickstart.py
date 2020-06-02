from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import send_email

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    msg=send_email.CreateMessage('me','khadri.zahid@gmail.com',"Introduction",
    '''Hi <NAME>,

I'm a recent post-grad in Data Informatics(CS) from USC, passionate about building statistical models and smart data-driven applications with my skills in Machine learning, Deep learning, Computer Vision and Natural Language Processing. I have previous experience of 2 years as a software engineer in security platforms team at Fidelity Investments, and as a data scientist intern for 8 months at Dermalogica (Unilever), building and deploying machine learning models. These have helped me gain a broader understanding of data related problems in both, service and product-based companies. I am looking for full time data science and machine learning roles. 
I have completed my degree program and available to start full time immediately.
I would love to have a quick chat about opportunities at <Company.>



Regards,
Tanay Shankar
MS in Data Informatics
University of Southern California
''')
    send_email.SendMessage(service,'me',msg)

if __name__ == '__main__':
    main()