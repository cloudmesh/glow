#!/usr/bin/env python

from flask import Flask, jsonify

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
    return jsonify( { 'glow': nop } )


@app.route('/cm/v1.0/glow/t/<cluster>', methods = ['GET'])
def get_cluster_temperatures(cluster):
    """returns the temperatures of all servers in the cluster with the given label"""
    return jsonify( { 'glow': nop } )


@app.route('/cm/v1.0/glow/t/<cluster>/<server>', methods = ['GET'])
def get_cluster_temperatures(cluster):
    """returns the temperatures of a named servers in the cluster with the given label"""
    return jsonify( { 'glow': nop } )


if __name__ == '__main__':
    print "start"
    app.run(debug = True)