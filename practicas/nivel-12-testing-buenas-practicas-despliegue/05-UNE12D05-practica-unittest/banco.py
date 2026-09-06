from decimal import Decimal


class Cuenta:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = Decimal(str(saldo))

    def depositar(self, monto):
        monto = Decimal(str(monto))
        if monto <= 0:
            raise ValueError("El depósito debe ser positivo")
        self.saldo += monto
        return self.saldo

    def retirar(self, monto):
        monto = Decimal(str(monto))
        if monto <= 0 or monto > self.saldo:
            raise ValueError("Retiro no permitido")
        self.saldo -= monto
        return self.saldo
