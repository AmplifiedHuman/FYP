#!/bin/bash
docker start client
docker start firewall
ovs-docker del-port ovs-br1 eth1 client
ovs-docker add-port ovs-br1 eth1 client --ipaddress=192.168.0.2/24
ovs-docker del-port ovs-br1 eth1 firewall
ovs-docker add-port ovs-br1 eth1 firewall --ipaddress=192.168.0.3/24