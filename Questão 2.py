class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia

    def status(self):
        return f"Motor: Tipo={self.tipo}, Potência={self.potencia} HP"

class Pneu:
    def __init__(self, tamanho, tipo):
        self.tamanho = tamanho
        self.tipo = tipo

    def status(self):
        return f"Pneu: Tamanho={self.tamanho}, Tipo={self.tipo}"

class Veiculo(Motor, Pneu):
    def __init__(self, tipo_motor, potencia_motor, tamanho_pneu, tipo_pneu):
        Motor.__init__(self, tipo_motor, potencia_motor)
        Pneu.__init__(self, tamanho_pneu, tipo_pneu)

    def status(self):
        motor_status = Motor.status(self)
        pneu_status = Pneu.status(self)
        return f"Veículo:\n{motor_status}\n{pneu_status}"

veiculo = Veiculo("V8", 450, "18 polegadas", "Radial")
print(veiculo.status())