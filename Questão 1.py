import turtle

class Forma:
    def desenhar(self):
        raise NotImplementedError("Subclasses devem implementar o método desenhar()")

class Circulo(Forma):
    def __init__(self, raio):
        self.raio = raio

    def desenhar(self):
        turtle.circle(self.raio)

class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def desenhar(self):
        for _ in range(4):
            turtle.forward(self.lado)
            turtle.right(90)
            
# Criando objetos e desenhando
circulo = Circulo(50)
quadrado = Quadrado(100)

circulo.desenhar()
quadrado.desenhar()

turtle.done()