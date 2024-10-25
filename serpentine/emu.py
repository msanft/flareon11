from qiling import Qiling
from qiling.const import QL_ARCH, QL_OS, QL_VERBOSE

ROOTFS = r"examples/rootfs/x8664_windows"

offsets = []
with open("execution.log") as f:
    for line in f:
        offsets.append(int(line.strip(), 16))

code = open("payload1.bin", "rb").read()

ql = Qiling(code=code, archtype=QL_ARCH.X8664, ostype=QL_OS.WINDOWS, rootfs=ROOTFS)

# start emulation
ql.run(begin=offsets[0])
