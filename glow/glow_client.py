#!/usr/bin/env python

"""Example of program with many options using docopt.

Usage:
  glow_client.py all
  glow_client.py --server=SERVER_LABEL 
  glow_client.py --cluster=CLUSTER_LABEL 
  glow_client.py --cluster=CLUSTER_LABEL --server=SERVER_LABEL
  
Arguments:
  PATH  destination path

Options:
  -h --help            show this help message and exit
  --version            show version and exit
  -v --verbose         print status messages
  -q --quiet           report only file names
  --server=SERVER_LABEL   speifies the server
  --cluster=CLUSTER_LABEL   speifies the cluster
  -t --temperature        returns the temperature
  -p --power              returns the power

Description:

  describe here what the commands do
   
  glow_client.py all
    
    prints out ...
        
  glow_client.py --server=a001
  
      prints out the information for the servers with 
      than name a001
      
  glow_client.py --cluster=alpha
  
      prints out the information for the cluster with 
      than name alpha
   
  glow_client.py --cluster=alpha --server=a001

      prints out the information for the cluster with 
      than name alpha and
      the servers with than name a001
      
   
    
"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    print(arguments)

'''    
1. declare via docopt some nice command for the commandline
2. have a nice api that calls internally the rest calls
3. the methods defined in 2 are used in 1

4. figure out how to secure the http call with ngnx while getting help form Allan


class glow_command

    uses docopts
    
    # glow -server label -t
    
    # glow 
    
    # glow -cluster label_cluster -server label_server -t
    
    

class glow_client_api

   def get_temperatures(self):
       call the rest thingy somehow
       
   def gat_temperature_cluster(self, label):
'''