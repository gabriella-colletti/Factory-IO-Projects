# Gabriella Colletti
# Project 2 c
# Intrustion detection system

global stop   # Stop condition to stop sniffing packets
stop = False  

class Collection():
    '''Collects the packet information so that we can average 
    the time imbetween packets'''
    def __init__(self):
        self.times = []                # Packet Time
        self.cur_idx = 0               # Current Packet Index
        self.possible_attack = [0]     # Array the holds indices of possible attack packet indices
        self.freqs = []                # The elapsed times between packets

    def update(self,time): 
        import numpy as np
        if len(self.times) > 500:  # Keep the average relavant
            self.times = []        # Reset the times
            self.cur_idx = 0       # Reset the current index
            self.freqs = []        # Reset the elapsed times
       
        else:  # Update the times array with new times
            self.times.append(time)
            self.freqs = [self.times[i+1] - self.times[i] for i in range(len(self.times)-1)]  # Update the frequency array with new frequencies

       
    def get_frequency(self):
        import numpy as np
        return np.mean(self.freqs), np.std(self.freqs)   # Mean Packet Elapsed Times and Standard Deviation
       
   
    def check_attack_status(self,packet):  
        ''' Determines the prescence of an attack'''
        time = float(packet[0][1].time)   # Get current packet time
        self.update(time)                 # Update the packet data
        average_freq, std = self.get_frequency()  # Get statistics
       
        if len(self.freqs) == 0: # Need a least 1 packet in frequency
            return
       
        try:
            # Ignore any packets of wrong sender
            if packet[0][1].src != '192.168.56.101': 
                return
        except:
            return
            
	# If the packet frequency is suspicious
        if self.freqs[self.cur_idx] < average_freq-std: 
            # If the last suspicious packet was within 5 packets of this 
            if self.possible_attack[-1] >= self.cur_idx-5: 
            	# new suspicious pack, add suspicios packet index to cache
                self.possible_attack.append(self.cur_idx)  
            else:  # The packets are not semi-sequential (within 5 packets)
            # Clear the Cache of Attack Indices annd add new sus packet
                self.possible_attack = [self.cur_idx] 
           

         # Looking for a drop in time delay between packets
        if len(self.possible_attack) == 10:  # If there have been 10 suspicious packet kinda in a row (within 5 packets) then we have an attack
            print('-------------------Attack Began-------------------')
            print('Time of Attack: %f'%self.times[self.cur_idx])
            print('Average Frequency : %.6f  Frequency:%.6f'%(average_freq,self.freqs[self.cur_idx]))
            global stop
            stop = True # Set Stopping Condition
        else: #Otherwise print every 100th packet frequency
            if self.cur_idx % 100 == 0:
                print('Benign Packet Frequency: \t%.6f'% self.freqs[self.cur_idx])
        self.cur_idx += 1  # Update Packet Index


def IDS():
    global stop
    from scapy.all import sniff
    import warnings
    packet_info = Collection() # Using Class Object to collect statistics
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category = RuntimeWarning)
        if is_online: #ONLINE IDS
            sniff( iface='enp0s8', stop_filter=lambda s:stop,  prn =packet_info.check_attack_status)



IDS()

	
	
	

