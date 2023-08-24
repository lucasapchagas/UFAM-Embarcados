#FUNÇÕES:

hex_to_bin_dict = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011','4': '0100', '5': '0101', '6': '0110', '7': '0111','8': '1000', '9': '1001', 'A': '1010', 'B': '1011','C': '1100', 'D': '1101', 'E': '1110', 'F': '1111','a': '1010', 'b': '1011', 'c': '1100', 'd': '1101','e': '1110', 'f': '1111'
    }

# função que pega um hexadecimal e converte para o equivalente em binario de "tam" bits
def hex_to_bin(hexa, tam):
    retorno = ""
    if(len(hexa) > 2 and "0x" in hexa):
        for h in range(2, len(hexa)):
            if(hexa[h] != " "):
                retorno += hex_to_bin_dict[hexa[h]]
        
        if(tam >= len(retorno)):
            while(len(retorno) != tam):
                retorno = "0" + retorno
        else:
            print("tamanho do retorno é menor que a conversão feita")
            return 
        return retorno
    else:
        print("hexadecimal invalido, use o formato 0x<algo>")


def bin_to_int(binario):
    resultado = 0
    pos = 0

    for i in range(len(binario) -1, -1, -1):
        resultado += int(binario[i]) * (2 ** pos)
        pos += 1

    return resultado


def int_to_bin(num, tam):
    num_bin = bin(num)[2:]
    if(tam >= len(num_bin)):
        while(len(num_bin) != tam):
            num_bin = "0" + num_bin
        return num_bin
    else:
        print('valor inválido')


def int_to_hex(num, tam):
    num_hex = hex(num)[2:]
    if(tam >= len(num_hex)):
        while(len(num_hex) != tam):
            num_hex = "0" + num_hex
        num_hex = "0x" + num_hex
        return num_hex
    else:
        print('valor inválido')


def bin_to_hex(binario, tam):
    tam_real = tam * 4
    binario_retorno = binario
    hexa_retorno = ""  
    
    if tam_real >= len(binario):
        while len(binario_retorno) != tam_real:  
            binario_retorno = "0" + binario_retorno
        
        for i in range(0, len(binario_retorno), 4):
            binario_agrupado = binario_retorno[i:i+4]
            hex_digit = hex(int(binario_agrupado, 2))[2:]
            hexa_retorno += hex_digit
        
        return "0x" + hexa_retorno
    else:
        print("Tamanho da conversão é maior que o permitido no parâmetro")
        return


def complemento(binario):
    retorno = ""
    if("0x" not in binario):
        for i in range(len(binario)):
            if(binario[i] == "0"):
                retorno += "1"
            else:
                retorno += "0"
        return retorno
    else:
        print("funcao aceita apenas binarios, nao hexacimais")


#SLIDES:

#SLIDE 4:
print("SLIDE 4:")
hexa1 = "0x7FF"
bin1 = hex_to_bin(hexa1,12)
print(f"Hexadecimal: {hexa1} == {bin1}.")
complemento1 = complemento(bin1)
print(f"aplicando o complemento, temos que: ~{bin1} == {complemento1}")
print(f"que corresponde a: {bin_to_hex(complemento1,4)}")

#SLIDE 5:
print("\nSLIDE 5:")
print("Outros exemplos (32 bits):")
exemplos = ["0xC5", "0x1111","0xFFFF","0x5B3C"]
# eh necessario mudar o parametro da conversao para 32 bits para ficar que nem o do slide
for exemplo in exemplos:
    binario = hex_to_bin(exemplo,32)
    complemento_binario = complemento(binario)
    print(f"~{exemplo} == {bin_to_hex(complemento_binario,8)}")

# mais exemplos do slide 5
bin2 = "00000000000000000000000011000101"
bin3 = "11111111111111111111111100111010"

print(f"\n{bin2} == {bin_to_hex(bin2,8)}")
print(f"{bin3} == {bin_to_hex(bin3,8)}")


#SLIDES 8,9:
print("\nSLIDES 8, 9:")
a = "0x6DB7"
b = "0xA726"
bin_a = hex_to_bin(a,16)
complemento_a = complemento(bin_a)
bin_b = hex_to_bin(b,16)
complemento_b = complemento(bin_b)

print(f"a = {bin_a} = {a}")
print(f"~a = {complemento_a} = {bin_to_hex(complemento_a,4)}")

print(f"\nb = {bin_b} = {b}")
print(f"~b = {complemento_b} = {bin_to_hex(complemento_b,4)}")

#SLIDE 10:
print("\nSLIDE 10:")
a_bin = hex_to_bin(a,16)
b_bin = hex_to_bin(b,16)

print(f"a = {a_bin} = {a}\nb = {b_bin} = {b}")

#convertendo os binarios para inteiros pois o operador & do python não recebe strings  
a_and_b = (bin_to_int(a_bin)) & (bin_to_int(b_bin))
a_and_b_bin = int_to_bin(a_and_b, 16)
a_and_b_hex = int_to_hex(a_and_b, 4)
print(f"a&b = {bin(a_and_b)[2:]} = {a_and_b_hex}")


#SLIDE 11:
print("\nSLIDE 11:")

#realizando processo semelhante ao slide 10 (acima)
a_xor_b = (bin_to_int(a_bin)) ^ (bin_to_int(b_bin))
a_xor_b_bin = int_to_bin(a_xor_b, 16)
a_xor_b_hex = int_to_hex(a_xor_b, 4)
print(f"a = {a_bin} = {a}\nb = {b_bin} = {b}\na^b = {a_xor_b_bin} = {a_xor_b_hex}")


#SLIDE 12:

print("\nSLIDE 12:")

#realizando processo semelhante ao slide 10 (acima)
a_or_b = (bin_to_int(a_bin)) | (bin_to_int(b_bin))
a_or_b_bin = int_to_bin(a_or_b, 16)
a_or_b_hex = int_to_hex(a_or_b, 4)
print(f"a = {a_bin} = {a}\nb = {b_bin} = {b}\na^b = {a_or_b_bin} = {a_or_b_hex}")


#SLIDE 15:
print("\nSLIDE 15:")

a = "0x6DB7"
mascara = "0x3F"

#convertendo os hexas para binario
a_bin = hex_to_bin(a, 16)
mascara_bin = hex_to_bin(mascara, 16)

# convertendo a e a mascara para inteiro, pois o operador & nao aceita strings
b = (bin_to_int(a_bin)) & (bin_to_int(mascara_bin)) # b eh um inteiro
b_hex = int_to_hex(b, 2)
b_bin = hex_to_bin(b_hex, 16)

print(f"a = {a_bin} = {a}\nM = {mascara_bin} = {mascara}\nb = {b_bin} = {b_hex}")


#SLIDE 17:
print("\nSLIDE 17:")

a = "0x6DB7"
mascara = "0xFC00"

#convertendo os hexas para binario
a_bin = hex_to_bin(a, 16)
mascara_bin = hex_to_bin(mascara, 16)

# convertendo a e a mascara para inteiro, pois o operador & nao aceita strings
b = (bin_to_int(a_bin)) & (bin_to_int(mascara_bin)) # b eh um inteiro
b_hex = int_to_hex(b, 4)
b_bin = hex_to_bin(b_hex, 16)

print(f"a = {a_bin} = {a}\nM = {mascara_bin} = {mascara}\nb = {b_bin} = {b_hex}")


#SLIDE 20:
print("\nSLIDE 20:")

a = "0x6DB7"
mascara = "0xFF"

#convertendo os hexas para binario
a_bin = hex_to_bin(a, 16)
mascara_bin = hex_to_bin(mascara, 16)

# convertendo a e a mascara para inteiro, pois o operador | nao aceita strings
b = (bin_to_int(a_bin)) | (bin_to_int(mascara_bin)) # b eh um inteiro
b_hex = int_to_hex(b, 4)
b_bin = hex_to_bin(b_hex, 16)

print(f"a = {a_bin} = {a}\nM = {mascara_bin} = {mascara}\nb = {b_bin} = {b_hex}")


#SLIDE 22:

print("\nSLIDE 22:")

a = "0x6DB7"
mascara = "0xFF00"

#convertendo os hexas para binario
a_bin = hex_to_bin(a, 16)
mascara_bin = hex_to_bin(mascara, 16)

# convertendo a e a mascara para inteiro, pois o operador | nao aceita strings
b = (bin_to_int(a_bin)) | (bin_to_int(mascara_bin)) # b eh um inteiro
b_hex = int_to_hex(b, 4)
b_bin = hex_to_bin(b_hex, 16)

print(f"a = {a_bin} = {a}\nM = {mascara_bin} = {mascara}\nb = {b_bin} = {b_hex}")


#SLIDE 24:
print("\nSLIDE 24:")

a = "0x6DB7"
mascara = "0xFF"

#convertendo os hexas para binario
a_bin = hex_to_bin(a, 16)
mascara_bin = hex_to_bin(mascara, 16)

# convertendo a e a mascara para inteiro, pois o operador ^ nao aceita strings
b = (bin_to_int(a_bin)) ^ (bin_to_int(mascara_bin)) # b eh um inteiro
b_hex = int_to_hex(b, 4)
b_bin = hex_to_bin(b_hex, 16)

print(f"a = {a_bin} = {a}\nM = {mascara_bin} = {mascara}\nb = {b_bin} = {b_hex}")


#SLIDE 25:
print("\nSLIDE 25:")

a = "0x6DB7"
mascara = "0xFF00"

#convertendo os hexas para binario
a_bin = hex_to_bin(a, 16)
mascara_bin = hex_to_bin(mascara, 16)

# convertendo a e a mascara para inteiro, pois o operador ^ nao aceita strings
b = (bin_to_int(a_bin)) ^ (bin_to_int(mascara_bin)) # b eh um inteiro
b_hex = int_to_hex(b, 4)
b_bin = hex_to_bin(b_hex, 16)

print(f"a = {a_bin} = {a}\nM = {mascara_bin} = {mascara}\nb = {b_bin} = {b_hex}")


#SLIDE 27:
print("\nSLIDE 27:")

a = "0x6DB7"
mascara = "0x4"

#convertendo os hexas para binario
a_bin = hex_to_bin(a, 16)
mascara_bin = hex_to_bin(mascara, 16)

# convertendo a e a mascara para inteiro, pois o operador ^ nao aceita strings
b = (bin_to_int(a_bin)) ^ (bin_to_int(mascara_bin)) # b eh um inteiro
b_hex = int_to_hex(b, 4)
b_bin = hex_to_bin(b_hex, 16)

# operando b novamente com a mascara 0x4 e retornando ao valor original de a
c = b ^ (bin_to_int(mascara_bin)) # c eh um inteiro
c_hex = int_to_hex(c, 4)
c_bin = hex_to_bin(c_hex, 16)

print(f"a = {a_bin} = {a}\nM = {mascara_bin} = {mascara}\nb = {b_bin} = {b_hex}")
print(f"M = {mascara_bin} = {mascara}\nc = {c_bin} = {c_hex}")


# SLIDE 33:
print("\nSLIDE 33:")

x = 1 # 00000001 (binario de 8 bits)

# como a entrada ja eh um inteiro, sem problemas para o operador, retorno inteiro
x0 = (x << 0) # 0000 0001 Não deslocadox1 = (x << 1); // 0000 0010
x1 = (x << 1) # 0000 0010
x2 = (x << 2) # 0000 0100
x3 = (x << 3) # 0000 1000
x4 = (x << 4) # 0001 0000
x5 = (x << 5) # 0010 0000
x6 = (x << 6) # 0100 0000
x7 = (x << 7) # 1000 0000

# criando uma lista para impressão mais fácil
numeros_deslocados = [x0,x1,x2,x3,x4,x5,x6,x7]
vez = 0
print("numeros deslocados a partir de 0000 0001:")
for numero in numeros_deslocados:
    print(int_to_bin(numero, 8), ":",vez, "vezes") # imprimir representacao binaria do numero
    vez +=1


#SLIDE 34:
print("\nSLIDE 34:")

x = 128 # 10000000 (binario de 8 bits)

# como a entrada ja eh um inteiro, sem problemas para o operador, retorno inteiro
x0 = (x >> 0) # 1000 0000 Não deslocadox1 = (x >> 1); // 0100 0000
x2 = (x >> 2) # 0010 0000
x3 = (x >> 3) # 0001 0000
x4 = (x >> 4) # 0000 1000
x5 = (x >> 5) # 0000 0100
x6 = (x >> 6) # 0000 0010
x7 = (x >> 7) # 0000 0001

# criando uma lista para impressão mais fácil
numeros_deslocados = [x0,x1,x2,x3,x4,x5,x6,x7]
vez = 0
print("numeros deslocados a partir de 1000 0000:")
for numero in numeros_deslocados:
    print(int_to_bin(numero, 8), ":",vez, "vezes") # imprimir representacao binaria do numero
    vez +=1


#SLIDE 36:
print("\nSLIDE 36:")

"""
convertendo a para inteiro para uso do operador <<,porem o operador << 
esta adicionando 6 bits menos significativos. Ou seja,em vez de perdermos 
os 6 bits mais signifcativos, está sendo apenas adicionados 6 0's menos 
significativos. Logo, preciso fazer o deslocamento de 6 bits (<< 6) e depois 
filtrar os 16 bits menos significativos, para excluir os que foram perdidos, 
pois nossa palavra eh de 16 bits.
"""

a = "0110110110110111"
mascara = "0xFFFF"
b = (bin_to_int(a)) << 6 # fazendo o deslocamento de 6 bits

#convertendo a mascara para inteiro e filtrando os 16 menos significativos
b = b & (bin_to_int(hex_to_bin(mascara,16)))

b_hex = int_to_hex(b,4)
b_bin = int_to_bin(b,16)

print(f"b = {b_hex}")
print(f"{a} bits antes do deslocamento\n{b_bin} bits apos o deslocamento, seis 0's deram lugar aos seis bits menos significativos")


#SLIDE 38:
print("\nSLIDE 38:")

"""
Nesse caso, não é necessário fazer aquele procedimento, pois os seis bits
menos significativos realmente serão perdidos no deslocamento.
"""

a = "0110110110110111"
b = (bin_to_int(a)) >> 6 # fazendo o deslocamento de 6 bits

b_bin = int_to_bin(b,16)
b_hex = int_to_hex(b,4)

print(f"b = {b_hex}")
print(f"{a} bits antes do deslocamento\n{b_bin} bits apos o deslocamento, seis 0's deram lugar aos seis bits mais significativos")
