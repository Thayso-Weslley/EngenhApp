class Difusao:
    def calcular_fluxo_difusao_fick_primeira_lei(self, coeficiente_difusao: float, gradiente_concentracao: float) -> float:
        """Calcula o fluxo de difusão usando a primeira lei de Fick (estado estacionário).

        Entrada:
            coeficiente_difusao (float): Coeficiente de difusão (em m²/s).
            gradiente_concentracao (float): Gradiente de concentração (dC/dx) (em (kg/m³)/m ou similar).

        Saída:
            float: Fluxo de difusão (em kg/(m².s) ou similar).
        """
        return -coeficiente_difusao * gradiente_concentracao

    def obter_coeficiente_difusao(self):
        """Função placeholder para obter o coeficiente de difusão.

        O coeficiente de difusão depende do material, da espécie que se difunde e da temperatura.
        Geralmente é obtido de tabelas ou através de modelos específicos (ex: equação de Arrhenius).
        Esta função pode ser expandida para solicitar essas informações e consultar um banco de dados ou aplicar um modelo.

        Saída:
            str: Uma mensagem indicando como obter o coeficiente de difusão.
        """
        return "O coeficiente de difusão depende do material, da espécie difusora e da temperatura, geralmente obtido de tabelas ou modelos."

    def calcular_distancia_difusao_aproximada(self, coeficiente_difusao: float, tempo: float) -> float:
        """Calcula uma distância de difusão aproximada em um determinado tempo (raiz quadrada da multiplicação de D e t).

        Esta é uma estimativa e não leva em conta condições de contorno ou variações na concentração.

        Entrada:
            coeficiente_difusao (float): Coeficiente de difusão (em m²/s).
            tempo (float): Tempo de difusão (em s).

        Saída:
            float: Distância de difusão aproximada (em m). Retorna None se o coeficiente de difusão ou o tempo forem negativos.
        """
        if coeficiente_difusao < 0 or tempo < 0:
            return None
        return (coeficiente_difusao * tempo)**0.5

# Exemplo de uso (pode ser integrado ao seu menu):
if __name__ == "__main__":
    difusao = Difusao()

    # Calcular fluxo de difusão (Primeira Lei de Fick)
    D = 1e-10  # m²/s (exemplo)
    dCdx = -100  # (kg/m³)/m (exemplo)
    fluxo = difusao.calcular_fluxo_difusao_fick_primeira_lei(D, dCdx)
    print(f"Fluxo de Difusão: {fluxo:.2e} kg/(m².s)")

    # Obter coeficiente de difusão
    coeficiente = difusao.obter_coeficiente_difusao()
    print(f"Coeficiente de Difusão: {coeficiente}")

    # Calcular distância de difusão aproximada
    tempo_difusao = 3600  # s (1 hora)
    distancia = difusao.calcular_distancia_difusao_aproximada(D, tempo_difusao)
    print(f"Distância de Difusão Aproximada: {distancia:.2e} m")