import enum
loads = set()
stores = set()
with open("/home/david/git/chipyard/toolchains/riscv-tools/riscv-isa-sim/build/ls.spike") as f:
    lines = f.readlines()
for line_s in lines:
    line = line_s.replace("\n", "").split()
    ls, pc, insn_hex, opcode, *args = line
    if(ls=="load:"):
        loads.add(opcode)
    if(ls=="store:"):
        stores.add(opcode)
print(ls)
print(loads)
print(stores)

with open("libquantum.spike") as f:
    lines = f.readlines()
op = enum.Enum("Op", "load", "store", "branch", "jump", "r_rr", "r_ri", "atomic", "r_i", "c_r_r", "c_r_i")
opcodes = {
    'add'       : (op.r_rr, ),
    'addi'      : (op.r_ri, ),
    'addiw'     : (op.r_ri, ),
    'addw'      : (op.r_rr, ),
    'amoadd.w'  : (op.atomic, ),
    'amoswap.d' : (op.atomic, ),
    'amoswap.w' : (op.atomic, ),
    'and'       : (op.r_rr, ),
    'andi'      : (op.r_ri, ),
    'auipc'     : (op.r_i, ),
    'beq'       : (op.branch, ),
    'beqz'      : (op.branch, ),
    'bge'       : (op.branch, ),
    'bgeu'      : (op.branch, ),
    'bgez'      : (op.branch, ),
    'blt'       : (op.branch, ),
    'bltu'      : (op.branch, ),
    'bltz'      : (op.branch, ),
    'bne'       : (op.branch, ),
    'bnez'      : (op.branch, ),
    'c.add'     : (op.c_r_r, ),
    'c.addi'    : (op.c_r_i, ),
    'c.addi16sp': (op.c_r_i, ),
    'c.addi4spn': (op.r_ri,),
    'c.addiw'   : (op.c_r_i, ),
    'c.addw'    : (op.c_r_r, ),
    'c.and'     : (op.c_r_r, ),
    'c.andi'    : (op.c_r_i, ),
    'c.beqz'    : (op.branch, ),
    'c.bnez'    : (op.branch, ),
    'c.fldsp'   : (op.unknown, ),
    'c.fsd'     : (op.unknown, ),
    'c.fsdsp'   : (op.unknown, ),
    'c.j'       : (op.unknown, ),
    'c.jalr'    : (op.unknown, ),
    'c.jr'      : (op.unknown, ),
    'c.ld'      : (op.unknown, ),
    'c.ldsp'    : (op.unknown, ),
    'c.li'      : (op.unknown, ),
    'c.lui'     : (op.unknown, ),
    'c.lw'      : (op.unknown, ),
    'c.lwsp'    : (op.unknown, ),
    'c.mv'      : (op.unknown, ),
    'c.nop'     : (op.unknown, ),
    'c.or'      : (op.unknown, ),
    'c.sd'      : (op.unknown, ),
    'c.sdsp'    : (op.unknown, ),
    'c.slli'    : (op.unknown, ),
    'c.srai'    : (op.unknown, ),
    'c.srli'    : (op.unknown, ),
    'c.sub'     : (op.unknown, ),
    'c.subw'    : (op.unknown, ),
    'c.sw'      : (op.unknown, ),
    'c.swsp'    : (op.unknown, ),
    'c.xor'     : (op.unknown, ),
    'csrr'      : (op.unknown, ),
    'csrrs'     : (op.unknown, ),
    'csrrw'     : (op.unknown, ),
    'csrw'      : (op.unknown, ),
    'csrwi'     : (op.unknown, ),
    'divu'      : (op.unknown, ),
    'divw'      : (op.unknown, ),
    'ecall'     : (op.unknown, ),
    'fadd.s'    : (op.unknown, ),
    'fcvt.d.lu' : (op.unknown, ),
    'fcvt.d.s'  : (op.unknown, ),
    'fcvt.d.w'  : (op.unknown, ),
    'fcvt.l.d'  : (op.unknown, ),
    'fcvt.s.d'  : (op.unknown, ),
    'fdiv.d'    : (op.unknown, ),
    'fence'     : (op.unknown, ),
    'fence.i'   : (op.unknown, ),
    'feq.s'     : (op.unknown, ),
    'fld'       : (op.unknown, ),
    'flt.d'     : (op.unknown, ),
    'flt.s'     : (op.unknown, ),
    'flw'       : (op.unknown, ),
    'fmadd.s'   : (op.unknown, ),
    'fmsub.s'   : (op.unknown, ),
    'fmul.d'    : (op.unknown, ),
    'fmul.s'    : (op.unknown, ),
    'fmv.w.x'   : (op.unknown, ),
    'fsd'       : (op.unknown, ),
    'fsgnj.d'   : (op.unknown, ),
    'fsgnj.s'   : (op.unknown, ),
    'fsw'       : (op.unknown, ),
    'j'         : (op.unknown, ),
    'jal'       : (op.unknown, ),
    'jalr'      : (op.unknown, ),
    'jr'        : (op.unknown, ),
    'lbu'       : (op.unknown, ),
    'ld'        : (op.unknown, ),
    'lhu'       : (op.unknown, ),
    'li'        : (op.unknown, ),
    'lr.d'      : (op.unknown, ),
    'lr.w'      : (op.unknown, ),
    'lui'       : (op.unknown, ),
    'lw'        : (op.unknown, ),
    'lwu'       : (op.unknown, ),
    'mret'      : (op.unknown, ),
    'mul'       : (op.unknown, ),
    'mulw'      : (op.unknown, ),
    'mv'        : (op.unknown, ),
    'not'       : (op.unknown, ),
    'or'        : (op.unknown, ),
    'ori'       : (op.unknown, ),
    'rem'       : (op.unknown, ),
    'remu'      : (op.unknown, ),
    'remw'      : (op.unknown, ),
    'ret'       : (op.unknown, ),
    'sb'        : (op.unknown, ),
    'sc.d'      : (op.unknown, ),
    'sc.w'      : (op.unknown, ),
    'sd'        : (op.unknown, ),
    'seqz'      : (op.unknown, ),
    'sext.w'    : (op.unknown, ),
    'sfence.vma': (op.unknown, ),
    'sh'        : (op.unknown, ),
    'sll'       : (op.unknown, ),
    'slli'      : (op.unknown, ),
    'slliw'     : (op.unknown, ),
    'sllw'      : (op.unknown, ),
    'sltu'      : (op.unknown, ),
    'snez'      : (op.unknown, ),
    'srai'      : (op.unknown, ),
    'sraiw'     : (op.unknown, ),
    'sraw'      : (op.unknown, ),
    'sret'      : (op.unknown, ),
    'srl'       : (op.unknown, ),
    'srli'      : (op.unknown, ),
    'srliw'     : (op.unknown, ),
    'srlw'      : (op.unknown, ),
    'sub'       : (op.unknown, ),
    'subw'      : (op.unknown, ),
    'sw'        : (op.unknown, ),
    'xor'       : (op.unknown, ),
}
opcodes = {}
for line_s in lines:
    line = line_s.replace("\n", "").split()
    if len(line) < 3 or not line[2].startswith("0x0"):
        continue
    _, _, pc, insn_hex, opcode, *args = line
    opcodes[opcode] = line_s
for o in sorted(opcodes):
    print(opcodes[o])