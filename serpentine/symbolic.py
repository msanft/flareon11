from __future__ import print_function
import sys
from miasm.analysis.binary import Container
from miasm.analysis.machine import Machine
from miasm.core.locationdb import LocationDB

binary = open("payload1.bin", 'rb')

loc_db = LocationDB()

# The Container will provide a *bin_stream*, bytes source for the disasm engine
# It will provide a view from a PE or an ELF.
cont = Container.from_stream(binary, loc_db)

# The Machine, instantiated with the detected architecture, will provide tools
# (disassembler, etc.) to work with this architecture
machine = Machine("x86_64")

# Instantiate a disassembler engine, using the previous bin_stream and its
# associated location DB. The assembly listing will use the binary symbols
mdis = machine.dis_engine(cont.bin_stream, loc_db=cont.loc_db)
mdis.follow_call = True

# Run a recursive traversal disassembling from the entry point
# (do not follow sub functions by default)
asmcfg = mdis.dis_multiblock(0x98)

# Display each basic blocks
for block in asmcfg.blocks:
    print(block)
