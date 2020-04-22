from pprint import pprint

from project_deletion import variable

class vpn:
    
    def vpn_details(self):

        
        vpn_list_request = variable.service.networks().list(project=variable.projectid)
        
        vpn_list_response = vpn_list_request.execute()
        
        vpn_details = vpn_list_response.get("items","")
        
        if len(vpn_details)>0:
            
            pprint("VPN exists in project, please delete .....")
            
        else:
            
            pprint("Resources not existed in project and project will be shutdown now")
            
            from project_deletion.projectdeletion import projectdeletion
            
            obj_projectdeletion = projectdeletion()
            
            pprint(obj_projectdeletion.project_deletion())
            