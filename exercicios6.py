import regex as re

frase = '(85)985558599'
if re.search('[-|+]?\d+([.]\d+)?',frase)[0] == frase:
    print('Valid')
else:
    print('Not valid')

if re.search("[(?]\d?\d\d[)?] ?\d\d\d\d\d[ |-]?\d\d\d\d", frase)[0] == frase:
    print('Celular')
else:
    print('Fixo')

