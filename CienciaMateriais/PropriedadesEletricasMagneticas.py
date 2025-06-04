class PropriedadesEletricasMagneticas:
    def calcular_resistividade_eletrica(self, resistencia: float, area_secao: float, comprimento: float) -> float:
        """Calcula a resistividade elétrica de um material.

        Entrada:
            resistencia (float): Resistência elétrica (em Ω).
            area_secao (float): Área da seção transversal do condutor (em m²).
            comprimento (float): Comprimento do condutor (em m).

        Saída:
            float: Resistividade elétrica (em Ω.m). Retorna None se o comprimento for zero.
        """
        if comprimento == 0:
            return None
        return (resistencia * area_secao) / comprimento

    def calcular_condutividade_eletrica(self, resistividade: float) -> float:
        """Calcula a condutividade elétrica de um material.

        Entrada:
            resistividade (float): Resistividade elétrica (em Ω.m).

        Saída:
            float: Condutividade elétrica (em S/m). Retorna None se a resistividade for zero.
        """
        if resistividade == 0:
            return None
        return 1 / resistividade

    def obter_permeabilidade_magnetica(self):
        """Função placeholder para obter a permeabilidade magnética.

        A permeabilidade magnética é uma propriedade do material e geralmente é obtida de tabelas.
        Ela pode ser a permeabilidade absoluta ou relativa.
        Esta função pode ser expandida para solicitar o tipo de material e consultar um banco de dados.

        Saída:
            str: Uma mensagem indicando como obter a permeabilidade magnética.
        """
        return "A permeabilidade magnética é uma propriedade do material e geralmente é obtida de tabelas (permeabilidade absoluta ou relativa)."

    def calcular_forca_magnetica_em_condutor(self, corrente: float, comprimento: float, campo_magnetico: float, angulo: float) -> float:
        """Calcula a força magnética em um condutor retilíneo percorrido por corrente em um campo magnético uniforme.

        Entrada:
            corrente (float): Corrente elétrica no condutor (em A).
            comprimento (float): Comprimento do condutor dentro do campo magnético (em m).
            campo_magnetico (float): Intensidade do campo magnético (em T).
            angulo (float): Ângulo entre a direção da corrente e o campo magnético (em radianos).

        Saída:
            float: Força magnética (em N).
        """
        return corrente * comprimento * campo_magnetico * math.sin(angulo)

# É necessário importar a biblioteca 'math' para usar a função 'sin'
import math

# Exemplo de uso (pode ser integrado ao seu menu):
if __name__ == "__main__":
    prop_eletro_magneticas = PropriedadesEletricasMagneticas()

    # Calcular resistividade elétrica
    resistencia = 10  # Ω
    area = 1e-6  # m²
    comprimento = 1  # m
    resistividade = prop_eletro_magneticas.calcular_resistividade_eletrica(resistencia, area, comprimento)
    print(f"Resistividade Elétrica: {resistividade:.2e} Ω.m")

    # Calcular condutividade elétrica
    condutividade = prop_eletro_magneticas.calcular_condutividade_eletrica(resistividade)
    print(f"Condutividade Elétrica: {condutividade:.2e} S/m")

    # Obter permeabilidade magnética
    permeabilidade = prop_eletro_magneticas.obter_permeabilidade_magnetica()
    print(f"Permeabilidade Magnética: {permeabilidade}")

    # Calcular força magnética em condutor
    corrente = 2  # A
    comprimento_condutor = 0.5  # m
    campo = 0.1  # T
    angulo_graus = 90
    angulo_radianos = math.radians(angulo_graus)
    forca_magnetica = prop_eletro_magneticas.calcular_forca_magnetica_em_condutor(corrente, comprimento_condutor, campo, angulo_radianos)
    print(f"Força Magnética no Condutor: {forca_magnetica:.3f} N")