from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.cli import CLI  # <--- CHANGE 1: ADD THIS IMPORT

class SimpleTopo(Topo):
    def build(self):
        # add 1 switch
        s1 = self.addSwitch('s1')
        
        # add 4 hosts and link them to the switch
        for i in range(1, 5):
            h = self.addHost(f'h{i}')
            self.addLink(h, s1)

def run():
    topo = SimpleTopo()
    # RemoteController points to POX running on localhost
    net = Mininet(topo=topo, controller=RemoteController('c0', ip='127.0.0.1', port=6633))
    net.start()
    
    
    CLI(net)
    
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    run()
