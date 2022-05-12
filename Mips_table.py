def bin_to_hex(code):
    h = '0123456789abcdef'
    b = ['0000','0001','0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
    hex_code='0x'
    codes = code.split(' ')
    for bits in codes:
        hex_code+=h[b.index(bits)]
    return hex_code

def a2(bits): # Erro 4->1111 1111 1111 101, deveria ser 4->111 1111 1111 1100
    bits_a2='0'
    for bit in bits:
        if bit=='0':
            bits_a2 += '1'
        else:
            bits_a2 += '0'
    bits = '' #0 1111 1111 1111 1011
    if bits_a2[-1] == '0':
        return bits_a2[1:-1]+'1'
    else:
        carry = '1'
        for i in range(17):
            if (bits_a2[16-i] == '0') and (carry == '0'):
                bits += '0'
                carry = '0'
            elif (bits_a2[16-i] == '1') ^ (carry == '1'):
                bits += '1'
                carry = '0'
            else:
                bits += '0'
                carry = '1'
        bits = bits[::-1]
    return bits[1:]

def bin_list_i(num):
    bits = bin(num).replace('b','').replace('-','')
    while len(bits)<16:
        bits = '0'+bits
    while len(bits)>16:
        bits = bits[1:]

    if(num<0):
        return a2(bits)
    return bits

def bin_list(num):
    bits = bin(num).replace('b','').replace('-','')
    while len(bits)<5:
        bits = '0'+bits
    while len(bits)>5:
        bits = bits[1:]
    return bits

def replace_code(string, target, bin_list):
	j=0
	code =""
	for i in range(len(string)):
		if string[i] == target:
			code += str(bin_list[j]) # Erro com numeros negativos
			j+=1
		else:
			code += string[i]
	return code

def is_int(reg):
    try:
        int(reg)
        return True
    except:
        return False

def code_reg(reg):
    if is_int(reg):
        return bin_list_i(int(reg))
    regs = ['$zero','$at','$v0','$v1','$a0','$a1','$a2','$a3',
            '$t0','$t1','$t2','$t3','$t4','$t5','$t6','$t7',
            '$s0','$s1','$s2','$s3','$s4','$s5','$s6','$s7',
            '$t8','$t9','$k0','$k1','$gp','$sp','$fp','$ra']
    return bin_list(regs.index(reg))

def code_inst(func):
    inst = ['add', 'addi', 'lw', 'mult']
    binary=['0000 00ss ssst tttt dddd d000 0010 0000',
            '0010 00ss ssst tttt iiii iiii iiii iiii',
            '1000 11ss ssst tttt iiii iiii iiii iiii',
            '0000 00ss ssst tttt 0000 0000 0001 1000']
    return binary[inst.index(func)]

def code_order(func):
    inst = ['add', 'addi', 'lw', 'mult']
    order = ['dst', 'tsi', 'tis', 'st']
    return order[inst.index(func)]

def split_cmd(cmd):
    aux = cmd.split(' ')
    inst = aux[0]
    regs = aux[1].split(',')

    if inst == 'lw':
        aux = regs[1].split('(')
        regs[1] = aux[0]
        regs.append(aux[1].replace(')',''))

    return inst, regs

'''
add $d, $s, $t      dst
addi $t, $s, imm    tsi
lw $t, offset($s)	tis
mult $s, $t         st
'''