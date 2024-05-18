from Inscrição import Inscrição

class Pessoa_juridica (Inscrição):
    
    def __init__(self):
        self.cnpj = None


    def horario_do_show (self):
        print("O show começa às 20:00")