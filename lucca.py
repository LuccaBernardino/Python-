# fome = True

# if fome == True:
#     print("Vou comer")
# else:
#     print("Não vou comer")
#--------------------------------------------------
# idade = 18

# if idade == 18:
#     print("Tenho 18y")
# else:
#     print("Não tenho 18y")
#----------------------------------------------------------
# idade = int(input())

# if idade > 17:
#     print("ela é maior de idade")
# else:
#     print("ela não é maior de idade")
# ---------------------------------------------------------------


# idade = int(input("digite a idade da criança"))

# if idade <= 10:
#     print("ela pode brincar")
# else:
#     print("ela não pode brincar")

# ---------------------------------------------------------------------

# idade = int(input("digite sua idade"))

# if idade >= 18:
#     print("obrigadorio a votar")
# elif idade >= 16:
#     print("opcional a votar")
# else:
#     print("ela não pode votar")
# ---------------------------------------------------------------------

# idade = int(input("digite a idade: "))

# if idade >= 50 and idade <= 60:
#     print("pode ir na festa")
# else: 
#     print("não pode ir na festa")

# ---------------------------------------------------------------------

# idade = int(input("digite sua idade: "))

# if idade >= 10 and idade <=15:
#     print("pode entrar na festa")
# else:
#     print("não pode entrar na festa")
# ---------------------------------------------------------------------

# idade = int(input("digite a idade: "))

# if idade == 20 or idade ==30:
#     print("pode entrar")
# else: 
#     print("não pode entrar")
#---------------------------------------------------------------------
# Switch-Case
# sabor ="morango"

# switch(sabor) {
#     case "morango":
#         print("comi sorvete de morango");
#         break;
        
#      case "chocolate":
#         print("comi sorvete de chocolate");
#         break;
        
#      case "baunilha":
#         print("comi sorvete de baunilha");
#         break;
# }

#---------------------------------------------------------------------


Alunos = int(input("quantos alunos tem: "))
Monitor = int(input("quantos monitores tem: "))

if Monitor < 1:
    print("não podem fazer a viagem")
elif Alunos <= 9:
    print ("preicsa fazer só uma viagem")
else:
    viagens = 1
    while Alunos > 9:
      Alunos = Alunos - 9
      viagens = viagens +1
    print("Qtd viagens", viagens)