from time import sleep
class Customer:
    def  __init__(self, name:str , surname:str , idno:str , password:str):
        self.__name = name
        self.__surname = surname
        self.__idno = idno
        self.__password = password
        self.__bakiye = 0

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def getID(self):
        return self.__idno

    def getPassword(self):
        return self.__password

    def getBakiye(self):
        return self.__bakiye

    def setBakiye(self , amount:float):
        self.__bakiye = amount

class Bank:
    def __init__(self , name:str):
        self.__name = name
        self.__customers = list()

    def askedCustomer(self, idno:str , password:str):
        for i in self.__customers:
            if i.getIdNo == idno and i.getPassword() == password:
                return i

        return False

    def aliciVarMi(self,idno):
        for i in self.__customers:
            if i.getIdNo() == idno:
                return i
        return False

    def paraAktar(self, gonderen:Customer , alici:Customer , amount:float):
        if gonderen in self.__customers and alici in self.__customers:
            if gonderen.getBakiye() >= amount:
                gonderen.setBakiye(gonderen.getBakiye() - amount)
                alici.setBakiye(alici.getBakiye() + miktar)
                print("Money has been gone succesfully!!")
            else:
                print("Amount not enough")
        else:
            print("Customer not found!!")

    def beCustomer(self , name:str , surname:str ,  idno:str , password:str):
        self.__customers.append(Customer(name,surname,idno,password))

    def withdrawMoney(self, customer:Customer , amount:int):
        if amount % 10 != 0:
            print("You can withdraw x10 !!")

        else:
            if customer.getBakiye() >= amount:
                print("Take your money.")
                customer.setBakiye(customer.getBakiye() - amount)
            else:
                print("Money not enough")

    def sendMoney(self , customer:Customer , amount:int):
        if amount % 5 != 0:
            print("Dont send small money pls !!")

        else:
            customer.setBakiye(customer.getBakiye() + amount)
            print("Your money have been sent")

    def infoAmount(self, customer:Customer):
        print("""
        Name: {}
        Surname: {}
        Amount: {}
        """.format(customer.getName(),customer.getSurname(),customer.getBakiye()))

def main():
    bank = Bank("Ekinci Bank")
    while True:
        print("""
        [1] Being Customer
        [2] Sign In
        """)

        choice1 = input("Choice:  ")

        if choice1 == "1":
            name = input("Name: ")
            surname = input("Surname: ")
            idno = input("ID no: ")
            password = input("Password: ")
            bank.beCustomer(name,surname,idno,password)
            input("Click enter for turning to home menu")

        elif choice1 == "2":
            idno = input("ID no: ")
            password = input("Password: ")

            if bank.askedCustomer(idno,password):
                while True:
                    print("""
                    [1] Show Bakiye          [2] Send Money
                    [3] Withdraw Money       [4] Para Aktar
                                    [5] Exit
                    """)
                    choice2 = input("Your Operation: ")
                    if choice2 == "1":
                        bank.infoAmount(customer)
                        input("Click enter for turning to home menu")

                    elif choice2 == "2":
                        amount = int(input("Amount: "))
                        bank.sendMoney(csutomer,amount)
                        input("Click enter for turning to home menu")

                    elif choice2 == "3":
                        amount = int(input("Amount: "))
                        bank.withdrawMoney(customer, amount)
                        input("Click enter for turning to home menu")

                    elif choice2 == "4":
                        idno = input("Alıcı ID: ")
                        amount = float(input("Amount: "))
                        if bank.aliciVarMi(idno):
                            bank.paraAktar(customer ,bank.aliciVarMi(idno),amount)
                        else:
                            print("Customer nout found")

                    elif choice2 == "5":
                        print("Redirectring...")
                        sleep(2)
                        break
                    else:
                        print("False input!!")

            else:
                print("There is no bank record or false password..")

        else:
            print("False İnput..")

if __name__ == "__main__":
    main()
