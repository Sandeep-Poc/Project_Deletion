from pprint import pprint

from googleapiclient import discovery

#from oauth2client.client import GoogleCredentials

from project_deletion import variable

class computevm:
    
        #credentials = GoogleCredentials.get_application_default()
        
        #service = discovery.build('compute', 'v1', credentials=credentials)
        
   
        def vm_instance_details(self):
            
            pprint("Checking for VM's in the project")
        
            instance_exists = False
        
            zone_request = variable.service.zones().list(project = variable.projectid)

            zone_response = zone_request.execute()
        
            for zone_details in zone_response['items']:
    
                zone_list = list(zone_details.values())
        
                zone_list = zone_list[3]
            
                instance_request = variable.service.instances().list(project = variable.projectid, zone=zone_list)
            
                instance_response = instance_request.execute()
            
                instance_details = instance_response.get("items","")
            
                if len(instance_details) > 0:
                
                    instance_exists =  True
                
                    break
            
            if instance_exists == 1:
            
                pprint("Instances exists in project please delete .........")
            
            else:
                
                    pprint("Checking for disks in project")
                    
                    from project_deletion.disks import disks
                
                    obj_disks = disks()
                
                    obj_disks.disks_details()
                
    
obj_computevm = computevm()

obj_computevm.vm_instance_details()


                
                

            
            
            
