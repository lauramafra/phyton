class Relogio:
    def __init__(self):
        self.__horas = 0
        self.__minutos = 0
        self.__segundos = 0

    #Setter
    def set_hora(self, h, m, s):
        if (0 <= h <= 23) and (0 <= m <= 59) and (0 <= s <= 59):
            self.__horas = h
            self.__minutos = m
            self.__segundos = s
            print("Horário configurado com sucesso!")
        else:
            print(f"Erro: Horário {h:02d}:{m:02d}:{s:02d} é inválido!")

    #Getter
    def get_hora(self):
        # :02d formata o número inteiro com 2 dígitos (ex: 7 vira "07")
        return f"{self.__horas:02d}:{self.__minutos:02d}:{self.__segundos:02d}"

    #Métodos
    def avancar_segundo(self):
        self.__segundos += 1

        if self.__segundos == 60:
            self.__segundos = 0
            self.__minutos += 1

            if self.__minutos == 60:
                self.__minutos = 0
                self.__horas += 1

                if self.__horas == 24:
                    self.__horas = 0

    def exibir(self):
        print(f"Hora atual: {self.get_hora()}")


relogio = Relogio()

# 1. Tentando definir uma hora inválida
relogio.set_hora(25, 61, 30)
print("-" * 30)

# 2. Configurando um horário válido (perto da virada de minuto/hora)
relogio.set_hora(23, 59, 58)
relogio.exibir() # 23:59:58
print("-" * 30)

# 3. Avançando vários segundos para ver o efeito cascata acontecer
print("Avançando 1 segundo...")
relogio.avancar_segundo()
relogio.exibir() # 23:59:59

print("Avançando mais 1 segundo... (Deve virar o dia!)")
relogio.avancar_segundo()
relogio.exibir() # 00:00:00

print("Avançando mais 3 segundos...")
relogio.avancar_segundo()
relogio.avancar_segundo()
relogio.avancar_segundo()
relogio.exibir() # 00:00:03