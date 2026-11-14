# Multi-Router Network Topology and Dynamic Routing

This lab experiment establishes an end-to-end multi-subnet routed network connecting two distinct LAN segments across a WAN Serial link using two Cisco routers (R1 and R2) configured with RIPv2.

---

## 1. Network Topology and Addressing Scheme

```text
[PC1: 192.168.1.100/24]
        |
    (Fa0/0) [192.168.1.1/24]
     [R1]
    (Se0/0/0) [10.0.0.1/8]
        |  WAN Link (DCE/DTE)
    (Se0/0/0) [10.0.0.2/8]
     [R2]
    (Fa0/0) [192.168.2.1/24]
        |
[PC2: 192.168.2.100/24]
```

### IP Address Allocation Table

| Device | Interface | IP Address | Subnet Mask | Default Gateway | Role |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **PC1** | FastEthernet0 | `192.168.1.100` | `255.255.255.0` | `192.168.1.1` | LAN 1 Host |
| **R1** | FastEthernet0/0 | `192.168.1.1` | `255.255.255.0` | N/A | LAN 1 Gateway |
| **R1** | Serial0/0/0 | `10.0.0.1` | `255.0.0.0` | N/A | WAN Link (DCE) |
| **R2** | Serial0/0/0 | `10.0.0.2` | `255.0.0.0` | N/A | WAN Link (DTE) |
| **R2** | FastEthernet0/0 | `192.168.2.1` | `255.255.255.0` | N/A | LAN 2 Gateway |
| **PC2** | FastEthernet0 | `192.168.2.100` | `255.255.255.0` | `192.168.2.1` | LAN 2 Host |

---

## 2. Configuration Steps

### A. Router 1 (R1) Configuration
```text
Router> enable
Router# configure terminal
Router(config)# hostname R1

! Configure LAN Interface
R1(config)# interface FastEthernet0/0
R1(config-if)# ip address 192.168.1.1 255.255.255.0
R1(config-if)# no shutdown
R1(config-if)# exit

! Configure WAN Serial Interface (DCE side requires clock rate)
R1(config)# interface Serial0/0/0
R1(config-if)# ip address 10.0.0.1 255.0.0.0
R1(config-if)# clock rate 64000
R1(config-if)# no shutdown
R1(config-if)# exit

! Configure Dynamic Routing (RIP v2)
R1(config)# router rip
R1(config-router)# version 2
R1(config-router)# no auto-summary
R1(config-router)# network 192.168.1.0
R1(config-router)# network 10.0.0.0
R1(config-router)# exit
R1(config)# end
R1# write memory
```

### B. Router 2 (R2) Configuration
```text
Router> enable
Router# configure terminal
Router(config)# hostname R2

! Configure LAN Interface
R2(config)# interface FastEthernet0/0
R2(config-if)# ip address 192.168.2.1 255.255.255.0
R2(config-if)# no shutdown
R2(config-if)# exit

! Configure WAN Serial Interface
R2(config)# interface Serial0/0/0
R2(config-if)# ip address 10.0.0.2 255.0.0.0
R2(config-if)# no shutdown
R2(config-if)# exit

! Configure Dynamic Routing (RIP v2)
R2(config)# router rip
R2(config-router)# version 2
R2(config-router)# no auto-summary
R2(config-router)# network 192.168.2.0
R2(config-router)# network 10.0.0.0
R2(config-router)# exit
R2(config)# end
R2# write memory
```

---

## 3. End-to-End Verification

1. **Routing Table Inspection**:
   Execute `show ip route` on R1:
   ```text
   R 192.168.2.0/24 [120/1] via 10.0.0.2, 00:00:14, Serial0/0/0
   ```
   R1 shows learned route `192.168.2.0/24` with hop count metric `1` and administrative distance `120`.

2. **Connectivity Test**:
   From PC1 command prompt:
   ```text
   PC1> ping 192.168.2.100
   ```
   All ICMP Echo Requests receive Echo Replies (`Reply from 192.168.2.100: bytes=32 time=12ms TTL=126`).
