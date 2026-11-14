# Router Basic Configuration and RIP Protocol

This lab guide details the step-by-step Cisco IOS commands used to configure a single Cisco router interface and activate Routing Information Protocol version 2 (RIPv2).

---

## 1. Cisco IOS Command Modes Overview

Cisco IOS uses a hierarchical command mode structure:
- **User EXEC Mode** (`Router>`): Basic monitoring and status viewing.
- **Privileged EXEC Mode** (`Router#`): Advanced verification, file operations, debugging, and configuration entry.
- **Global Configuration Mode** (`Router(config)#`): System-wide parameter settings.
- **Interface Configuration Mode** (`Router(config-if)#`): Specific physical/logical interface settings.
- **Router Configuration Mode** (`Router(config-router)#`): Dynamic routing protocol settings.

---

## 2. Step-by-Step IOS Commands

### A. Entering Privileged and Global Configuration Mode
```text
Router> enable
Router# configure terminal
Enter configuration commands, one per line. End with CNTL/Z.
Router(config)#
```

### B. Configuring GigabitEthernet Interface
Assign IPv4 address `192.168.1.1/24` to interface `GigabitEthernet 0/0/0` and bring it up:
```text
Router(config)# interface gigabitEthernet 0/0/0
Router(config-if)# ip address 192.168.1.1 255.255.255.0
Router(config-if)# no shutdown
Router(config-if)# exit
```

### C. Activating RIP Routing (Version 2)
Activate RIP, specify version 2 (to enable classless routing and subnet mask propagation), and advertise the local network:
```text
Router(config)# router rip
Router(config-router)# version 2
Router(config-router)# network 192.168.1.0
Router(config-router)# exit
Router(config)# end
```

---

## 3. Verification and Inspection Commands

### A. Display System and Hardware Version
```text
Router# show version
```
Displays Cisco IOS Software release, uptime, ROMMON bootloader version, processor specs, and memory allocation.

### B. Verify Routing Protocol Parameters
```text
Router# show ip protocols
```
Output confirms:
- **Routing Protocol**: "rip"
- **Update Timer**: Sending updates every 30 seconds
- **Invalid Timer**: 180 seconds; **Flushed**: 240 seconds
- **Default Version Control**: Send version 2, receive version 2
- **Routing for Networks**: `192.168.1.0`
- **Administrative Distance**: 120 (standard default for RIP)

### C. Verify Active Routing Table
```text
Router# show ip route
```
Lists directly connected subnets (`C`), local interface addresses (`L`), and dynamically learned routes (`R`).
