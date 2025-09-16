from dataclasses import dataclass

@dataclass()
class Numero:
    numero: int
    def __init__(self, numero):
        self.numero = numero

    def evaluarnumero(self):
        if self.numero & 1:
            print("impar")
            if self.numero == 7:
                print("\n El numero ingresado es un comodin")

        else:
            print("par")
            if self.numero == 10:
                print("\n El numero ingresado es 10")


    def sumar(self ,numeroasumar):
        return self.numero + numeroasumar


if __name__ == "__main__":
    numeroaevaluar = Numero(int(input("Ingrese un numero:\n")))
    numeroaevaluar.evaluarnumero()
    sumarealizada = numeroaevaluar.sumar(2)
    print("\n la suma realizada es: ",sumarealizada)
    print("nueva linea")
    

    