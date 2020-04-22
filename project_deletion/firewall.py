from pprint import pprint

from project_deletion import variable

class firewall:
        
    def fire_details(self):
        
        firewall_request = variable.service.firewalls().list(project=variable.projectid)

        firewall_response = firewall_request.execute()
        
        disk_details = firewall_response.get("items","")
        
        if len(disk_details)>0:
            
            pprint("Firewalls exists in project, please delete ......")
            
        else:
            
            from project_deletion.vpn import vpn
            
            obj_vpn = vpn()
            
            pprint(obj_vpn.vpn_details())