



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
