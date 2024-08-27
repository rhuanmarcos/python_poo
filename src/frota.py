class Carro:
    modelo : str
    marca : str
    cor : str
    __odometro : 0.0
    __motor_on : False
    __tanque: float
    consumo_medio: float

    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool, tanque: float, consumo_medio: float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = odometro
        self.__motor_on = motor
        self.__tanque = tanque
        self.consumo_medio = consumo_medio

    def ligar(self):
        if not self.__motor_on:
            self.__motor_on = True
        else:
            raise Exception("Erro: Motor já ligado!")

    def acelerar(self, velocidade : float, tempo : float):
        if self.__motor_on and self.__tanque > 0:
            km = velocidade * tempo
            litros = km / self.consumo_medio

            if self.__tanque >= litros:
                self.__odometro += km
                self.__tanque -= litros
            else:
                km = self.__tanque * self.consumo_medio
                self.__odometro += km
                self.__tanque = 0
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado ou sem combustível!")


    def desligar(self):
        if self.__motor_on:
            self.__motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def getOdometro(self):
        return self.__odometro

    def getTanque(self):
        return self.__tanque

    def getMotorOn(self):
        return self.__motor_on

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.__motor_on}, consumo medio {self.consumo_medio}\n'
                f'tanque {self.__tanque}')
        return info

    def __repr__(self):
        return f'Carro(modelo="{self.modelo}", marca="{self.marca}", ' \
               f'cor="{self.cor}", odometro={self.__odometro}' \
               f'motor_on={self.__motor_on})'