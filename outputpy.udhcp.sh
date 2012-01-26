#!/bin/sh
#
# outputpy.udhcp.sh: a simple script called by udhcpc when a lease is
# obtained. The script takes information passed by udhcpc as environment
# variables and outputs it formatted as a python dict. Only the variables
# needed by pypxeboot are currently printed: others are listed in comments
# for reference.
# Copyright 2007 Trinity College Dublin
# Author: Stephen Childs <childss@cs.tcd.ie>

# we only need to process "bound" events
if [ "$1" == "bound" ]; then
echo ip=$ip
echo siaddr=$siaddr
echo sname=$sname
echo boot_file=$boot_file
echo subnet=$subnet
echo timezone=$timezone
echo router=$router
echo bootfile=$bootfile #        - The bootfile name
fi
exit 0

#        timesvr         - A list of time servers
#        namesvr 
#        dns  
#        logsvr          - A list of MIT-LCS UDP log servers
#        cookiesvr       - A list of RFC 865 cookie servers
#        lprsvr          - A list of LPR servers
#        hostname        - The assigned hostname
#        bootsize        - The length in 512 octect blocks of the bootfile
#        domain          - The domain name of the network
#        swapsvr         - The IP address of the client's swap server
#        rootpath        - The path name of the client's root disk
#        ipttl           - The TTL to use for this network
#        mtu             - The MTU to use for this network
#        broadcast       - The broadcast address for this network
#        ntpsrv          - A list of NTP servers
#        wins            - A list of WINS servers
#        lease           - The lease time, in seconds
#        dhcptype        - DHCP message type (safely ignored)
#        serverid        - The IP of the server
#        message         - Reason for a DHCPNAK
#        tftp            - The TFTP server name
