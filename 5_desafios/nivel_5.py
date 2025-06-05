# Validador de senha forte

import pwinput

senha = str(pwinput.pwinput(f"""\nSua nova senha deve atender os seguinte requisitos:
    - Pelo menos 8 caracteres de comprimento.
    - Conter pelo menos uma letra maiúscula.
    - Conter pelo menos uma letra minúscula.
    - Conter pelo menos um número.
    - Conter pelo menos um caractere especial (!, @, #, $, %, ^, &, *).
                                                               
Informe a senha desejada: """, mask="*"))

INVALIDO = "Senha inválida, critérios não atendidos!"
VALIDO = "Senha forte, criada com sucesso!"
CARACTERE_ESPECIAL = ["!, @, #, $, %, &, *"]

if len(senha) < 8 or \
    (not any(caractere.isupper() for caractere in senha)) or \
    (not any(caractere.islower() for caractere in senha)) or \
    (not any(caractere.isdigit() for caractere in senha)) or \
    (any(caractere in CARACTERE_ESPECIAL for caractere in senha)):
    print(INVALIDO,'\n')
else:
    print(VALIDO,'\n')