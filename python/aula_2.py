# \r\n -> CRLF
# \N -> LF

'''
sep='' -> Defini algo para separar os meus valores, ex: sep='/' 

end='' -> Defini algo que será exibido no final do último valor, por padrão é o valor \r\n. Ex: *

tipagem estática, tipagem dinâmica, tipagem forte e tipagem fraca
'''
print( 10, 11, 12, sep='-', end='*\n'  )
print(100,101,102, sep='/', end=' FIM\n')
print('oi "mano"')