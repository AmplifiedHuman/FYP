#!/bin/bash
docker start client
docker start firewall
docker start snort
ovs-docker del-port ovs-br1 eth1 client
ovs-docker add-port ovs-br1 eth1 client --ipaddress=192.168.0.2/24
ovs-docker del-port ovs-br1 eth1 firewall
ovs-docker add-port ovs-br1 eth1 firewall --ipaddress=192.168.0.3/24
ovs-docker del-port ovs-br2 eth2 firewall
ovs-docker add-port ovs-br2 eth2 firewall --ipaddress=192.168.1.2/24
ovs-docker del-port ovs-br2 eth2 snort
ovs-docker add-port ovs-br2 eth2 snort --ipaddress=192.168.1.3/24