class BankAccount:
    def __init__(self, account_number,pasta = 0):
       self. account_number = account_number
       self. pasta= pasta
    def conseguir_el_numerito (self):
        return self. account_number
    def cuanto_tienes(self):
        return self.pasta
    def deposit(self, fondos):
        self.pasta += fondos

        
    
cuenta1 = BankAccount("1", 115)
cuenta1.deposit(float(input("Cuanta pasta quieres meter? :" ) ))

print (f"Tu cuenta con el numero {cuenta1.conseguir_el_numerito()} tiene la increible cantidad de {cuenta1.cuanto_tienes()} euros")


    