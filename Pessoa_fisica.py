from Inscrição import Inscrição

class Pessoa_fisica (Inscrição):
    
     def __init__(self):
        self.cpf = None
        self.rg = None


     def realizar_incrição(self):
         print("Realizando inscrição de pessoa física")
    