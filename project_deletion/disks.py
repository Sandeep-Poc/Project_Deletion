from pprint import pprint

from project_deletion import variable

class disks:
    
    def disks_details(self):
        
        disks_exist = False
        
        zone_request = variable.service.zones().list(project = variable.projectid)
  
        zone_response = zone_request.execute()
        
        for zone_details in zone_response['items']:

            zone_list = list(zone_details.values())
        
            zone_list = zone_list[3]
            
            disks_request = variable.service.disks().list(project = variable.projectid, zone = zone_list)
            
            disks_response = disks_request.execute()
            
            disk_details = disks_response.get("items","")
            
            if len(disk_details) > 0:
                
                disks_exist = True
        
        if disks_exist:
            
            pprint("Disks exists in project please delete .......")
        
        else:
            
            pprint("Checking for firewalls in project")
            
            from project_deletion.firewall import firewall
            
            obj_firewall = firewall()
            
            obj_firewall.fire_details()
 
         
            