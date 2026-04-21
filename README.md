# ARP Handling in SDN Networks

## Overview
This project implements ARP request and reply handling using an SDN controller (POX) and Mininet. Instead of flooding ARP requests across the network, the controller intercepts them, maintains an ARP table, and replies directly — a technique called **Proxy ARP**. This enables efficient host discovery and validates end-to-end communication.

---

## Project Structure
```
.
├── topology.py
└── pox/ext/
    └── arp_handler.py
```

---

## How It Works

### `topology.py`
Creates a simple Mininet network with 4 hosts (h1–h4) connected to a single switch (s1). The switch connects to the POX controller running on localhost port 6633.

### `pox/ext/arp_handler.py`
The core controller logic. Key components:

- **`ARPHandler.__init__`** — Initializes two tables: `arp_table` (IP→MAC) and `port_table` (MAC→port). Registers event listeners on the switch connection.

- **`_handle_PacketIn`** — Main entry point. Called whenever the switch doesn't know what to do with a packet. Learns the source host's MAC and port, then dispatches based on packet type (ARP or IP).

- **`send_arp_reply`** — Handles ARP requests. Looks up the target IP in the ARP table and sends a crafted ARP reply back to the requester without flooding. If the target is unknown, falls back to flooding.

- **`install_flow_rule`** — Once a destination is known, installs a flow rule in the switch so future packets are forwarded locally without hitting the controller.

- **`resend_packet`** — Sends a raw packet out of a specified switch port.

---

## Setup & Requirements

- Ubuntu 22.04
- Mininet: `sudo apt install mininet`
- POX: `git clone https://github.com/noxrepo/pox ~/pox`
- Python 3

Place `arp_handler.py` inside `~/pox/ext/`.

---

## Running the Project

**Terminal 1 — Start the controller:**
```bash
cd ~/pox
python3 pox.py arp_handler
```

**Terminal 2 — Start the topology:**
```bash
sudo python3 topology.py
```

---

## Test Scenarios

**Scenario 1 — Host communication via ARP:**
```
mininet> h1 ping h2 -c 4
mininet> h3 ping h4 -c 4
```
Expected: Successful ping. POX logs ARP mappings learned.

**Scenario 2 — Full mesh reachability:**
```
mininet> pingall
```
Expected: All hosts reachable (0% drop).

**Scenario 3 — Throughput measurement:**
```
mininet> iperf h1 h2
```
Expected: Throughput reported in Mbits/sec.

**Flow table inspection:**
```
mininet> sh ovs-ofctl dump-flows s1
```
Expected: Flow rules installed after first ping.

---

## Expected Output

- POX terminal logs: `Learned: 10.0.0.1 is at <MAC>` and `Proxy ARP reply` messages
- Ping RTT in milliseconds
- Flow rules with match criteria and output port actions
- iperf bandwidth between hosts

---

## References
- [Mininet Documentation](http://mininet.org)
- [POX Documentation](https://noxrepo.github.io/pox-doc/html/)
- [OpenFlow 1.0 Specification](https://opennetworking.org/wp-content/uploads/2013/04/openflow-spec-v1.0.0.pdf)
