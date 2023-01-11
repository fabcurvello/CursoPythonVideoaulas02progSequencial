cpf = "3655521304" #cpf é do tipo str
print("CPF inserido: {}".format(cpf))

if len(cpf) < 11:
    cpf = cpf.zfill(11) #zfill torna o str em 11 dígitos preenchendo com zeros iniciais
    print("CPF com função zfill(11): {}".format(cpf))

cpf_formatado = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
print("CPF Formatado: {}".format(cpf_formatado))
