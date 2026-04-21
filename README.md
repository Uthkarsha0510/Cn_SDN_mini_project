Here’s a **clean, GitHub-ready README.md** (proper markdown, no extra IDs, formatted like your reference):

---

# ARP Handling in SDN Networks (Proxy ARP using POX)

## Problem Statement

In traditional networks, ARP requests are broadcast across the network, causing unnecessary traffic and inefficiency. This project aims to optimize ARP handling in an SDN environment by reducing broadcast overhead using a centralized controller.

## Objective

This project demonstrates:

* Efficient ARP handling using **Proxy ARP**
* Controller–switch interaction in SDN
* Reduction of broadcast traffic
* Dynamic learning of IP–MAC mappings
* Flow rule installation for optimized forwarding

## Technologies Used

* Mininet (Network Emulator)
* POX Controller (SDN Controller)
* OpenFlow Protocol
* Python

## System Architecture

Mininet (Hosts + Switch) → OpenFlow Switch → POX Controller → ARP Handler → Optimized Forwarding

---

## Project Structure

```
.
├── topology.py
└── pox/ext/
    └── arp_handler.py
```

---

## Setup Instructions

### 1. Install Mininet

```bash
sudo apt update
sudo apt install mininet -y
```

### 2. Install POX Controller

```bash
git clone https://github.com/noxrepo/pox ~/pox
```

### 3. Verify Python

```bash
python3 --version
```

---

## How To Run

### 1. Run POX Controller

```bash
cd ~/pox
python3 pox.py arp_handler
```

### 2. Start Mininet Topology

```bash
sudo python3 topology.py
```

---

## Working Mechanism

### 1) Topology

* 4 hosts (h1–h4) connected to a single switch (s1)
* Switch connected to POX controller

### 2) Packet Handling

* Unknown packets → sent to controller (Packet-In)
* Controller learns:

  * MAC → Port
  * IP → MAC

### 3) Proxy ARP

* If IP is known → Controller sends ARP reply directly
* If unknown → Request is flooded

### 4) Flow Rules

* Installed after first communication
* Reduces controller involvement for future packets

## Test Scenarios

### Host Communication

```
mininet> h1 ping h2 -c 4
mininet> h3 ping h4 -c 4
```

### Full Connectivity

```
mininet> pingall
```

### Throughput Test

```
mininet> iperf h1 h2
```

### Flow Table Check

```
mininet> sh ovs-ofctl dump-flows s1
```

---

## Expected Results

* 0% packet loss between hosts
* ARP handled without unnecessary flooding
* Controller logs:

  ```
  Learned: 10.0.0.1 is at <MAC>
  Proxy ARP Reply Sent
  ```
* Flow rules dynamically installed in switch

---

## Conclusion

This project demonstrates how **Proxy ARP in SDN** improves network efficiency by reducing broadcast traffic and enabling intelligent forwarding using a centralized controller.

## References

* [http://mininet.org](http://mininet.org)
* [https://noxrepo.github.io/pox-doc/html/](https://noxrepo.github.io/pox-doc/html/)
* [https://opennetworking.org](https://opennetworking.org)

---

If you want, I can next:

* Add **actual screenshots formatting like your reference repo**
* Or make a **diagram image for architecture (looks very good on GitHub)**
