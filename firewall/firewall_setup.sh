ip link set eth1 promisc on
ethtool -K eth1 gro off lro off
ip link set eth2 promisc on
ethtool -K eth2 gro off lro off
ip link set eth4 promisc on
ethtool -K eth4 gro off lro off
