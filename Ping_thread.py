import ipaddress
import subprocess
import sys
from multiprocessing import Pool
from datetime import datetime
import dis

def ping_sweep(network):	
	results = []
	for host in network:
		address = str(host)
		output = subprocess.Popen(["ping.exe", "-n", "1",address],stdout = subprocess.PIPE).communicate()[0]

		if ('Received = 0' in str(output)) or ("Destination host unreachable" in str(output)):
			#print("{} - Offline\n".format(host))
			results.append("{} - Offline\n".format(host))
		else:
			print("{} - Online\n".format(host))
			results.append("{} - Online\n".format(host))
	return results


def main():
	startTime = datetime.now()
	net = sys.argv[1]
	network = ipaddress.ip_network(net)

	split_networks = list(network.subnets(new_prefix=30))

	#agents = 8
	with Pool() as pool:
		results = pool.map(ping_sweep, split_networks)

	with open("results.txt", "w") as f:
		for x in results:
			for i in x:
				f.write(i)

	print(f'Script took: {datetime.now()-startTime}')			

if __name__ == '__main__':
	main()