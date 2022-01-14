Gabriella Colletti
README

Convention: ">>" is a symbol for command line. Do not type ">>" when typing in the commands.

sample.pcap is sample data to sniff 
source.txt is a text file that has sample.pcap's source ip addresses
dest.txt is a text file that has sample.pcap's source ip addresses


Libraries Needed: numpy and scapy
	(1) First you need to install pip to be able to install the libraries:
		>> sudo apt install python3-pip
   	(2) To install scapy to be able to use its library run:
		>> pip install scapy
	(3) To install numpy to be able to use its library run:
		>> pip install numpy

To run the Task_1.py use the command:
	>> python3 Task_1.py 

To run the Task_2.py use the command:
	>> sudo python3 Task_2.py

	Note you need to use "sudo" to ensure the correct privilege use. 
	If there is an error regarding the libraries reinstall the 
	libraries using the sudo command (i.e. sudo pip install numpy)

	If there is an error regarding not finding the ethernet interface
	(i.e. OSError: [Errno 19] No such device) it means my ethernet 
	interface (enp0s3) is not present on your device. Use the following
	command:
		>> ifconfig -a
	to determine what your ethernet interface is called. Note that "lo"
	is the loop back interface and should not be used. When you have
	found the correct name ethernet interface name then go to Task_2.py
	and change "iface = 'enp0s3'" to "iface = 'YOURINTERFACESNAME'". 
	Note don't actually type the string "YOURINTERFACESNAME" in but
	rather type in the name of the ethernet interface like "eth0" or
	the like.  

Currently Task_2.py uses the stopping condition of finding the first 
6 ip addresses, source and destination ip included, (may or may not be unique), if you want to increase this amount change "count=6" to the proper value.

Similarly, Task_1.py uses the stopping condition of timing out after 120 seconds since running the file without a stopping condition leads my machine to automatically kill it.: If you wish to increase the time, change "timeout=120" to the proper amount. 
