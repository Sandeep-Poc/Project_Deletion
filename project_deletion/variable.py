import os

from googleapiclient import discovery

from oauth2client.client import GoogleCredentials

projectid = os.getenv("Project_Id")

credentials = GoogleCredentials.get_application_default()
        
service = discovery.build('compute', 'v1', credentials=credentials)
