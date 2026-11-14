# Computer Networks: Comprehensive Theoretical and Technical Reference Guide

This document serves as an exhaustive, structured technical reference covering foundational computer networking principles, protocol mechanics, the Berkeley socket API, concurrent server architectures, routing algorithms, packet analysis, and practical lab implementations.

---

## Table of Contents

- [1. Network Architectures, Topologies & Layered Models](#1-network-architectures-topologies--layered-models)
- [2. Physical & Data Link Layer (MAC, Framing, Switches, VLANs, CSMA)](#2-physical--data-link-layer-mac-framing-switches-vlans-csma)
- [3. Network Layer, IP Addressing & Subnetting (IPv4, IPv6, CIDR, ARP, ICMP)](#3-network-layer-ip-addressing--subnetting-ipv4-ipv6-cidr-arp-icmp)
- [4. Routing Protocols & Autonomous Systems (RIP, OSPF, BGP, Routing Tables)](#4-routing-protocols--autonomous-systems-rip-ospf-bgp-routing-tables)
- [5. Transport Layer Mechanics & Protocols (TCP, UDP, Handshakes, Flow & Congestion Control)](#5-transport-layer-mechanics--protocols-tcp-udp-handshakes-flow--congestion-control)
- [6. Application Layer Protocols (DNS, HTTP, SMTP, POP3, IMAP, DHCP)](#6-application-layer-protocols-dns-http-smtp-pop3-imap-dhcp)
- [7. Socket Programming Architecture & Berkeley Sockets API](#7-socket-programming-architecture--berkeley-sockets-api)
- [8. Concurrency, I/O Multiplexing & Raw Sockets (Threads, Processes, select/poll/epoll)](#8-concurrency-io-multiplexing--raw-sockets-threads-processes-selectpollepoll)
- [9. Network Security, QoS & Diagnostic Tools (Wireshark, ping, traceroute, ip)](#9-network-security-qos--diagnostic-tools-wireshark-ping-traceroute-ip)
- [10. Lab Experiments & Socket Programming Implementations](#10-lab-experiments--socket-programming-implementations)

---

## 1. Network Architectures, Topologies & Layered Models

### Q1. What is a computer network?

A set of interconnected devices, such as computers, routers, and switches, that exchange data and share resources using common protocols.

### Q2. What is a protocol?

A set of rules that de ne the format, order, and actions of messages between communicating parties.

### Q3. What is the client-server model?

A model in which a server waits for requests and provides a service, and a client starts the communication by sending requests.

### Q4. What is a host?

Any device on a network that has an IP address and can send or receive data.

### Q5. What is a LAN, MAN, and W AN?

LAN (Local Area Network) covers a building or campus. MAN (Metropolitan Area Network) covers a city. W AN (Wide Area Network) covers large geographic areas, such as the Internet.

### Q6. What is a gateway?

A device that connects two networks that use dierent protocols or architectures. A router can act as a gateway. 12.2 Addressing

### Q7. What is the full form of IP?

Internet Protocol.

### Q8. What does ow control do?

It stops a fast sender from overwhelming a slow receiver. TCP uses a receive window for this.

### Q9. What does congestion control do?

It reduces the sending rate when the network is congested, to avoid packet loss. TCP uses it. UDP does not. 12.4 Layers and Encapsulation

### Q10. List the seven OSI layers.

Application, Presentation, Session, Transport, Network, Data Link, Physical (top to bottom).

### Q11. Which layer does IP belong to?

The Network layer (layer 3).

### Q12. What is encapsulation?

Adding a header at each layer as data moves down the stack. Data becomes a segment (TCP) or datagram (UDP), then a packet (IP), then a frame (Ethernet), then bits.

### Q13. What is a frame?

A unit of data at the Data Link layer, such as an Ethernet frame. It carries MAC addresses.  12.5 Networking Commands

### Q14. What is TTL?

Time To Live. A counter in the IP header that each router decrements. When it reaches zero, the packet is dropped. This prevents endless loops.

### Q15. What does ipcong or ifcong show?

IP address, MAC address, and other interface settings for the computer. 12.6 Python Socket Programming

### Q16. What does close() do?

It closes the socket and releases the port.

### Q17. Why must the server start before the client?

The client's connect() needs a listening server. Otherwise it fails with connection refused.

### Q18. Why does a server need concurrency?

A simple server handles one client at a time. With concurrency, it serves many clients at once, so one slow client does not block the others.

### Q19. What are the common ways to build a concurrent server?

Threads (one thread per client), processes (one process per client, for example with multiprocess- ing or fork), and event-driven methods such as select or asyncio.

### Q20. What is the dierence between a thread and a process?

A thread runs inside a process and shares its memory. A process has its own memory space and its own PID. Processes are safer but heavier.

### Q21. What is the GIL?

The Global Interpreter Lock in CPython. Only one thread runs Python bytecode at a time. For network-bound work like socket servers, threads are still useful because they wait on I/O.

### Q22. What is a daemon thread?

A thread that stops automatically when the main program exits. Chat handler threads use it so the server can shut down cleanly.

### Q23. What does broadcast mean in a chat server?

Sending each message to every connected client except the one who sent it.

### Q24. Why is a lock used in the chat server?

Several threads read and change the shared list of clients. A lock prevents two threads from changing the list at the same time, which could corrupt it.

### Q25. Why does the chat client use two threads?

One thread waits for keyboard input, and the other waits for messages from the server. Without two threads, the program would block on one of these operations.

### Q26. Why does the multi-client chat server need threading instead of a loop?

A loop handles one client's recv() at a time. The loop would block on the rst client and never accept others. A thread for each client avoids this. 12.9 Lab Programs

### Q27. Program 1: what happens with a negative input?

The factorial is not de ned for negative numbers. The server sends an error message.

### Q28. What is multiplexing and demultiplexing?

Multiplexing combines data from several sockets into one stream at the sender. Demultiplexing uses the port number at the receiver to deliver each segment to the correct socket.

### Q29. What are the hello and dead intervals?

Hello 10 seconds and dead 40 seconds on broadcast and point-to-point networks (30 and 120 seconds on NBMA). They must match between neighbours.

### Q30. Explain the architecture of electronic mail.

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

The system consists of user agents (UA), message transfer agents (MTA) and mailboxes. The sender's UA pushes the mail to its mail server using SMTP, the MTAs relay it using SMTP to the recipient's mail server, and the recipient's UA retrieves it using POP3 or IMAP (or HTTP for webmail).

### Q31. What is the difference between recursive and iterative queries?

*(Topic: = zero or more (NS records), Additional = zero or more (glue records or OPT).)*

In a recursive query the resolver does the entire work and returns the final answer. In an iterative query the server returns a referral to another server and the client keeps asking.

### Q32. How many question, answer, authority and additional records are in a typical query?

*(Topic: Wireshark based)*

Question = 1, Answer = 0, Authority = 0, Additional = 0 (0 or 1 if an EDNS OPT record is added).

### Q33. What is the purpose of the Transaction ID field?

*(Topic: Wireshark based)*

It is a 16-bit identifier chosen by the client and copied into the reply so that the client can match a response with the query it sent. The query and response ID numbers are identical.

### Q34. What is the difference between a process and a program?

*(Topic: Socket programming based)*

A program is a passive file on disk; a process is an executing instance of a program with its own PID, memory and resources.

### Q35. Compare pure ALOHA and slotted ALOHA.

*(Topic: DLC, MAC protocols, addressing, Ethernet, connecting devices, WLAN, Mobile IP, packet interface)*

Pure ALOHA: stations transmit at any time; vulnerable time = 2T; maximum throughput = 1/(2e)

### Q36. How do you remove an ACL?

*(Topic: Cisco Packet Tracer based)*

First remove it from the interface with no ip access-group 10 out, then delete it with no access-list 10.

### Q37. How do you parse the captured packet?

*(Topic: Socket programming based)*

Cast the buffer to struct ethhdr for the Ethernet header, then to struct iphdr (after 14 bytes) for the IP header, and then to struct tcphdr, udphdr or icmphdr depending on the protocol field. Print the source/destination MAC, IP and ports.

### Q38. What is a protocol? What are its key elements?

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

A protocol is a set of rules for communication between entities. Its three key elements are syntax (format of data), semantics (meaning of each field) and timing (when and how fast data is sent).

### Q39. How would you allow only Host_B to reach network 172.16.10.0?

*(Topic: Cisco Packet Tracer based)*

Create a standard ACL, for example access-list 10 permit host <IP of Host_B>, and apply it on the router interface connected to 172.16.10.0 in the outbound direction: interface f0/0 / ip access-group 10 out. Everything else is dropped by the implicit deny.

### Q40. What is the meaning of 2001:DB8:1111:1::/64?

*(Topic: Cisco Packet Tracer based)*

It is the network prefix: the first 64 bits are the network/subnet portion (2001:DB8:1111 is the site prefix and 1 is the subnet ID) and the remaining 64 bits are the interface ID.

### Q41. What are the byte ordering and address conversion functions?

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

htons/htonl/ntohs/ntohl convert between host and network byte order. inet_pton() and inet_ntop() convert between the presentation (text) and numeric forms of IPv4/IPv6 addresses.

### Q42. What is the difference between ip addr and ip route?

*(Topic: Warm up)*

ip addr shows or configures the addresses assigned to interfaces. ip route shows or modifies the kernel routing table (for example the default gateway).

### Q43. What are the different memory types in a Cisco router?

*(Topic: Cisco Packet Tracer based)*

ROM (bootstrap/POST), Flash (IOS image), RAM (running config, routing tables, ARP cache), NVRAM (startup config).

### Q44. What is the EtherType field?

*(Topic: Socket programming based)*

A 2-byte field in the Ethernet header identifying the upper-layer protocol, for example 0x0800 = IPv4, 0x0806 = ARP, 0x86DD = IPv6.

### Q45. Which command displays the router's model, IOS version, memory and interfaces?

*(Topic: Cisco Packet Tracer based)*

show version. It shows the IOS image, uptime, RAM, NVRAM and flash size, number of interfaces and configuration register.

### Q46. Why must routes be configured in both directions?

*(Topic: Cisco Packet Tracer based)*

For ping to work, the ICMP echo request must reach the destination and the echo reply must find its way back. If the return route is missing, the ping fails.

### Q47. What is the difference between running-config and startup-config?

*(Topic: Cisco Packet Tracer based)*

running-config is the active configuration stored in RAM and is lost on reload. startup-config is stored in NVRAM and is loaded at boot.

### Q48. Why is the no shutdown command needed?

*(Topic: Cisco Packet Tracer based)*

Router interfaces are administratively down by default. no shutdown enables the interface.

### Q49. What is the Router ID and how is it chosen?

A 32-bit identifier of the OSPF router. It is chosen from the manually configured router-id, otherwise the highest loopback IP, otherwise the highest active interface IP.

### Q50. What is Mobile IP? Explain its entities and operation.

*(Topic: = 1/e = 36.8%.)*

Mobile IP lets a host keep its IP address while moving between networks. Entities: mobile node, home agent (HA), foreign agent (FA), home address and care-of address (COA). Phases: agent discovery, registration, and data transfer with tunnelling (HA intercepts the packet, encapsulates it to the COA and the FA/host decapsulates it).

### Q51. What are the source and destination ports of the query and the response?

*(Topic: Wireshark based)*

Query: source is a random ephemeral port, destination is 53. Response: source is 53, destination is the ephemeral port of the query.

### Q52. What is the difference between a capture filter and a display filter?

*(Topic: Wireshark based)*

A capture filter (BPF syntax) restricts which packets are recorded while capturing. A display filter, such as http, hides packets from the view after capturing without deleting them.

### Q53. What is static routing?

*(Topic: Cisco Packet Tracer based)*

Routes are configured manually by the administrator and do not change automatically when the topology changes.

### Q54. Why are root privileges required?

*(Topic: Socket programming based)*

Raw sockets allow reading and forging packets, which is a security risk. Linux requires root or the CAP_NET_RAW capability.

### Q55. Explain the IEEE 802.11 architecture.

*(Topic: = 1/e = 36.8%.)*

The basic service set (BSS) is a group of stations with an optional access point (AP). Infrastructure mode has an AP; ad hoc mode has none. Several BSSs are connected via a distribution system to form an extended service set (ESS). Standards: 802.11a/b/g/n/ac/ax.

### Q56. What are the types of ACLs?

*(Topic: Cisco Packet Tracer based)*

Standard ACLs (numbers 1-99 and 1300-1999) filter only by source IP address. Extended ACLs (100-199 and 2000-2699) filter by source, destination, protocol and port. Named ACLs may be either type.

### Q57. What are the functions of the data-link layer?

*(Topic: DLC, MAC protocols, addressing, Ethernet, connecting devices, WLAN, Mobile IP, packet interface)*

Framing, physical addressing, error control, flow control, access control (MAC), and node-to-node delivery. It has two sublayers: Data Link Control (DLC) and Media Access Control (MAC).

### Q58. What are cookies and how do they work?

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

Cookies are small pieces of state data stored by the browser. The server sends a Set-Cookie header with a unique ID in the response, the browser stores it and includes the Cookie header in later requests, allowing the server to track sessions.

### Q59. What information does netstat give? Give a useful option combination.

*(Topic: Warm up)*

netstat displays active connections, listening ports, routing tables and interface statistics. For example netstat -tuln lists listening TCP and UDP ports in numeric form; netstat -r shows the routing table. The modern replacement is ss.

### Q60. What are multiple access protocols? Classify them.

*(Topic: DLC, MAC protocols, addressing, Ethernet, connecting devices, WLAN, Mobile IP, packet interface)*

Protocols to share a broadcast channel: random access (ALOHA, CSMA, CSMA/CD, CSMA/CA), controlled access (reservation, polling, token passing) and channelisation (FDMA, TDMA, CDMA).

### Q61. What are the advantages and disadvantages of static routing?

*(Topic: Cisco Packet Tracer based)*

Advantages: no protocol overhead, secure, predictable, simple in small networks. Disadvantages: no automatic adaptation to failures and hard to manage in large networks.

### Q62. To which class does the address 140.80.0.0 belong and what is its default mask?

*(Topic: Cisco Packet Tracer based)*

Class B (first octet 128-191), default mask 255.255.0.0 (/16).

### Q63. What is convergence?

*(Topic: Cisco Packet Tracer based)*

The state when all routers have consistent routing information after a change.

### Q64. What is the implicit deny?

*(Topic: Cisco Packet Tracer based)*

Every ACL ends with an invisible 'deny any' statement. Any packet that does not match a permit statement is dropped.

### Q65. What is NAT and how does it work?

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Network Address Translation maps private addresses to one or more public addresses. With port address translation (PAT), a translation table maps (private IP, port) to (public IP, new port) for outgoing packets and reverses for incoming ones.

### Q66. What is IMF?

*(Topic: <CRLF>.<CRLF>. 221: service closing the transmission channel. Also 550 means mailbox unavailable and 421 means service not available.)*

Internet Message Format (RFC 5322) defines the structure of an e-mail message: header lines (From, To, Subject, Date, Message-ID) followed by a blank line and the body. The IMF packet carries the actual message you typed.

### Q67. What is the difference between nslookup and dig?

*(Topic: Warm up)*

Both query DNS servers. nslookup is simpler and works interactively; dig gives detailed output of the DNS message sections and is preferred for troubleshooting. nslookup www.example.com returns the IP address of the domain.

### Q68. How can zombies be avoided?

*(Topic: Socket programming based)*

Use a SIGCHLD handler that calls waitpid(-1, NULL, WNOHANG) in a loop.

### Q69. What is promiscuous mode?

*(Topic: Socket programming based)*

A mode in which the network interface accepts all frames on the wire and not just those addressed to its own MAC address. It is set with ioctl() (SIOCSIFFLAGS with IFF_PROMISC) or via libpcap.

### Q70. Why is 'permit ip any any' needed?

*(Topic: 140.80.127.255.)*

Because of the implicit deny at the end of every ACL. Without it all other traffic, including other services from the server, would also be blocked.

### Q71. What is nmap and where is it used?

*(Topic: Warm up)*

nmap is a network scanner used for host discovery, port scanning, service and OS detection. It is used by administrators for security audits. It must only be used on networks you are authorised to scan.

### Q72. What is the difference between multiplexing and demultiplexing?

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

Multiplexing: the sender's transport layer gathers data from several processes and adds headers with port numbers. Demultiplexing: the receiver's transport layer uses the port numbers to deliver segments to the correct process.

### Q73. How do you find the length of the IP header?

*(Topic: Socket programming based)*

The IHL field (4 bits) gives the header length in 32-bit words. Header length in bytes = IHL x 4 (minimum 20).

### Q74. What is the use of the whois command?

*(Topic: Warm up)*

whois queries the registration database of a domain or IP block and returns details such as registrar, registrant, creation and expiry dates and name servers.

### Q75. What is mtr?

*(Topic: Warm up)*

mtr (My Traceroute) combines the functions of ping and traceroute. It continuously probes each hop and displays packet loss and latency statistics per hop.

### Q76. What is the effect of the order of statements in an ACL?

*(Topic: Cisco Packet Tracer based)*

The router checks from top to bottom and stops at the first match, so more specific statements must be placed before general ones.

### Q77. What is a floating static route?

*(Topic: Cisco Packet Tracer based)*

A static route configured with a higher administrative distance (for example ip route ... 200) so that it is used only when the primary (dynamic) route fails.

### Q78. What is the server's IP address?

*(Topic: 140.80.127.255.)*

Taking the 7th usable host address in the 16th subnet, it is 140.80.120.7. If the address count starts at the network address (0th = network), the 7th address would be 140.80.120.6. State the assumption clearly.

### Q79. What is the difference between a concurrent and an iterative server?

*(Topic: Basics to revise before all experiments)*

An iterative server handles one client at a time. A concurrent server handles several clients simultaneously using fork(), threads, or I/O multiplexing (select/poll/epoll).

### Q80. How do you save the running configuration?

*(Topic: Cisco Packet Tracer based)*

copy running-config startup-config (or write memory / wr).

### Q81. What is the difference between inbound and outbound ACL?

*(Topic: Cisco Packet Tracer based)*

Inbound filters packets as they enter the interface, before routing. Outbound filters packets after routing, as they leave the interface.

### Q82. What is encapsulation and decapsulation?

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

Encapsulation is the addition of a header (and sometimes trailer) at each layer as data moves down the stack at the sender. Decapsulation is the removal of these headers as data moves up the stack at the receiver.

### Q83. What is the difference between show interfaces and show ip interface brief?

*(Topic: Cisco Packet Tracer based)*

show interfaces gives detailed statistics for each interface (MTU, bandwidth, errors, counters, encapsulation). show ip interface brief gives a one-line summary with the IP address and status (up/down) of each interface.

### Q84. Which type of ACL is required and why?

*(Topic: 140.80.127.255.)*

An extended ACL, because the requirement depends on the source subnet, destination host and the TCP port (application), which a standard ACL cannot match.

### Q85. What is the difference between using sendto()/recvfrom() and send()/recv()?

*(Topic: Socket programming based)*

sendto() and recvfrom() carry the peer address with every datagram, which is needed in an unconnected UDP socket. send() and recv() require a connected socket.

### Q86. What are the services provided by the transport layer?

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

Process-to-process delivery using port numbers, encapsulation/decapsulation, multiplexing and demultiplexing, flow control, error control, congestion control, and connection-oriented or connectionless delivery.

### Q87. How do you configure a serial interface with an IP address and clock rate?

*(Topic: Cisco Packet Tracer based)*

Router(config)# interface serial 0 / Router(config-if)# ip address 192.168.1.1 255.255.255.0 / clock rate 64000 (on the DCE end only) / no shutdown.

### Q88. What is MIME?

*(Topic: <CRLF>.<CRLF>. 221: service closing the transmission channel. Also 550 means mailbox unavailable and 421 means service not available.)*

Multipurpose Internet Mail Extensions allow e-mail to carry non-ASCII text and attachments such as images and files by defining content types and encodings like base64.

### Q89. Which standard protocol is similar to this experiment? Which port does it use?

*(Topic: Socket programming based)*

The Daytime protocol (RFC 867) on port 13 and the Time protocol (RFC 868) on port 37. Modern systems use NTP on UDP port 123.

### Q90. How many records are in the response?

*(Topic: Wireshark based)*

Question = 1 (copied), Answer = one or more (for example a CNAME and A records), Authority

### Q91. How do you find whether a serial interface is DTE or DCE?

*(Topic: Cisco Packet Tracer based)*

Use show controllers serial 0 (for example). The output states DCE cable or DTE cable. The DCE end provides the clock.

### Q92. How does the server check if the requested file exists?

*(Topic: Socket programming based)*

By trying to open it with open() or fopen(); if it returns -1 or NULL (errno = ENOENT), the file does not exist. access() or stat() can also be used.

### Q93. Why do we clear the browser cache before capturing?

*(Topic: Wireshark based)*

So that the browser sends fresh GET requests to the server instead of serving the page from its cache. Otherwise the request may be a conditional GET or may not be sent at all.

### Q94. Why is no auto-summary used?

*(Topic: Cisco Packet Tracer based)*

By default RIPv2 summarises routes at classful boundaries, which breaks discontiguous subnets. no auto-summary disables this.

### Q95. Which command shows the active routing protocols?

*(Topic: Cisco Packet Tracer based)*

show ip protocols. It shows the protocol, timers, networks advertised, neighbours and administrative distance.

### Q96. What does iftop show?

*(Topic: Warm up)*

iftop shows real-time bandwidth usage on an interface, listing connections between pairs of hosts with their send and receive rates. It works like top but for network traffic.

### Q97. What is a port number? Give the ranges.

*(Topic: Basics to revise before all experiments)*

A 16-bit number that identifies a process on a host. Well-known ports are 0- 1023, registered ports are 1024-49151, and dynamic/ephemeral ports are 49152-65535 (Linux uses 32768-60999 by default).

### Q98. What is the count-to-infinity problem?

*(Topic: Cisco Packet Tracer based)*

In distance-vector protocols, routers gradually increase the metric to an unreachable network through mutual updates. RIP limits this problem by making 16 the infinity value.

### Q99. How would you translate the abbreviations in the received sentence?

*(Topic: Socket programming based)*

Split the sentence into words (strtok() or manual parsing), compare each word with a lookup table of abbreviations, replace matches with the full form and join the words again. Punctuation attached to a word (for example 'atm,') must be handled.

### Q100. What are the differences between the client-server and P2P paradigms?

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

In client-server, the server is centralised, always on, has a fixed address and is a bottleneck and a single point of failure. In P2P, resources are shared by peers, the system is scalable and robust, but management and security are harder.

### Q101. What is the difference between routing and forwarding?

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Forwarding is moving a packet from an input port to an output port using the forwarding table. Routing is determining the route (path) from source to destination using routing algorithms and building the forwarding table.

### Q102. Where should standard and extended ACLs be placed?

*(Topic: Cisco Packet Tracer based)*

Standard ACLs close to the destination (because they only check the source). Extended ACLs close to the source (to stop unwanted traffic early).

### Q103. What is multicasting? Explain IGMP.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Multicasting sends a packet to a group of hosts identified by a class D address. IGMP (Internet Group Management Protocol) lets hosts inform the local router about the groups they wish to join or leave (membership query, report, leave).

### Q104. What is the difference between getpid() and getppid()?

*(Topic: Socket programming based)*

getpid() returns the process ID of the calling process and getppid() returns the ID of its parent.

### Q105. What are the different Cisco IOS modes and their prompts?

*(Topic: Cisco Packet Tracer based)*

User EXEC mode: Router>. Privileged EXEC mode: Router#. Global configuration mode: Router(config)#. Interface configuration mode: Router(config-if)#. Others: line (config-line)# and router (config-router)#.

### Q106. Which flag bits are set only in a response message?

*(Topic: Wireshark based)*

QR = 1, AA (authoritative answer), RA (recursion available) and the RCODE (response code, for example 0 = no error, 3 = NXDOMAIN). RD (recursion desired) is set by the client and copied back.

### Q107. Write the ACL to block the website access from CCF only.

*(Topic: 140.80.127.255.)*

access-list 101 deny tcp 140.80.24.0 0.0.7.255 host 140.80.120.7 eq 80 / (also eq 443 if HTTPS is used) / access-list 101 permit ip any any. Apply it inbound on the router interface facing CCF: ip access-group 101 in.

### Q108. What is a peer-to-peer network? Differentiate between structured and unstructured P2P.

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

A network in which peers directly share resources. Unstructured P2P (such as Gnutella) uses flooding to find files, and structured P2P (such as Chord, Kademlia) uses a Distributed Hash Table (DHT) to map keys to peers deterministically for efficient lookup.

### Q109. What does the ifconfig command do? Which command replaces it?

*(Topic: Warm up)*

ifconfig displays and configures network interfaces (IP address, netmask, MAC address, MTU, RX/TX packet counts). It is deprecated and replaced by the ip command (for example ip addr show).

### Q110. How do you find how long it took from the GET message to the response?

*(Topic: Wireshark based)*

Subtract the time value of the GET packet from the time value of the corresponding HTTP response packet in the Time column of Wireshark.

### Q111. Explain the transparent bridge (learning bridge) and spanning tree protocol (STP).

*(Topic: = 1/e = 36.8%.)*

A transparent bridge learns source addresses to build a forwarding table, floods frames for unknown destinations and filters the rest. STP removes loops in redundant topologies by electing a root bridge and blocking redundant ports to make a loop-free tree.

### Q112. What is a default route and how is it configured?

*(Topic: Cisco Packet Tracer based)*

A route that matches all destinations not in the routing table: ip route 0.0.0.0 0.0.0.0 <next-hop>. It is used at stub networks.

### Q113. How do you verify that static routing works?

*(Topic: Cisco Packet Tracer based)*

show ip route (S entries) and ping from a host or router to remote networks; traceroute (tracert) can confirm the path.

### Q114. What is a link-local address?

*(Topic: Cisco Packet Tracer based)*

An address of the form FE80::/10 that is automatically generated on each IPv6- enabled interface. It is valid only on the local link and is used for neighbour discovery and as the next hop by routing protocols.

### Q115. How does the server know where to send the reply?

*(Topic: Socket programming based)*

recvfrom() fills a sockaddr structure with the client's IP address and port, which is passed to sendto() when replying.

### Q116. What are the I/O models in Unix?

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

Blocking, non-blocking, I/O multiplexing (select/poll), signal-driven I/O (SIGIO) and asynchronous I/O (aio_).

### Q117. What are SMI and MIB?

*(Topic: SNMP, ASN.1, data and signals, transmission, bandwidth, media)*

SMI (Structure of Management Information) specifies how objects are named (OBJECT IDENTIFIER tree), their data types and the encoding (using ASN.1 and BER). MIB is the virtual database of managed objects, organised as a tree, for example iso.org.dod.internet.mgmt.mib-2 (1.3.6.1.2.1).

### Q118. What is the Last-Modified header and why is it useful?

*(Topic: Wireshark based)*

It gives the date and time the resource was last changed on the server. Browsers use it for cache validation with If-Modified-Since, and the server answers 304 Not Modified if nothing has changed.

### Q119. What is the syntax of a static route command?

*(Topic: Cisco Packet Tracer based)*

ip route <destination-network> <subnet-mask> <next-hop-IP | exit-interface>, for example ip route 172.16.30.0 255.255.255.0 172.16.20.2.

### Q120. What are DR and BDR?

On multi-access networks like Ethernet, a Designated Router and Backup Designated Router are elected to reduce adjacency and LSA flooding. Others form full adjacency only with the DR and BDR.

### Q121. How does the server send its PID?

*(Topic: Socket programming based)*

It calls getpid() in the child process and sends the value to the client along with the file contents or the error message, for example using sprintf() to build the message.

### Q122. Which functions are used to obtain and format time in C?

*(Topic: Socket programming based)*

time() gets the seconds since the Unix epoch, localtime() or gmtime() converts them to a broken-down structure, ctime() or strftime() converts them to a readable string.

### Q123. Explain the distance-vector routing algorithm and its problems.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Each router maintains a vector of distances to all destinations and exchanges it with neighbours, using the Bellman-Ford equation d_x(y) = min over v of {c(x,v) + d_v(y)}. Problems: slow convergence, routing loops and count-to-infinity, solved by split horizon, poison reverse and hold-down.

### Q124. What is a web cache (proxy server) and how does it improve performance?

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

A proxy server stores copies of recently requested objects. If the object is present, the proxy delivers it without contacting the origin server, reducing response time and traffic. The conditional GET with If-Modified-Since validates the cached copy.

### Q125. What is an ACL?

*(Topic: Cisco Packet Tracer based)*

An Access Control List is an ordered list of permit and deny statements applied to a router interface to filter packets based on address, protocol or port.

### Q126. How is a message broadcast to all users?

*(Topic: Socket programming based)*

The server keeps an array or list of all connected client sockets. On receiving a message from one client, it loops over the list and calls send() to every other client.

### Q127. Which commands verify an ACL?

*(Topic: Cisco Packet Tracer based)*

show access-lists (with hit counters), show ip interface (which shows applied ACLs) and show running-config.

---

## 2. Physical & Data Link Layer (MAC, Framing, Switches, VLANs, CSMA)

### Q128. What is a switch?

A device that forwards frames within a LAN using MAC addresses. It works at the Data Link layer.

### Q129. What is a hub?

A device that repeats an incoming signal to all its ports. It has no addressing and works at the Physical layer.

### Q130. What is a NIC?

Network Interface Card. The hardware that connects a device to a network. Its MAC address is assigned by the manufacturer.

### Q131. What is the full form of MAC?

Media Access Control.

### Q132. How many bits is a MAC address?

48 bits, which is 6 bytes or 12 hexadecimal digits, for example 00:1A:2B:3C:4D:5E .

### Q133. Which layer does a MAC address belong to?

The Data Link layer (layer 2).

### Q134. Is a MAC address permanent?

It is burned into the NIC by the manufacturer, so it is xed in hardware. It can be changed in software (MAC spoo ng), but the hardware address is normally permanent.

### Q135. What is the dierence between an IP address and a MAC address?

An IP address is logical, works at the Network layer, can change, and delivers data end to end. A MAC address is physical, works at the Data Link layer, is xed by hardware, and delivers data hop to hop within a local network.

### Q136. Which layer does MAC belong to?

The Data Link layer (layer 2).

### Q137. Explain CSMA/CA and why it is used in wireless LANs.

*(Topic: = 1/e = 36.8%.)*

Wireless stations cannot detect collisions while transmitting (the hidden terminal problem). CSMA/CA avoids collisions using interframe spaces (IFS), a random backoff, positive acknowledgement and the optional RTS/CTS exchange with the NAV (network allocation vector) for virtual carrier sensing.

### Q138. What is a VLAN?

*(Topic: = 1/e = 36.8%.)*

A virtual LAN is a logical grouping of hosts into a broadcast domain independent of their physical location, configured on switches. Frames are tagged (IEEE 802.1Q) so that the trunk link can carry several VLANs.

### Q139. What is the hidden terminal and exposed terminal problem?

*(Topic: = 1/e = 36.8%.)*

Hidden terminal: two stations that cannot hear each other transmit to a common receiver and collide. Exposed terminal: a station refrains from transmitting because it hears another transmission, although its own transmission would not interfere with the receiver.

### Q140. Explain bit stuffing with an example.

*(Topic: DLC, MAC protocols, addressing, Ethernet, connecting devices, WLAN, Mobile IP, packet interface)*

The sender inserts a 0 after every five consecutive 1s in the data, so that the flag 01111110 does not appear in the data. The receiver removes the 0 after five 1s. Example: 0111111011111 becomes 011111010111110.

### Q141. Explain error detection: parity, checksum and CRC.

*(Topic: DLC, MAC protocols, addressing, Ethernet, connecting devices, WLAN, Mobile IP, packet interface)*

Parity adds one bit to make the number of 1s even/odd (detects odd number of bit errors). The checksum is the 1's complement sum of words. CRC divides the data by a generator polynomial using modulo-2 division and appends the remainder, giving strong burst-error detection.

### Q142. Explain CSMA and its persistence methods.

*(Topic: = 1/e = 36.8%.)*

Carrier Sense Multiple Access: sense before transmitting. 1-persistent transmits immediately when idle. Non-persistent waits a random time if busy. p-persistent transmits with probability p if idle in slotted channels.

### Q143. Explain the Ethernet frame format.

*(Topic: = 1/e = 36.8%.)*

Preamble (7 bytes), SFD (1), destination MAC (6), source MAC (6), type/length (2), data (46-1500) and CRC (4). The minimum frame is 64 bytes and the maximum is 1518 bytes.

### Q144. How do you switch from user mode to privileged mode and to configuration mode?

*(Topic: Cisco Packet Tracer based)*

Type enable to enter privileged mode, then configure terminal (conf t) for global configuration mode. Use exit or end/Ctrl+Z to go back.

### Q145. Differentiate between a hub, a bridge, a switch and a router.

*(Topic: = 1/e = 36.8%.)*

Hub: physical-layer repeater, one collision domain. Bridge/switch: data-link layer, learns MAC addresses, separates collision domains, and forwards frames on the basis of the MAC address table. Router: network layer, separates broadcast domains and forwards by IP.

### Q146. Explain CSMA/CD.

*(Topic: = 1/e = 36.8%.)*

In Ethernet, a station senses the medium, transmits, and keeps listening. On detecting a collision, it sends a jam signal, aborts and waits a random time using binary exponential backoff. The minimum frame size ensures that collisions are detected: the transmission time >= 2 x propagation delay (512 bits, 64 bytes for 10 Mbps Ethernet).

### Q147. What is a MAC address and how does it differ from an IP address?

*(Topic: = 1/e = 36.8%.)*

A 48-bit physical (link-layer) address burned into the NIC, written in hex, flat and used within a link. An IP address is a logical hierarchical network address used for routing across networks.

---

## 3. Network Layer, IP Addressing & Subnetting (IPv4, IPv6, CIDR, ARP, ICMP)

### Q148. How many bits is an IPv4 address?

32 bits, written as four decimal octets such as 192.168.1.10. This gives about 232, or 4.29 billion, addresses.

### Q149. How many bits is an IPv6 address?

128 bits, written as eight groups of hexadecimal digits.

### Q150. How many bits is a port number?

16 bits, giving a range of 0 to 65535.

### Q151. What are the well-known port numbers?

0 to 1023. Examples: FTP 20/21, SSH 22, Telnet 23, SMTP 25, DNS 53, DHCP 67/68, HTTP 80, POP3 110, IMAP 143, HTTPS 443.

### Q152. What is the range of registered ports?

1024 to 49151.

### Q153. What are dynamic or private ports?

49152 to 65535. The operating system assigns these temporarily to client programs.

### Q154. What is ARP?

Address Resolution Protocol. It maps an IPv4 address to a MAC address on a local network.

### Q155. What is a subnet mask?

A value that divides an IP address into a network part and a host part. For example, 255.255.255.0 means the rst three octets identify the network.

### Q156. Which layer is a port number in?

The Transport layer. It identi es the process on the host.

### Q157. What are the main functions of the T ransport layer?

Process-to-process delivery using ports, segmentation, ow control, error control, and, for TCP, reliability and congestion control.

### Q158. What is ICMP?

Internet Control Message Protocol. It carries error and status messages, and it is used by ping and traceroute.

### Q159. Why is the buer size important?

If the buer is too small, data is cut o. Use a larger size for big matrices or les.

### Q160. What is the default port used by HTTP and HTTPS?

80 for HTTP and 443 for HTTPS. 12.7 Pickling

### Q161. Which port does SSH use?

22.

### Q162. Which port does T elnet use?

23.

### Q163. Which port does POP3 use?

110.

### Q164. Which port does IMAP use?

143.

### Q165. What is an ephemeral port?

A temporary port chosen by the operating system for the client side of a connection, usually in the 49152 to 65535 range.

### Q166. Explain ARP.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Address Resolution Protocol maps a known IP address to a MAC address on a LAN. A host broadcasts an ARP request, and the owner of the IP replies with a unicast ARP reply. The mapping is cached.

### Q167. Explain the IPv4 datagram format.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Version, header length (IHL), type of service/DSCP, total length, identification, flags (DF, MF), fragment offset, TTL, protocol, header checksum, source address, destination address, options and data.

### Q168. What is the difference between wildcard mask and subnet mask?

*(Topic: Cisco Packet Tracer based)*

A wildcard mask is the inverse of a subnet mask: 0 bits must match and 1 bits are ignored. For

### Q169. What are the limitations of IPv4 and the features of IPv6?

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

IPv4 has 32-bit address exhaustion and no built-in security. IPv6 has 128-bit addresses, a simplified fixed 40-byte header, no fragmentation by routers, extension headers, auto-configuration, built-in IPsec support and no broadcast.

### Q170. How do you verify IPv6 routing?

*(Topic: Cisco Packet Tracer based)*

show ipv6 route (R entries), show ipv6 rip database, show ipv6 interface brief and ping ipv6

### Q171. Why is ipv6 unicast-routing needed?

*(Topic: Cisco Packet Tracer based)*

IPv6 routing is disabled by default on Cisco routers. This command enables forwarding of IPv6 packets.

### Q172. What is the 16th subnet?

*(Topic: Cisco Packet Tracer based)*

(16 - 1) x 8 = 120, so 140.80.120.0/21 with hosts 140.80.120.1 - 140.80.127.254 and broadcast

### Q173. How does IPv6 replace ARP?

*(Topic: Cisco Packet Tracer based)*

With Neighbor Discovery Protocol (NDP) using ICMPv6 Neighbor Solicitation and Advertisement messages.

### Q174. What is the wildcard mask for /21?

*(Topic: 140.80.127.255.)*

0.0.7.255 (inverse of 255.255.248.0).

### Q175. What is ICMP? Give its message types.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Internet Control Message Protocol reports errors and provides diagnostics. Error-reporting: destination unreachable, source quench (obsolete), time exceeded, parameter problem, redirect. Query: echo request/reply, timestamp. It is used by ping and traceroute.

### Q176. How does subnetting work? Explain VLSM.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Subnetting divides a network into smaller networks by borrowing host bits. VLSM allows different subnet masks within the same network so that subnets of different sizes can be allocated efficiently.

### Q177. Explain classful and classless addressing (CIDR).

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Classful addressing has classes A to E with fixed prefix lengths (8, 16, 24). CIDR uses a variable-length prefix in the form a.b.c.d/n, which allows flexible allocation and route aggregation.

### Q178. Explain IP fragmentation with an example.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

If a datagram is larger than the MTU of a link, it is divided into fragments, each with a copy of the header, the same identification, the MF flag set for all but the last, and the offset in units of 8 bytes. Example: 4000-byte datagram (3980 bytes of data) over MTU 1500 gives fragments with data 1480, 1480 and 1020 bytes and offsets 0, 185 and

### Q179. What are the IPv4-to-IPv6 transition strategies?

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Dual stack, tunnelling (IPv6 packets carried inside IPv4) and header translation (NAT64).

### Q180. Explain the IPv6 header format.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Version (4 bits), traffic class (8), flow label (20), payload length (16), next header (8), hop limit (8), source address (128) and destination address (128).

### Q181. What is the size of an IPv6 address? How is it written?

*(Topic: Cisco Packet Tracer based)*

128 bits, written as eight groups of four hexadecimal digits separated by colons, for example 2001:0DB8:1111:0001:0000:0000:0000:0001.

### Q182. How can an IPv6 address be shortened?

*(Topic: Cisco Packet Tracer based)*

Leading zeros in a group can be dropped and one consecutive run of all-zero groups can be replaced by :: (only once). For example 2001:DB8:1111:1::1.

### Q183. How many bits are borrowed for 20 subnets and what is the new mask?

*(Topic: Cisco Packet Tracer based)*

2^5 = 32 >= 20, so 5 bits are borrowed. The new mask is /21 = 255.255.248.0 and each subnet has 2^11 - 2 = 2046 usable hosts. The block size is 8 in the third octet.

### Q184. What are the first four subnets? Where is CCF?

*(Topic: Cisco Packet Tracer based)*

Subnet 1: 140.80.0.0, subnet 2: 140.80.8.0, subnet 3: 140.80.16.0, subnet 4: 140.80.24.0/21 (host range 140.80.24.1 - 140.80.31.254, broadcast 140.80.31.255). CCF is in 140.80.24.0/21.

---

## 4. Routing Protocols & Autonomous Systems (RIP, OSPF, BGP, Routing Tables)

### Q185. What is a router?

A device that forwards packets between dierent networks using IP addresses. It works at the Network layer.

### Q186. What is a hop?

One intermediate device, usually a router, that a packet passes through on its way to the desti- nation.

### Q187. What is an autonomous system? Differentiate intra-domain and inter- domain routing.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

An AS is a group of networks under a single administration. Intra-domain protocols (RIP, OSPF) run inside an AS. Inter-domain routing (BGP) exchanges reachability between ASes.

### Q188. What is administrative distance? What is the value for static routes?

*(Topic: Cisco Packet Tracer based)*

Administrative distance (AD) measures the trustworthiness of a route source. Lower is better. Connected = 0, static = 1, EIGRP = 90, OSPF = 110, RIP = 120.

### Q189. Write the commands to enable RIPng on a router.

*(Topic: Cisco Packet Tracer based)*

Router(config)# ipv6 unicast-routing / Router(config)# interface g0/0 / ipv6 address 2001:DB8:1111:1::1/64 / ipv6 rip MYRIP enable / no shutdown. The same ipv6 rip <name> enable is applied to each interface (no network command is used).

### Q190. Explain RIP and OSPF briefly.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

RIP: distance-vector, hop count metric, max 15 hops, updates every 30 s, UDP port 520. OSPF: link-state, cost metric, areas, Dijkstra, hello/LSA messages, directly over IP (protocol 89), supports authentication and VLSM.

### Q191. Explain the link-state routing algorithm.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Each router floods link-state advertisements to all routers, builds the complete topology graph and runs Dijkstra's algorithm to compute the shortest-path tree. It converges faster than distance vector but needs more memory and processing.

### Q192. Which transport protocol and port does RIP use?

*(Topic: Cisco Packet Tracer based)*

UDP port 520.

### Q193. Which command shows the routing table?

*(Topic: Cisco Packet Tracer based)*

show ip route. Codes such as C (connected), S (static), R (RIP) and O (OSPF) indicate how each route was learned.

### Q194. How often are RIP updates sent?

*(Topic: Cisco Packet Tracer based)*

Every 30 seconds by default. Invalid timer = 180 s, hold-down = 180 s, flush = 240 s.

### Q195. What are the advantages of OSPF over RIP?

Faster convergence, no hop-count limit, classless with VLSM support, uses bandwidth-based cost, scalable due to areas, and sends triggered updates only on change.

### Q196. Write the commands to configure OSPF.

*(Topic: Cisco Packet Tracer based)*

Router(config)# router ospf 1 / Router(config-router)# network 172.16.10.0 0.0.0.255 area 0. The network statement uses a wildcard mask and an area ID.

### Q197. What is OSPF? What type of protocol is it?

*(Topic: Cisco Packet Tracer based)*

Open Shortest Path First is a link-state interior gateway protocol. Each router builds a link-state database of the whole area and runs Dijkstra's SPF algorithm to calculate best paths.

### Q198. How do you verify OSPF?

show ip ospf neighbor, show ip ospf interface, show ip route (O entries), show ip protocols, and ping.

### Q199. What is the metric of OSPF?

*(Topic: Cisco Packet Tracer based)*

Cost, calculated as reference bandwidth divided by interface bandwidth (default reference 100 Mbps). For example a 10 Mbps link has cost 10.

### Q200. Write the commands to configure RIPv2.

*(Topic: Cisco Packet Tracer based)*

Router(config)# router rip / Router(config-router)# version 2 / network 172.16.0.0 / no auto-summary. The network command lists the classful networks of the directly connected interfaces to advertise.

### Q201. What is the maximum hop count in RIP?

*(Topic: Cisco Packet Tracer based)*

15. A hop count of 16 means the network is unreachable.

### Q202. Explain split horizon, route poisoning and hold-down.

*(Topic: Cisco Packet Tracer based)*

Split horizon: a route is not advertised back on the interface from which it was learned. Route poisoning: a failed route is advertised with metric 16. Hold-down: ignore updates about a route for a period after it is marked unreachable. All prevent routing loops.

### Q203. Explain BGP.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Border Gateway Protocol is the path-vector inter-domain protocol. Peers exchange path attributes (AS-PATH, NEXT-HOP, LOCAL-PREF) over TCP port 179 with eBGP (between ASes) and iBGP (within an AS). Routes are chosen using policies, not just shortest path.

### Q204. Compare distance-vector and link-state routing.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Distance vector: neighbour knowledge only, periodic updates, simple, slow convergence, risk of loops (RIP). Link state: complete topology knowledge, event- triggered floods, fast convergence and loop-free but more resource use (OSPF).

### Q205. What are the differences between RIPv1 and RIPv2?

*(Topic: Cisco Packet Tracer based)*

RIPv1 is classful, sends broadcasts (255.255.255.255) and has no authentication. RIPv2 is classless (carries subnet masks and supports VLSM/CIDR), uses multicast 224.0.0.9, and supports authentication and manual summarisation.

### Q206. What is the difference between RIPv2 and RIPng in configuration?

*(Topic: Cisco Packet Tracer based)*

RIPv2 uses router rip and network commands under router mode. RIPng enables RIP per interface with ipv6 rip <name> enable, and ipv6 unicast-routing must be enabled globally.

### Q207. How can you verify RIP operation?

*(Topic: Cisco Packet Tracer based)*

show ip route (R entries), show ip protocols, show ip rip database and debug ip rip; also ping between all hosts.

### Q208. Name the OSPF neighbour states.

Down, Init, 2-Way, ExStart, Exchange, Loading, Full.

### Q209. What is RIPng?

*(Topic: Cisco Packet Tracer based)*

RIP next generation is the IPv6 version of RIP. It is a distance-vector protocol using hop count, 15 as the maximum, updates every 30 seconds, UDP port 521 and multicast address FF02::9.

### Q210. What is RIP? Which type of routing algorithm does it use?

*(Topic: Cisco Packet Tracer based)*

Routing Information Protocol is a distance-vector protocol that uses the Bellman-Ford algorithm and hop count as its metric.

### Q211. What is an OSPF area? What is area 0?

An area is a logical group of routers that share the same link-state database, which reduces SPF calculation and LSA flooding. Area 0 is the backbone area, and all other areas must connect to it.

---

## 5. Transport Layer Mechanics & Protocols (TCP, UDP, Handshakes, Flow & Congestion Control)

### Q212. What is the loopback address?

127.0.0.1, also called localhost. It lets a program talk to itself on the same machine.

### Q213. What is the full form of TCP?

Transmission Control Protocol.

### Q214. What is the full form of UDP?

User Datagram Protocol.

### Q215. What is the dierence between TCP and UDP?

TCP is connection-oriented, reliable, ordered, and slower. UDP is connectionless, unreliable, unordered, and faster. See the comparison table in this guide.

### Q216. Why is UDP faster than TCP?

UDP has no handshake, no acknowledgments, no retransmission, no ow or congestion control, and a smaller header of 8 bytes.

### Q217. What is the TCP 3-way handshake?

SYN from client, SYN-ACK from server, then ACK from client. After this the connection is established.

### Q218. Why is TCP called a byte-stream protocol?

It has no message boundaries. Data is a continuous stream of bytes, so the receiver may get the data in dierent chunk sizes from the sender.

### Q219. What is a datagram?

An independent message unit used by UDP. Each datagram carries its own addressing information, and message boundaries are kept.

### Q220. What header size does TCP have?

At least 20 bytes. UDP has an 8-byte header.

### Q221. Name two protocols that use UDP and two that use TCP .

UDP: DNS (usually), DHCP, streaming, and online games. TCP: HTTP/HTTPS, SMTP, FTP, and SSH.

### Q222. Does UDP guarantee delivery?

No. The application must handle loss, if it needs reliability.

### Q223. Which layer does TCP or UDP belong to?

The Transport layer (layer 4).

### Q224. Name the four layers of the TCP/IP model.

Application, Transport, Internet, and Network Access.

### Q225. How does a host know which process should receive a packet?

The destination port number in the transport header tells the operating system which socket should get the data.

### Q226. What is a segment?

A unit of data at the Transport layer, used by TCP.

### Q227. Program 2 (TCP even or odd): how is parity checked?

With n % 2 . A remainder of 0 means even, and a remainder of 1 means odd.

### Q228. Program 3 (TCP square): why is the server result sent as text?

Sockets transmit bytes. The result must be converted to a string and then encoded before sending.

### Q229. Program 4 (TCP string length): how is length found?

With len(text) , which counts characters.

### Q230. Program 5 (TCP reverse): how is the string reversed?

With slicing, text[::-1] . The step of −1 walks from the end to the start.

### Q231. Program 7 (TCP uppercase): how is uppercase conversion done?

With text.upper() .

### Q232. Program 8 (TCP sum of digits): how is the digit sum found?

Each character that is a digit is converted to an int and added. For 1234 the result is 10.

### Q233. Program 11 (UDP reverse): is there any dierence from the TCP version?

Only the socket type and the send and receive functions. The reversal logic is the same.

### Q234. Program 13 (UDP square): what changes from the TCP version?

Only the socket type, the bind() call, and the use of recvfrom() and sendto().

### Q235. Program 16 (UDP hyphen): how are spaces replaced?

With str.replace(" ", "-") , which replaces every space character.

### Q236. Program 17 (TCP word count): how are words counted?

With len(sentence.split()) . The split function treats runs of spaces as a single separator.

### Q237. Program 19 (UDP number of digits): how are digits counted?

By checking each character with isdigit() and counting the ones that are digits. Minus signs and spaces are skipped.

### Q238. Concurrent le server: why is the PID sent back?

So the client can see that a separate process handled its request. os.getpid() returns the PID of the process that handled it.

### Q239. Packet snier: why does it need root?

A raw socket reads frames that the operating system would otherwise keep from user programs. Only privileged users may open such a socket.

### Q240. Packet snier: what is the EtherType 0x0800?

It means the frame carries an IPv4 packet.

### Q241. Packet snier: what does protocol 6, 17, and 1 mean?

6 is TCP, 17 is UDP, and 1 is ICMP.

### Q242. What are the applications of UDP?

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

DNS, DHCP, SNMP, TFTP, streaming, VoIP and online games, where low delay is more important than reliability, and query-response applications.

### Q243. What is the difference between flow control and congestion control?

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

Flow control prevents a sender from overwhelming the receiver, using the receiver window (rwnd). Congestion control prevents the sender from overwhelming the network, using the congestion window (cwnd). The sending window is min(rwnd, cwnd).

### Q244. Explain TCP congestion control: slow start, congestion avoidance and fast recovery.

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

Slow start: cwnd starts at 1 MSS and doubles every RTT until it reaches ssthresh. Congestion avoidance: cwnd increases by 1 MSS per RTT (additive increase). On a timeout, ssthresh = cwnd/2 and cwnd = 1 (Tahoe/Reno); on 3 duplicate ACKs, fast retransmit and fast recovery set cwnd = ssthresh (Reno) and continue with linear growth.

### Q245. Write the sequence of socket calls in a TCP server and a TCP client.

*(Topic: Basics to revise before all experiments)*

Server: socket(), bind(), listen(), accept(), recv()/send(), close(). Client: socket(), connect(), send()/recv(), close().

### Q246. Write the sequence of socket calls in a UDP server and client.

*(Topic: Basics to revise before all experiments)*

Server: socket(), bind(), recvfrom(), sendto(), close(). Client: socket(), sendto(), recvfrom(), close(). There is no listen(), accept() or connect() in the basic UDP model.

### Q247. What is the difference between a chat server using TCP and one using UDP?

*(Topic: Socket programming based)*

TCP gives reliable ordered delivery and detects disconnects, so it is preferred for chat. With UDP the server would need to track clients itself and messages may be lost.

### Q248. Explain how a concurrent TCP server is written using fork().

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

The parent calls socket, bind, listen, and loops on accept(); for each connection it calls fork(); the child closes the listening socket, serves the client and exits; the parent closes the connected socket and continues to accept.

### Q249. What is tcpdump? Give an example.

*(Topic: Warm up)*

tcpdump is a command-line packet analyser that captures packets from an interface. Example: sudo tcpdump -i eth0 port 80 captures HTTP traffic. Output can be saved with -w file.pcap and opened in Wireshark.

### Q250. Explain the TCP/IP protocol layering and the function of each layer.

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

Application (services to the user: HTTP, SMTP, DNS), Transport (process-to- process delivery: TCP, UDP), Network (host-to-host delivery and routing: IP), Data-link (node-to-node delivery within a link: Ethernet, Wi-Fi) and Physical (transmission of bits over the medium).

### Q251. Differentiate between TCP and UDP.

*(Topic: Basics to revise before all experiments)*

TCP is connection-oriented, reliable, ordered and does flow and congestion control (SOCK_STREAM). UDP is connectionless, unreliable, has no ordering guarantee and low overhead (SOCK_DGRAM). TCP suits file transfer and web; UDP suits DNS, streaming and time services.

### Q252. Why is TCP used in this experiment?

*(Topic: Socket programming based)*

The matrix must be delivered completely and in order, and TCP provides reliable, connection-oriented byte-stream delivery.

### Q253. Why is no connection established in UDP?

*(Topic: Socket programming based)*

UDP is connectionless. Each datagram is independent and there is no handshake, so the server learns the client's address from recvfrom().

### Q254. What is the UDP header format?

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

Four 16-bit fields: source port, destination port, length and checksum (a total of 8 bytes).

### Q255. How is concurrency achieved in a UDP server?

*(Topic: Socket programming based)*

After recvfrom() receives a request the server calls fork() (or creates a thread) and the child processes the request and replies with sendto(), while the parent goes back to recvfrom() for the next request.

### Q256. What happens if a UDP datagram is lost?

*(Topic: Socket programming based)*

UDP does not retransmit, so the client would wait forever on recvfrom(). Use a timeout (SO_RCVTIMEO or select()) and retry at the application level.

### Q257. Explain TCP connection termination.

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

Each direction is closed independently with FIN and ACK (four-way close): FIN from A, ACK from B, FIN from B, ACK from A. The side that closes first goes into TIME_WAIT for 2 x MSL. A half-close is possible.

### Q258. Does DNS use UDP or TCP? On which port?

*(Topic: Wireshark based)*

Normally UDP port 53 for queries and responses. TCP port 53 is used for zone transfers and for responses too large for UDP (truncated, TC bit set).

### Q259. What is the TCP segment format? Name the fields.

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

Source port, destination port, sequence number, acknowledgement number, header length, control flags (URG, ACK, PSH, RST, SYN, FIN), window size, checksum, urgent pointer, options and data.

### Q260. Explain how TCP provides reliable data transfer.

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

By using sequence numbers, cumulative acknowledgements, timers with retransmission on timeout, fast retransmit on three duplicate ACKs, checksums and a sliding window.

### Q261. Explain the elementary TCP socket functions.

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

socket() creates a descriptor; bind() assigns a local address; listen() converts the socket to passive and sets the backlog; accept() returns a connected descriptor; connect() begins the three-way handshake; send()/recv() (or read()/write()) transfer data; close() ends the connection.

### Q262. Does UDP guarantee ordering or delivery?

*(Topic: Socket programming based)*

No. Datagrams may be lost, duplicated or reordered.

### Q263. Explain TCP connection establishment (three-way handshake).

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

The client sends SYN with initial sequence number x; the server replies with SYN+ACK (its own sequence number y and acknowledgement x+1); the client sends ACK (y+1). Then the connection is established.

### Q264. Explain the elementary UDP socket functions and how the UDP client- server differs from TCP. Ans: recvfrom() and sendto() are used with the peer address. No listen/accept/connect is needed, and there is no connection state. UDP preserves message boundaries. A connected UDP socket (connect() then send()/recv()) can be used to receive ICMP errors.

*(Topic: *timeout). It waits until any descriptor in the sets is ready or the timeout expires, and it returns the number of ready descriptors. Macros: FD_ZERO, FD_SET, FD_CLR, FD_ISSET.)*

Answer not provided in the source document.

### Q265. How is a large file sent over a TCP socket?

*(Topic: Socket programming based)*

Read it in chunks (for example 1024 bytes) using read()/fread() into a buffer and send each chunk with send() in a loop until end of file. The receiver loops on recv() until the connection is closed or a length is reached.

### Q266. Why is TCP called a byte stream and why does it matter here?

*(Topic: Socket programming based)*

TCP does not preserve message boundaries. One send() may be received by several recv() calls, so the receiver must loop until it has received the expected number of bytes.

### Q267. Compare the OSI model and the TCP/IP model.

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

OSI has seven layers, and TCP/IP has five (or four). OSI separates the session, presentation and application layers, while TCP/IP combines them in the application layer. OSI is a theoretical reference; TCP/IP is the protocol suite that is actually deployed.

### Q268. What protocol numbers identify ICMP, TCP and UDP in the IP header?

*(Topic: Socket programming based)*

ICMP = 1, TCP = 6, UDP = 17.

---

## 6. Application Layer Protocols (DNS, HTTP, SMTP, POP3, IMAP, DHCP)

### Q269. What is DHCP?

Dynamic Host Con guration Protocol. It automatically assigns IP address and other settings to devices. It uses ports 67 and 68.

### Q270. What is DNS?

Domain Name System. It translates domain names (such as example.com) into IP addresses. It uses port 53.

### Q271. What are the SNMP PDUs?

*(Topic: SNMP, ASN.1, data and signals, transmission, bandwidth, media)*

GetRequest, GetNextRequest, GetBulkRequest (v2), SetRequest, Response, Trap (agent-to-manager notification, port 162) and InformRequest (v2).

### Q272. Explain FTP. Why is it called an 'out-of-band' protocol?

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

FTP transfers files using two TCP connections: a control connection on port 21 (commands and replies) and a data connection on port 20 (file transfer). Control information is sent separately from the data, hence 'out-of-band'.

### Q273. Which transport protocol and port does HTTP use?

*(Topic: Wireshark based)*

HTTP runs over TCP, by default on port 80. HTTPS uses TCP port 443.

### Q274. Explain the SNMP architecture.

*(Topic: SNMP, ASN.1, data and signals, transmission, bandwidth, media)*

A manager (NMS) monitors and controls agents that run on managed devices. Each agent holds a MIB (Management Information Base). SMI defines the rules for naming and encoding management objects. Communication is by SNMP messages over UDP (ports 161 and 162).

### Q275. What is the difference between SMTP, POP3 and IMAP?

*(Topic: <CRLF>.<CRLF>. 221: service closing the transmission channel. Also 550 means mailbox unavailable and 421 means service not available.)*

SMTP is a push protocol used to send mail. POP3 and IMAP are pull protocols used by the client to retrieve mail from the mailbox; POP3 usually downloads and deletes, while IMAP keeps mail on the server and synchronises.

### Q276. What is an HTTP GET message? Name other HTTP methods.

*(Topic: Wireshark based)*

GET requests a resource from the server. Other methods are POST, HEAD, PUT, DELETE, OPTIONS and PATCH.

### Q277. Which port number is the SMTP client port and in which range does it lie?

*(Topic: Wireshark based)*

The client uses a randomly selected ephemeral (dynamic) port in the range 49152-65535 (or 32768-60999 on Linux). The server side is a well-known port.

### Q278. What is the difference between HTTP/1.0 and HTTP/1.1?

*(Topic: Wireshark based)*

HTTP/1.0 uses non-persistent connections by default (one object per TCP connection). HTTP/1.1 uses persistent connections and supports pipelining and the Host header. HTTP/2 adds multiplexing and header compression.

### Q279. What are the HTTP request and response message formats?

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

Request: request line (method, URL, version), header lines, blank line, optional body. Response: status line (version, status code, phrase), header lines, blank line, body.

### Q280. Explain the SMTP response codes 220, 250, 354 and 221.

*(Topic: Wireshark based)*

220: service ready. 250: requested action completed OK. 354: start mail input, end with

### Q281. Compare POP3 and IMAP.

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

POP3 downloads messages to the local machine and typically deletes them from the server (stateless across sessions). IMAP keeps messages on the server and allows folders, partial fetches and synchronisation across devices.

### Q282. To which IP address is the DNS query sent?

*(Topic: Wireshark based)*

To the configured local DNS resolver (often the router or the ISP/public DNS server, such as 8.8.8.8). Check it with cat /etc/resolv.conf or resolvectl status.

### Q283. Name the common DNS record types.

*(Topic: = zero or more (NS records), Additional = zero or more (glue records or OPT).)*

A (IPv4 address), AAAA (IPv6 address), CNAME (alias), MX (mail exchanger), NS (name server), PTR (reverse lookup), SOA (start of authority), TXT (text).

### Q284. Why can you not see the HTTP content clearly when visiting an HTTPS site?

*(Topic: Wireshark based)*

HTTPS encrypts HTTP with TLS, so only the TCP/TLS handshake and encrypted records are visible. That is why this experiment uses a plain HTTP website.

### Q285. What is the difference between active and passive FTP?

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

In active mode the server initiates the data connection from port 20 to the client. In passive mode the client initiates both connections, which works better through firewalls and NAT.

### Q286. What is SMTP and what is its function?

*(Topic: Wireshark based)*

Simple Mail Transfer Protocol is the application layer protocol used to send (push) e-mail from a client to a server and between mail servers.

### Q287. Why do we flush the DNS cache before capturing? Which commands are used?

*(Topic: Wireshark based)*

To force the computer to send a fresh DNS query rather than answer from the local cache. Use ipconfig /flushdns on Windows and systemd-resolve --flush-caches (resolvectl flush-caches) on Linux.

### Q288. What is a stateless protocol? Is HTTP stateless?

*(Topic: Wireshark based)*

A stateless protocol does not remember previous requests. HTTP is stateless; cookies and sessions are used to maintain state.

### Q289. What are the common HTTP status codes? What does 200 OK mean?

*(Topic: Wireshark based)*

1xx informational, 2xx success, 3xx redirection, 4xx client error, 5xx server error. 200 OK means the request succeeded. Others: 301 Moved Permanently, 304 Not Modified, 404 Not Found, 500 Internal Server Error.

### Q290. List the main SMTP commands.

*(Topic: Wireshark based)*

HELO/EHLO (identify client), MAIL FROM (sender), RCPT TO (recipient), DATA (start message body, ended by a line with a single dot), RSET, NOOP, QUIT, and STARTTLS (upgrade to encryption).

### Q291. What is DNS? Explain its hierarchy and how name resolution works.

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

DNS maps domain names to IP addresses using a distributed database. The hierarchy consists of root servers, top-level domain (TLD) servers, and authoritative servers. A local resolver performs recursive or iterative queries and caches the results.

### Q292. Which transport protocol and port numbers does SMTP use?

*(Topic: Wireshark based)*

TCP. Port 25 is used for server-to-server relay, 587 for mail submission (STARTTLS) and 465 for SMTP over implicit TLS.

### Q293. What is DNS and why is it needed?

*(Topic: Wireshark based)*

The Domain Name System translates human-readable domain names (for example www.example.com) into IP addresses. It is a distributed hierarchical database.

### Q294. What is DHCP and how does it work?

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Dynamic Host Configuration Protocol automatically assigns IP address, mask, gateway and DNS. Steps (DORA): Discover, Offer, Request, Acknowledge using UDP ports 67 and 68.

---

## 7. Socket Programming Architecture & Berkeley Sockets API

### Q295. What is a socket?

An endpoint for network communication, identi ed by an (IP address, port number) pair.

### Q296. What identies a single TCP connection?

A four-tuple: source IP, source port, destination IP, and destination port. 12.3 TCP and UDP

### Q297. How is a TCP connection closed?

With FIN and ACK exchanges. Each side closes its half of the connection.

### Q298. What is the Python socket type for TCP? F or UDP?

socket.SOCK_STREAM for TCP. socket.SOCK_DGRAM for UDP.

### Q299. How do you use the socket module in Python?

Import it with import socket , then create a socket with socket.socket(family, type) , for example socket.socket(socket.AF_INET, socket.SOCK_STREAM) .

### Q300. What does bind() do?

It attaches the socket to a local IP address and port. The server calls it so clients know where to connect.

### Q301. What does listen() do?

It puts a TCP server socket into listening mode. The argument is the backlog, which is the number of pending connections the system will queue.

### Q302. What does accept() do?

It blocks until a client connects. It returns a new socket for that client and the client's address.

### Q303. What does connect() do?

It opens a TCP connection from the client to the server address.

### Q304. Why do UDP programs not need listen() and accept()?

UDP is connectionless. There is no connection to set up, so the server just waits with recvfrom().

### Q305. What is the dierence between send() and sendall()?

send() may send only part of the data and returns how many bytes it sent. sendall() keeps sending until all bytes are sent.

### Q306. What does recv() return when the other side closes the connection?

An empty bytes object, b .

### Q307. What does recvfrom() return?

A tuple of (data, sender address). The address is needed to send a reply with sendto().

### Q308. Why must data be encoded before sending?

Sockets transmit bytes, not Python strings. Use .encode() before sending and .decode() after receiving.

### Q309. What is SO_REUSEADDR?

A socket option that lets a server bind to a port that was recently used, for example one in the TIME_W AIT state. It avoids address already in use errors when restarting a server.

### Q310. What does bind to 0.0.0.0 mean?

The server accepts connections on all of the machine's network interfaces.

### Q311. What is the dierence between AF_INET and AF_INET6?

AF_INET is for IPv4 addresses. AF_INET6 is for IPv6 addresses.

### Q312. Why might recv(1024) return only part of a message?

TCP is a byte stream, so one recv() may return fewer bytes than the sender wrote. A program needs a length pre x or a delimiter to know where a message ends.

### Q313. Why is pickling needed in socket programs?

A socket sends only bytes. Pickling converts lists, tuples, dictionaries, and matrices into bytes, and unpickling restores the original object on the other side.

### Q314. What is the dierence between sending a string and sending a pickled object?

A string needs only encode() and decode(). A pickled object can hold lists, tuples, dictionaries, and other structures, and must be restored with pickle.loads().  12.8 Concurrency and Multi-Client Servers

### Q315. How does the server know that a client has disconnected?

recv() returns an empty bytes object, b. The server then removes that client from the list and closes the connection.

### Q316. What is the backlog in listen(n)?

The maximum number of connections waiting to be accepted. Connections beyond this limit may be refused.

### Q317. Program 9 (UDP length): why does the server use recvfrom()?

UDP has no connection, so the server needs recvfrom() to get the data and the sender's address. The address is needed for the reply.

### Q318. Program 10 (UDP even or odd): why must the server reply with sendto()?

UDP has no connection. The server uses sendto() with the address it received from recvfrom().

### Q319. Program 15 (UDP uppercase): can the client send a string with spaces?

Yes. The whole string is sent and converted. Make sure the buer is large enough for the message.

### Q320. Time server: what does the server send back?

The current time, formatted with strftime("%H:%M:%S") .

### Q321. What is the dierence between a socket and a port?

A port is a number in the transport header. A socket is the programming endpoint that combines an IP address with a port.

### Q322. What is a raw socket?

*(Topic: Socket programming based)*

A socket that gives direct access to the underlying protocol headers, bypassing the transport layer processing of the kernel. It is created with SOCK_RAW.

### Q323. Explain how HTTP works. What is the difference between persistent and non-persistent connections?

*(Topic: Overview of the Internet, HTTP, FTP, E-mail, DNS, P2P, BitTorrent)*

HTTP is a request-response protocol over TCP port 80. In non-persistent HTTP each object needs a new TCP connection, costing two RTTs plus transmission time per object. In persistent HTTP the connection remains open for several objects (default in HTTP/1.1), saving RTTs.

### Q324. What is a socket? Explain the socket address structure.

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

A socket is an endpoint of communication. struct sockaddr_in contains sin_family (AF_INET), sin_port (network byte order) and sin_addr (struct in_addr), and it is cast to struct sockaddr in calls such as bind() and connect().

### Q325. How do you detect that a client has disconnected?

*(Topic: Socket programming based)*

recv() returns 0 on an orderly close (or -1 on error). The server then closes that socket and removes it from the client list.

### Q326. What is the purpose of bind()?

*(Topic: Basics to revise before all experiments)*

bind() associates a socket with a local IP address and port number so the operating system knows which incoming packets to deliver to that socket. Servers must bind to a well-known port; clients normally let the OS choose an ephemeral port.

### Q327. What does accept() return?

*(Topic: Socket programming based)*

A new socket descriptor dedicated to the connected client. The original listening socket continues to listen for more connections.

### Q328. What does listen()'s backlog parameter mean?

*(Topic: Socket programming based)*

It is the maximum length of the queue of pending, fully-established connections waiting to be accepted.

### Q329. Which call creates a raw socket that captures all packets on Linux?

*(Topic: Socket programming based)*

socket(AF_PACKET, SOCK_RAW, htons(ETH_P_ALL)). This receives complete Ethernet frames. Alternatively socket(AF_INET, SOCK_RAW, IPPROTO_TCP) receives only TCP packets with the IP header.

### Q330. What should the parent do with the connected socket after fork()?

*(Topic: Socket programming based)*

The parent closes the connected socket (it only needs the listening socket) and the child closes the listening socket. Otherwise the connection will not be closed properly.

---

## 8. Concurrency, I/O Multiplexing & Raw Sockets (Threads, Processes, select/poll/epoll)

### Q331. Why do we close the connection in the parent process after starting a child process?

The child process has its own copy of the socket. The parent closes its copy so that the connection is not held open unnecessarily.

### Q332. Why does the server use fork() for each client?

*(Topic: Socket programming based)*

So that the parent can keep accepting new connections while each child process serves one client, allowing simultaneous file transfers.

### Q333. Explain the select() function.

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

int select(int maxfdp1, fd_set *readset, fd_set *writeset, fd_set *exceptset, struct timeval

### Q334. What are threads and how are they different from processes?

*(Topic: Socket programming based)*

Threads share the same address space of a process, so they are lightweight and communicate easily, while processes have separate address spaces and use IPC or copies of data.

### Q335. Explain stop-and-wait, Go-Back-N and Selective Repeat.

*(Topic: Services, UDP, TCP; sockets, elementary TCP/UDP sockets, I/O multiplexing)*

Stop-and-wait sends one frame and waits for the ACK (window size 1). Go-Back- N uses a sender window up to 2^m - 1 and a receiver window of 1; on an error, all frames from the lost one are resent. Selective Repeat uses windows of 2^(m-1) on both sides and retransmits only the lost frames.

### Q336. What synchronisation issues arise in a threaded chat server?

*(Topic: Socket programming based)*

Shared data such as the client list can be modified by many threads simultaneously, causing race conditions. Protect it with a mutex (pthread_mutex_lock/unlock).

### Q337. Compare select() and poll().

*(Topic: *timeout). It waits until any descriptor in the sets is ready or the timeout expires, and it returns the number of ready descriptors. Macros: FD_ZERO, FD_SET, FD_CLR, FD_ISSET.)*

select() uses fixed-size bit sets (limited by FD_SETSIZE, typically 1024) that must be re-initialised for each call. poll() takes an array of struct pollfd (fd, events, revents), has no fixed limit and does not modify the input events. Both scan all descriptors, so O(n); epoll is more scalable.

### Q338. What is a zombie process and how do you avoid it in a fork-based server?

*(Topic: Socket programming based)*

A child that has terminated but whose exit status has not been collected. Avoid with wait()/waitpid() in a SIGCHLD handler or by ignoring SIGCHLD.

### Q339. Explain how select() works.

*(Topic: Socket programming based)*

select() monitors a set of file descriptors and blocks until one or more are ready for reading, writing or have an exception. The server keeps the listening socket and all client sockets in an fd_set; when the listening socket is ready it calls accept(), and when a client socket is ready it reads the message.

---

## 9. Network Security, QoS & Diagnostic Tools (Wireshark, ping, traceroute, ip)

### Q340. What does ping do?

It checks whether a host is reachable by sending ICMP Echo Request messages and waiting for Echo Reply messages. It also measures round-trip time.

### Q341. What does traceroute do?

It shows the path to a destination by sending packets with increasing TTL values. Each router that sends back a Time Exceeded message is shown as one hop.

### Q342. What are the intermediary devices seen in traceroute?

Routers along the path.

### Q343. What does nslookup do?

It queries DNS to nd the IP address for a domain name, or the domain name for an IP address.

### Q344. What does netstat show?

Open connections, listening ports, and related network statistics.

### Q345. Differentiate between the leaky bucket and token bucket algorithms.

*(Topic: IP, routing, multicast, intra/inter-domain routing, IPv6, QoS, Linux routing table)*

Leaky bucket outputs at a constant rate irrespective of burstiness of input, smoothing the traffic. Token bucket allows bursts up to the number of accumulated tokens while keeping the average rate.

### Q346. How does ping work? Which protocol does it use?

*(Topic: Warm up)*

ping sends ICMP Echo Request messages to a destination and waits for ICMP Echo Reply messages. It reports whether the host is reachable, the round-trip time and packet loss.

### Q347. What is Wireshark?

*(Topic: Wireshark based)*

Wireshark is a free, open-source packet analyser used to capture live network traffic and inspect each packet at every protocol layer.

### Q348. What does a ping result of '!!!!!' or ' ' or 'U.U.U' mean on a router?

*(Topic: Cisco Packet Tracer based)*

! = success, . = timeout, U = destination unreachable.

### Q349. What will be the result of pinging Host_A from Lab_B and Lab_C?

*(Topic: Cisco Packet Tracer based)*

The ping fails (Destination unreachable, shown as U on a router, or 'Destination host unreachable' on a PC) because they are blocked by the ACL. The ping from Host_B succeeds.

### Q350. How does traceroute discover the path to a destination?

*(Topic: Warm up)*

It sends packets with TTL = 1, 2, 3 and so on. Each router decrements the TTL and, when it reaches 0, discards the packet and returns an ICMP Time Exceeded message. This reveals each hop in turn until the destination is reached.

---

## 10. Lab Experiments & Socket Programming Implementations

### Q351. What is pickling?

Serializing a Python object into a byte stream with pickle.dumps() , so that it can be sent over a socket. pickle.loads() reverses this process.

### Q352. What is the security risk of pickle?

Unpickling untrusted data can run arbitrary code. Only unpickle data from sources you trust.

### Q353. Program 1 (TCP factorial): how is the factorial computed?

With math.factorial(n) . The server converts the received string to an int, computes the facto- rial, and sends the result back as a string.

### Q354. Program 6 (TCP palindrome): what is a palindrome?

A word or phrase that reads the same forwards and backwards, such as level. The check is text == text[::-1] .

### Q355. Program 12 (UDP palindrome): what happens if the UDP packet is lost?

The client waits forever, because UDP does not retransmit. A real program would use a timeout with settimeout() and retry.

### Q356. Program 14 (UDP vowels): which letters count as vowels?

a, e, i, o, u, in both uppercase and lowercase.

### Q357. Program 18 (TCP vowel count): what is the dierence from Program 14?

The protocol. Program 18 uses TCP with a connection. Program 14 uses UDP with datagrams. The counting logic is the same.

### Q358. Slang translator: how is a word replaced?

The server splits the sentence into words and looks up each word in a dictionary. If found, it replaces the word with the full form.

### Q359. Matrix classication: why is pickle used here?

The matrix is a nested list. Pickle turns it into bytes that can be sent over the socket. The server restores it with pickle.loads().

### Q360. Matrix classication: what does i > j mean?

The element is below the main diagonal. i < j means above the diagonal. i == j means on the diagonal.

### Q361. SMTP simulation: what does 354 mean?

The server is ready to receive the message body, which ends with a line containing a single period.

### Q362. SMTP simulation: what does 221 mean?

The server is closing the connection in reply to QUIT. 12.10 Miscellaneous

### Q363. Which port does SMTP use?

25.

### Q364. How is the matrix sent from the client to the server?

*(Topic: Socket programming based)*

The client sends N first and then N x N integers (for example as a flat array in a single send(), or row by row). The server reads exactly N x N integers. Integers should be converted with htonl()/ntohl() if the machines may differ in endianness.

### Q365. What is the function of a time server?

*(Topic: Socket programming based)*

It returns the current system time of the remote machine to a requesting client, which displays it.

### Q366. What is the condition for a lower triangular matrix?

*(Topic: Socket programming based)*

All elements above the main diagonal are zero (a[i][j] = 0 for i < j).

### Q367. What is the condition for an upper triangular matrix?

*(Topic: Socket programming based)*

All elements below the main diagonal are zero (a[i][j] = 0 for i > j).

### Q368. Calculate the CRC for data 1101011011 and generator 10011.

*(Topic: DLC, MAC protocols, addressing, Ethernet, connecting devices, WLAN, Mobile IP, packet interface)*

Append 4 zeros: 11010110110000, then divide by 10011 using XOR. Remainder = 1110. Transmitted frame = 11010110111110.

### Q369. What is a diagonal matrix? Which check order should be used?

*(Topic: Socket programming based)*

All off-diagonal elements are zero. A diagonal matrix is both upper and lower triangular, so check for diagonal first, then upper, then lower, and otherwise report that it is none of these.

### Q370. How can a chat server handle multiple clients?

*(Topic: Socket programming based)*

Using a process per client (fork()), a thread per client (pthread), or I/O multiplexing with select(), poll() or epoll() in a single process.

---
