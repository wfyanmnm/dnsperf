#!/usr/bin/env python3

import sys
import dns.message
import struct

m = dns.message.make_query('.', 'TYPE666')
m.id = int(sys.argv[1])
m.use_edns(0, options=[dns.edns.GenericOption(dns.edns.OptionType.PADDING, '\x00' * int(sys.argv[2]))])
binary = m.to_wire(max_size=65535)
binary = struct.pack('>H', len(binary)) + binary
open(sys.argv[3], 'wb').write(binary)
