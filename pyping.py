import ipaddress
import subprocess
import sys
from datetime import datetime

startTime = datetime.now()

net = sys.argv[1]


network = ipaddress.ip_network(net)

for host in network:
	address = str(host)
	output = subprocess.Popen(["ping.exe", "-n", "1",address],stdout = subprocess.PIPE).communicate()[0]

	if ('Received = 0' in str(output)) or ("Destination host unreachable" in str(output)):
		print("{} - Offline\n".format(host))
		
	else:
		print("{} - Online\n".format(host))

print(f'Script took: {datetime.now()-startTime}')