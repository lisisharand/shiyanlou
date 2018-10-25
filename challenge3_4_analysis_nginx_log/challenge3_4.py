from datetime import datetime
import re
from collections import Counter
def open_parser(filename):
    with open(filename) as logfile:
        patter = (r''
                r'(\d+.\d+.\d+.\d+)\s-\s-\s'#ip
                r'\[(.+)]\s'#time
                r'"GET\s(.+)\s\w+/.+"\s'#road
                r'(\d+)\s'#status_number
                r'(\d+)\s'#data
                r'"(.+)"\s'#request_head
                r'"(.+)"'#client_info
            )
        parsers = re.findall(patter,logfile.read())
    return parsers
def logs_count():
    logs = open_parser('nginx.log')
#storage_ip_request_ip
    ip_list = []
    request404_list = []
    for log in logs:
        dt = datetime.strptime(log[1][:-6],"%d/%b/%Y:%H:%M:%S")#strptime?
        if int(dt.strftime("%d")) == 11:
            ip_list.append(log[0])
        if int(log[3])==404:
                request404_list.append(log[2])
    return ip_list,request404_list

def main():
    ip_counts = Counter(logs_count()[0])
    request404_counts = Counter(logs_count()[1])
    sorted_ip = sorted(ip_counts.items(),key=lambda x:x[1])
    sorted_request404 = sorted(request404_counts.items(),key=lambda x:x[1])
#max
    ip_dict = dict([sorted_ip[-1]])#parameter_type
    url_dict = dict([sorted_request404[-1]])
    return ip_dict,url_dict
if __name__ == "__main__":
    print(main())
            
            
            
            
            
            
            

