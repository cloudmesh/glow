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
import requests
import pprint

class GlowClient:
    
    def __init__(self, argdict):
        self.arg_dict = argdict
        self.server_url = "http://127.0.0.1:5000"
        
    def run(self):
        if self.arg_dict["all"]:
            self.get_temperature_all_rest()
        elif self.arg_dict["--cluster"]:
            if self.arg_dict["--server"]:
                self.get_temperature_rack_rest(self.arg_dict["--cluster"], self.arg_dict["--server"])
            else:
                self.get_temperature_rack_rest(self.arg_dict["--cluster"])
        elif self.arg_dict["--server"]:
            self.get_temperature_all_rest(self.arg_dict["--server"])
            
    
    def get_temperature_all_rest(self, server=None):
        surl = "/cm/v1.0/glow/t"
        result_dict = self.request_rest_api(surl)
        data_dict = result_dict["glow"]["data"]
        implicit_rack_name = None
        if server:
            for rack_name in data_dict:
                if server in data_dict[rack_name]:
                    implicit_rack_name = rack_name
                    break
            if implicit_rack_name:
                filtered_data_dict = {implicit_rack_name: {server: data_dict[implicit_rack_name][server]}}
            else:
                filtered_data_dict = {"Unknown-Rack": {server: None}}
            result_dict["glow"]["data"] = filtered_data_dict
        pprint.pprint(result_dict)
    
    def get_temperature_rack_rest(self, rack_name, server=None):
        surl = "/cm/v1.0/glow/t"
        if rack_name:
            surl += "/{0}".format(rack_name)
        if server:
            surl += "/{0}".format(server)
        result_dict = self.request_rest_api(surl)
        data_dict = result_dict["glow"]["data"][rack_name]
        if server:
            if server in data_dict:
                result_dict["glow"]["data"][rack_name] = {server: data_dict[server]}
            else:
                result_dict["glow"]["data"][rack_name] = {server: None}
        pprint.pprint(result_dict)
    
    def request_rest_api(self, surl):
        r = requests.get(self.server_url + surl)
        return r.json()


if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    gclient = GlowClient(arguments)
    gclient.run()
    
    """
    print(arguments)
    server = "not defined"
    if arguments['--server'] is not None:
        server = arguments['--server']
    print server
    """

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