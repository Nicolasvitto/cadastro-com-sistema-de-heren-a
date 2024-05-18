from Pessoa_fisica import Pessoa_fisica
from Pessoa_juridica import Pessoa_juridica

pf = Pessoa_fisica
pj = Pessoa_juridica

def dados_pf ():
    pf.cpf = input("digite seu cpf: ")
    pf.nome = input("digite seu nome: ")
    pf.rg = input("digite seu rg: ")
    pf.endereço = input("digite seu endereco: ")    
    pf.telefone = input("digite seu telefone: ")
    pf.email = input("digite seu email: ")
    pf.data_nascimento = input("digite seu nascimento: ")
    pf.pais = input("coloque seu pais: ")
    pf.cidade = input("coloque sua cidade: ")
    pf.estado = input("coloque seu estado: ")
    pf.genero = input("Homem ou Mulher: ")
    return pf 


def dados_pj ():
    pj.cnpj = input("digite seu cnpj: ")
    pj.nome = input("digite seu nome: ")
    pj.endereço = input("digite seu endereco: ")
    pj.telefone = input("digite seu telefone: ")
    pj.email = input("digite seu email: ")
    pj.data_nascimento = input("digite seu nascimento: ")
    pj.pais = input("coloque seu pais: ")
    pj.cidade = input("coloque sua cidade: ")
    pj.estado = input("coloque seu estado: ")
    return pj 

dados_pf
    
tipo_de_cadastro = input("coloque se você e (pf/pj): ")
    
if tipo_de_cadastro == "pf":
        pf = dados_pf()
        print(pf.cpf)
        print(pf.nome)
        print(pf.rg)
        print(pf.endereço)
        print(pf.telefone)
        print(pf.email)
        print(pf.data_nascimento)
        print(pf.pais)
        print(pf.cidade)
        print(pf.estado)
        print(pf.genero)

elif tipo_de_cadastro == "pj":
        pj = dados_pj()
        print(pj.cnpj)
        print(pj.nome)
        print(pj.endereço)
        print(pj.telefone)
        print(pj.email)
        print(pj.data_nascimento)
        print(pj.pais)
        print(pj.cidade)
        print(pj.estado)

else:
        print("tipo de cadastro não econtrado por favor escolha pf ou pj")

