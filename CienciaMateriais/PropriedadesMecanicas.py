class PropriedadesMecanicas:
    def calcular_tensao_normal(self, forca: float, area: float) -> float:
        """Calcula a tensão normal (tração ou compressão).

        Entrada:
            forca (float): Força aplicada (em N).
            area (float): Área da seção transversal onde a força atua (em m²).

        Saída:
            float: Tensão normal (em Pa).
        """
        if area == 0:
            raise ValueError("A área não pode ser zero.")
        return forca / area

    def calcular_tensao_cisalhamento(self, forca: float, area: float) -> float:
        """Calcula a tensão de cisalhamento.

        Entrada:
            forca (float): Força de cisalhamento aplicada (em N).
            area (float): Área da seção transversal paralela à força (em m²).

        Saída:
            float: Tensão de cisalhamento (em Pa).
        """
        if area == 0:
            raise ValueError("A área não pode ser zero.")
        return forca / area

    def calcular_deformacao_normal(self, delta_comprimento: float, comprimento_inicial: float) -> float:
        """Calcula a deformação normal (alongamento ou contração).

        Entrada:
            delta_comprimento (float): Variação no comprimento (em m).
            comprimento_inicial (float): Comprimento inicial (em m).

        Saída:
            float: Deformação normal (adimensional).
        """
        if comprimento_inicial == 0:
            raise ValueError("O comprimento inicial não pode ser zero.")
        return delta_comprimento / comprimento_inicial

    def calcular_deformacao_cisalhamento(self, deslocamento_lateral: float, comprimento_inicial: float) -> float:
        """Calcula a deformação de cisalhamento (tangente do ângulo de deformação).

        Entrada:
            deslocamento_lateral (float): Deslocamento lateral (em m).
            comprimento_inicial (float): Comprimento inicial perpendicular ao deslocamento (em m).

        Saída:
            float: Deformação de cisalhamento (adimensional).
        """
        if comprimento_inicial == 0:
            raise ValueError("O comprimento inicial não pode ser zero.")
        return deslocamento_lateral / comprimento_inicial

    def calcular_modulo_young(self, tensao_normal: float, deformacao_normal: float) -> float:
        """Calcula o módulo de Young (módulo de elasticidade).

        Entrada:
            tensao_normal (float): Tensão normal aplicada (em Pa).
            deformacao_normal (float): Deformação normal resultante (adimensional).

        Saída:
            float: Módulo de Young (em Pa). Retorna None se a deformação normal for zero.
        """
        if deformacao_normal == 0:
            return None
        return tensao_normal / deformacao_normal

    def calcular_modulo_cisalhamento(self, tensao_cisalhamento: float, deformacao_cisalhamento: float) -> float:
        """Calcula o módulo de cisalhamento (módulo de rigidez).

        Entrada:
            tensao_cisalhamento (float): Tensão de cisalhamento aplicada (em Pa).
            deformacao_cisalhamento (float): Deformação de cisalhamento resultante (adimensional).

        Saída:
            float: Módulo de cisalhamento (em Pa). Retorna None se a deformação de cisalhamento for zero.
        """
        if deformacao_cisalhamento == 0:
            return None
        return tensao_cisalhamento / deformacao_cisalhamento

    def calcular_coeficiente_poisson(self, deformacao_lateral: float, deformacao_axial: float) -> float:
        """Calcula o coeficiente de Poisson.

        Entrada:
            deformacao_lateral (float): Deformação na direção lateral (adimensional).
            deformacao_axial (float): Deformação na direção axial (adimensional).

        Saída:
            float: Coeficiente de Poisson (adimensional). Retorna None se a deformação axial for zero.
        """
        if deformacao_axial == 0:
            return None
        return -deformacao_lateral / deformacao_axial

    def obter_resistencia_tracao(self):
        """Função placeholder para obter a resistência à tração.

        A resistência à tração geralmente é uma propriedade tabelada para diferentes materiais.
        Esta função pode ser expandida para solicitar o tipo de material e consultar um banco de dados.

        Saída:
            str: Uma mensagem indicando como obter a resistência à tração.
        """
        return "A resistência à tração (UTS) é uma propriedade do material e geralmente é obtida de tabelas ou ensaios."

    def obter_limite_escoamento(self):
        """Função placeholder para obter o limite de escoamento.

        O limite de escoamento é uma propriedade do material e geralmente é obtido de tabelas ou ensaios.
        Esta função pode ser expandida para solicitar o tipo de material e consultar um banco de dados.

        Saída:
            str: Uma mensagem indicando como obter o limite de escoamento.
        """
        return "O limite de escoamento é uma propriedade do material e geralmente é obtido de tabelas ou ensaios."

    def calcular_ductilidade_alongamento(self, comprimento_final: float, comprimento_inicial: float) -> float:
        """Calcula a ductilidade como alongamento percentual.

        Entrada:
            comprimento_final (float): Comprimento do corpo de prova após a fratura (em m).
            comprimento_inicial (float): Comprimento inicial do corpo de prova (em m).

        Saída:
            float: Ductilidade (% de alongamento). Retorna None se o comprimento inicial for zero.
        """
        if comprimento_inicial == 0:
            return None
        return ((comprimento_final - comprimento_inicial) / comprimento_inicial) * 100

    def calcular_ductilidade_reducao_area(self, area_inicial: float, area_final: float) -> float:
        """Calcula a ductilidade como redução percentual de área.

        Entrada:
            area_inicial (float): Área da seção transversal inicial do corpo de prova (em m²).
            area_final (float): Área da seção transversal na fratura (em m²).

        Saída:
            float: Ductilidade (% de redução de área). Retorna None se a área inicial for zero.
        """
        if area_inicial == 0:
            return None
        return ((area_inicial - area_final) / area_inicial) * 100

    def obter_dureza(self):
        """Função placeholder para obter a dureza.

        A dureza é uma propriedade do material medida por diferentes escalas (Brinell, Vickers, Rockwell).
        Esta função pode ser expandida para solicitar o tipo de ensaio de dureza e o valor medido.

        Saída:
            str: Uma mensagem indicando como obter a dureza e as diferentes escalas.
        """
        return "A dureza é medida em diferentes escalas (Brinell, Vickers, Rockwell) e geralmente é obtida por ensaios específicos."

# Exemplo de uso (pode ser integrado ao seu menu):
if __name__ == "__main__":
    prop_mecanicas = PropriedadesMecanicas()

    # Calcular tensão normal
    forca = 10000  # N
    area = 0.01  # m²
    tensao = prop_mecanicas.calcular_tensao_normal(forca, area)
    print(f"Tensão Normal: {tensao:.2f} Pa")

    # Calcular deformação normal
    delta_l = 0.005  # m
    l0 = 0.1  # m
    deformacao = prop_mecanicas.calcular_deformacao_normal(delta_l, l0)
    print(f"Deformação Normal: {deformacao:.4f}")

    # Calcular Módulo de Young
    E = prop_mecanicas.calcular_modulo_young(tensao, deformacao)
    print(f"Módulo de Young: {E:.2e} Pa")

    # Calcular ductilidade (alongamento)
    lf = 0.12  # m
    alongamento = prop_mecanicas.calcular_ductilidade_alongamento(lf, l0)
    print(f"Ductilidade (Alongamento): {alongamento:.2f}%")

    # Obter propriedades que dependem de tabelas/ensaios
    uts = prop_mecanicas.obter_resistencia_tracao()
    print(f"Resistência à Tração: {uts}")
    sy = prop_mecanicas.obter_limite_escoamento()
    print(f"Limite de Escoamento: {sy}")
    dureza = prop_mecanicas.obter_dureza()
    print(f"Dureza: {dureza}")