arquivoSenha =  open('SecretPasswordFile.txt')
senhaRecuperada = arquivoSenha.read()
print('Digite sua senha:')
senhaDigitada = input()
if str(senhaDigitada) == senhaRecuperada:
    print('Acesso permitido.')
    if str(senhaDigitada) == '12345':
        print('Tente criar uma senha mais complexa. Por favor...')
else:
    print('Acesso negado.')

    