ip link set eth2 promisc on
ethtool -K eth1 gro off lro off
ip link set eth3 promisc on
ethtool -K eth2 gro off lro off
