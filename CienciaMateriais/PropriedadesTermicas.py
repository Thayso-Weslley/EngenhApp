class PropriedadesTermicas:
    def calcular_capacidade_calorifica(self, calor_transferido: float, massa: float, delta_temperatura: float) -> float:
        """Calcula a capacidade calorífica de um material.

        Entrada:
            calor_transferido (float): Quantidade de calor transferido (em J).
            massa (float): Massa do material (em kg).
            delta_temperatura (float): Variação da temperatura (em K ou °C).

        Saída:
            float: Capacidade calorífica (em J/K ou J/°C). Retorna None se massa ou delta_temperatura forem zero.
        """
        if massa == 0 or delta_temperatura == 0:
            return None
        return calor_transferido / delta_temperatura

    def calcular_calor_especifico(self, calor_transferido: float, massa: float, delta_temperatura: float) -> float:
        """Calcula o calor específico de um material.

        Entrada:
            calor_transferido (float): Quantidade de calor transferido (em J).
            massa (float): Massa do material (em kg).
            delta_temperatura (float): Variação da temperatura (em K ou °C).

        Saída:
            float: Calor específico (em J/(kg.K) ou J/(kg.°C)). Retorna None se massa ou delta_temperatura forem zero.
        """
        if massa == 0 or delta_temperatura == 0:
            return None
        return calor_transferido / (massa * delta_temperatura)

    def obter_condutividade_termica(self):
        """Função placeholder para obter a condutividade térmica.

        A condutividade térmica é uma propriedade do material e geralmente é obtida de tabelas.
        Esta função pode ser expandida para solicitar o tipo de material e consultar um banco de dados.

        Saída:
            str: Uma mensagem indicando como obter a condutividade térmica.
        """
        return "A condutividade térmica é uma propriedade do material e geralmente é obtida de tabelas."

    def calcular_expansao_termica_linear(self, coeficiente_expansao: float, comprimento_inicial: float, delta_temperatura: float) -> float:
        """Calcula a variação no comprimento devido à expansão térmica linear.

        Entrada:
            coeficiente_expansao (float): Coeficiente de expansão térmica linear (em 1/K ou 1/°C).
            comprimento_inicial (float): Comprimento inicial do material (em m).
            delta_temperatura (float): Variação da temperatura (em K ou °C).

        Saída:
            float: Variação no comprimento (em m).
        """
        return coeficiente_expansao * comprimento_inicial * delta_temperatura

    def calcular_comprimento_final_expansao_linear(self, comprimento_inicial: float, delta_comprimento: float) -> float:
        """Calcula o comprimento final após a expansão térmica linear.

        Entrada:
            comprimento_inicial (float): Comprimento inicial do material (em m).
            delta_comprimento (float): Variação no comprimento (em m).

        Saída:
            float: Comprimento final (em m).
        """
        return comprimento_inicial + delta_comprimento

# Exemplo de uso (pode ser integrado ao seu menu):
if __name__ == "__main__":
    prop_termicas = PropriedadesTermicas()

    # Calcular capacidade calorífica
    calor = 1000  # J
    massa = 0.5  # kg
    dt = 20  # K
    capacidade = prop_termicas.calcular_capacidade_calorifica(calor, massa, dt)
    print(f"Capacidade Calorífica: {capacidade:.2f} J/K")

    # Calcular calor específico
    calor_especifico = prop_termicas.calcular_calor_especifico(calor, massa, dt)
    print(f"Calor Específico: {calor_especifico:.2f} J/(kg.K)")

    # Obter condutividade térmica
    condutividade = prop_termicas.obter_condutividade_termica()
    print(f"Condutividade Térmica: {condutividade}")

    # Calcular expansão térmica linear
    alpha = 12e-6  # 1/K (aço)
    l0 = 1  # m
    dt_expansao = 50  # K
    delta_l = prop_termicas.calcular_expansao_termica_linear(alpha, l0, dt_expansao)
    print(f"Variação no Comprimento (Expansão Térmica): {delta_l:.6f} m")

    # Calcular comprimento final
    lf = prop_termicas.calcular_comprimento_final_expansao_linear(l0, delta_l)
    print(f"Comprimento Final: {lf:.6f} m")