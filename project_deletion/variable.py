from googleapiclient import discovery

from oauth2client.client import GoogleCredentials

projectid = input("Enter project_id : ")

credentials = GoogleCredentials.get_application_default()
        
service = discovery.build('compute', 'v1', credentials=credentials)