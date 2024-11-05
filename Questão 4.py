from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, numero_conta, titular, saldo_inicial=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo_inicial

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass

    @abstractmethod
    def calcular_saldo(self):
        pass

    def exibir_informacoes(self):
        return f"Conta: {self.numero_conta}\nTitular: {self.titular}\nSaldo: R${self.calcular_saldo():.2f}"

class ContaCorrente(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo_inicial=0, limite_cheque_especial=1000):
        super().__init__(numero_conta, titular, saldo_inicial)
        self.limite_cheque_especial = limite_cheque_especial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso!"
        else:
            return "Valor de depósito deve ser positivo."

    def sacar(self, valor):
        if valor > 0:
            if self.saldo - valor >= -self.limite_cheque_especial:
                self.saldo -= valor
                return f"Saque de R${valor:.2f} realizado com sucesso!"
            else:
                return f"Saque negado. Limite do cheque especial excedido. Saldo disponível: R${self.saldo + self.limite_cheque_especial:.2f}."
        else:
            return "Valor de saque deve ser positivo."

    def calcular_saldo(self):
        return self.saldo

class ContaPoupanca(ContaBancaria):
    def __init__(self, numero_conta, titular, saldo_inicial=0, taxa_juros=0.02):
        super().__init__(numero_conta, titular, saldo_inicial)
        self.taxa_juros = taxa_juros

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso!"
        else:
            return "Valor de depósito deve ser positivo."

    def sacar(self, valor):
        if valor > 0:
            if self.saldo - valor >= 0:
                self.saldo -= valor
                return f"Saque de R${valor:.2f} realizado com sucesso!"
            else:
                return f"Saque negado. Saldo insuficiente. Saldo atual: R${self.saldo:.2f}."
        else:
            return "Valor de saque deve ser positivo."

    def calcular_saldo(self):
        saldo_com_juros = self.saldo + (self.saldo * self.taxa_juros)
        return saldo_com_juros

if __name__ == "__main__":

    conta_corrente = ContaCorrente(numero_conta="12345", titular="João Silva", saldo_inicial=500,
                                   limite_cheque_especial=2000)
    print(conta_corrente.exibir_informacoes())
    print(conta_corrente.depositar(1000))
    print(conta_corrente.sacar(2000))
    print(conta_corrente.sacar(4000))  # Tentando sacar mais que o limite do cheque especial
    print(conta_corrente.exibir_informacoes())

    print("\n----------------------\n")

    conta_poupanca = ContaPoupanca(numero_conta="67890", titular="Maria Oliveira", saldo_inicial=1000, taxa_juros=0.05)
    print(conta_poupanca.exibir_informacoes())
    print(conta_poupanca.depositar(500))
    print(conta_poupanca.sacar(2000))  # Tentando sacar mais que o saldo
    print(conta_poupanca.sacar(1200))  # Sacando um valor válido
    print(conta_poupanca.exibir_informacoes())