# conversão de tipos, coerção 
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro tipos
# imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')))
print(float(10) + 1) #Conversão de inteiro para float.

print(type(int(10)))
print(int(2.0) + 5) #Conversão de float para inteiro.

print(type(str(10)))
print(str(10) + "b") #Conversão de inteiro para string.

print(int("100") + 80) #Conversão de string para inteiro.
print(float('100') + 5.0) #Conversão de string para float.

print(bool(' '))