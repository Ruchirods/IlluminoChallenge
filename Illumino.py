import pandas as pd

class Firewall:

    def __init__(self,path):
        self.path = path
      
    #Checks if the IP address is in range    
    def checkRange(ipAdd,ipadd):
        ruleAdd = ipAdd.split('.')
        inAdd = ipadd.split('.')
        for i in range(len(ruleAdd)-1):
            if ruleAdd[i] < inAdd[i]:
                return True
            if ruleAdd[i] > inAdd[i]:
                return False
        return True

    # checks if the input parameters should be blocked or passed
    def accept_packet(self,direction,protocol,portno,ipadd): 
        for portion in pd.read_csv(self.path, chunksize=4):            
            filteredDirPro = portion[(portion["direction"] == direction) &\
                                   (portion["protocol"] == protocol)]
            if not filteredDirPro.empty:
                filteredPort = filteredDirPro[(filteredDirPro["port"] == str(portno)) |\
                                            ((int(filteredDirPro["port"].str.split('-',1).str[0]) < portno < int(filteredDirPro["port"].str.split('-',1).str[1])))]
                if not filteredPort.empty:
                    print(filteredPort)
                    for index,row in filteredPort.iterrows():                        
                        if row['IP address'] == ipadd:
                            return True;
                        else:
                            IPList = row[3].split('-')
                            if len(IPList) == 2:
                                return Firewall.checkRange(IPList[0],ipadd) & \
                                    Firewall.checkRange(ipadd,IPList[1])
        return False
                                
                                
     

