#!/usr/bin/env python

from flask import Flask, jsonify

from cloudmesh.rack.rack_data import RackData
from cloudmesh.temperature.cm_temperature import cm_temperature as RackTemperature

app = Flask(__name__)


nop = [
    {
        'id': 1,
        'label' : "abc",
        'description': 'not yet implemented',
        'status' : 4,
        'unit' : 'temperature',
        'ttl' : 'time to live in data to be implemented'
    }
]

@app.route('/cm/v1.0/glow/t', methods = ['GET'])
def get_all_temperatures():
    """returns the temperatures of all registered servers"""
    rack_name = "all"
    temperature_unit = "C"
    data_dict = read_data_from_mongodb(rack_name, temperature_unit)
    return format_result_data(data_dict, temperature_unit, rack_name)
    
@app.route('/cm/v1.0/glow/t/<cluster>', methods = ['GET'])
def get_cluster_temperatures(cluster):
    """returns the temperatures of all servers in the cluster with the given label"""
    temperature_unit = "C"
    data_dict = read_data_from_mongodb(cluster, temperature_unit)
    return format_result_data(data_dict, temperature_unit, cluster)
    
@app.route('/cm/v1.0/glow/t/<cluster>/<server>', methods = ['GET'])
def get_cluster_server_temperatures(cluster, server):
    """returns the temperatures of a named servers in the cluster with the given label"""
    temperature_unit = "C"
    data_dict = read_data_from_mongodb(cluster, temperature_unit)
    return format_result_data(data_dict, temperature_unit, cluster, server)

def format_result_data(data_dict, unit, rack_name, server=None):
    """ format the output data """
    result_dict = {"unit": unit, "data": None}
    if data_dict is None:
        if server:
            result_dict["data"] = {rack_name: {server: None}}
        else:
            result_dict["data"] = {rack_name: None}
    else:
        if server:
            server_data = None
            if rack_name in data_dict:
                if server in data_dict[rack_name]:
                    server_data = data_dict[rack_name][server]
            result_dict["data"] = {rack_name: {server: server_data}}
        else:
            result_dict["data"] = data_dict
    return jsonify( {"glow": result_dict} )

def read_data_from_mongodb(rack_name="all", unit='C'):
    """ Read data from mongo db """
    rack_data = RackData()
    rack_temperature = RackTemperature()
    raw_data_dict = rack_data.get_rack_temperature_data(rack_name)
    if raw_data_dict is None:
        return None
    
    dict_data = {}
    for rack_name in raw_data_dict:
        dict_data[rack_name] = {}
        for host in raw_data_dict[rack_name]:
            result = rack_temperature.parse_max_temp(raw_data_dict[rack_name][host], unit)
            dict_data[rack_name][host] = result["value"]
    return dict_data

if __name__ == '__main__':
    print "start"
    app.run(debug = True)