from Mips_table import *

arq = input("Digite o nome do arquivo: ")
file = open(arq, 'r')
print('')
for cmd in file:
    cmd = cmd.replace('\n','')
    inst, regs = split_cmd(cmd)
    reg_tipe= code_order(inst)
    code = code_inst(inst)
    print(cmd)
    i=0
    for reg in regs:
        code = replace_code(code, reg_tipe[i], code_reg(reg))
        i+=1
    print(code)
    print(bin_to_hex(code))
input("\n========================\nPressione enter pra sair")
