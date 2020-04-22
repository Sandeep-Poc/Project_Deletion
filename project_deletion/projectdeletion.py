from googleapiclient import discovery

from pprint import pprint

from project_deletion import variable

class projectdeletion:
    
    def project_deletion(self):

        service = discovery.build('cloudresourcemanager', 'v1', credentials=variable.credentials)

        request = service.projects().delete(projectId=variable.projectid)
        
        request.execute()
        
        pprint("Project has been shutdown now and it will get deleted after 30days")
        
        