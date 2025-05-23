class DinamicaFluidos:
    def calcular_vazao_volumetrica(self, area: float, velocidade_media: float) -> float:
        """Calcula a vazão volumétrica de um fluido.

        Entrada:
            area (float): Área da seção transversal do escoamento (em m²).
            velocidade_media (float): Velocidade média do fluido (em m/s).

        Saída:
            float: Vazão volumétrica (em m³/s).
        """
        return area * velocidade_media

    def calcular_vazao_massica(self, densidade: float, vazao_volumetrica: float) -> float:
        """Calcula a vazão mássica de um fluido.

        Entrada:
            densidade (float): Densidade do fluido (em kg/m³).
            vazao_volumetrica (float): Vazão volumétrica do fluido (em m³/s).

        Saída:
            float: Vazão mássica (em kg/s).
        """
        return densidade * vazao_volumetrica

    def aplicar_equacao_continuidade_incompressivel(self, area1: float, velocidade1: float, area2: float) -> float:
        """Aplica a equação da continuidade para escoamento incompressível para encontrar a velocidade 2.

        Entrada:
            area1 (float): Área da seção 1 (em m²).
            velocidade1 (float): Velocidade na seção 1 (em m/s).
            area2 (float): Área da seção 2 (em m²).

        Saída:
            float: Velocidade na seção 2 (em m/s). Retorna None se area2 for zero.
        """
        if area2 == 0:
            return None
        return (area1 * velocidade1) / area2

    def aplicar_equacao_continuidade_compressivel(self, densidade1: float, area1: float, velocidade1: float,
                                                area2: float, densidade2: float) -> float:
        """Aplica a equação da continuidade para escoamento compressível para encontrar a velocidade 2.

        Entrada:
            densidade1 (float): Densidade na seção 1 (em kg/m³).
            area1 (float): Área da seção 1 (em m²).
            velocidade1 (float): Velocidade na seção 1 (em m/s).
            area2 (float): Área da seção 2 (em m²).
            densidade2 (float): Densidade na seção 2 (em kg/m³).

        Saída:
            float: Velocidade na seção 2 (em m/s). Retorna None se (densidade2 * area2) for zero.
        """
        if (densidade2 * area2) == 0:
            return None
        return (densidade1 * area1 * velocidade1) / (densidade2 * area2)

    def calcular_equacao_bernoulli(self, pressao1: float, densidade: float, velocidade1: float, altura1: float,
                                  pressao2: float, velocidade2: float, altura2: float, gravidade: float = 9.81) -> str:
        """Calcula um termo desconhecido da equação de Bernoulli para escoamento ideal.

        Entrada:
            pressao1 (float): Pressão no ponto 1 (em Pa).
            densidade (float): Densidade do fluido (em kg/m³).
            velocidade1 (float): Velocidade no ponto 1 (em m/s).
            altura1 (float): Altura do ponto 1 em relação a um referencial (em m).
            pressao2 (float): Pressão no ponto 2 (em Pa).
            velocidade2 (float): Velocidade no ponto 2 (em m/s).
            altura2 (float): Altura do ponto 2 em relação ao mesmo referencial (em m).
            gravidade (float, optional): Aceleração da gravidade (em m/s²). Padrão é 9.81.

        Saída:
            str: Uma mensagem indicando qual termo pode ser calculado (implementação para cálculo específico pode ser adicionada).
        """
        return "Função para calcular um termo desconhecido da Equação de Bernoulli \n(requer implementação específica para isolar a variável desejada)."

    def calcular_perda_carga_distribuida(self, fator_atrito: float, comprimento: float, diametro: float,
                                         velocidade: float, gravidade: float = 9.81) -> float:
        """Calcula a perda de carga distribuída em uma tubulação reta usando a equação de Darcy-Weisbach.

        Entrada:
            fator_atrito (float): Fator de atrito de Darcy.
            comprimento (float): Comprimento da tubulação (em m).
            diametro (float): Diâmetro interno da tubulação (em m).
            velocidade (float): Velocidade média do fluido (em m/s).
            gravidade (float, optional): Aceleração da gravidade (em m/s²). Padrão é 9.81.

        Saída:
            float: Perda de carga distribuída (em m de coluna de fluido).
        """
        if diametro == 0:
            raise ValueError("O diâmetro não pode ser zero.")
        return fator_atrito * (comprimento / diametro) * (velocidade**2) / (2 * gravidade)

    def calcular_perda_carga_localizada(self, coeficiente_perda: float, velocidade: float, gravidade: float = 9.81) -> float:
        """Calcula a perda de carga localizada em um acessório.

        Entrada:
            coeficiente_perda (float): Coeficiente de perda local (K).
            velocidade (float): Velocidade média do fluido (em m/s).
            gravidade (float, optional): Aceleração da gravidade (em m/s²). Padrão é 9.81.

        Saída:
            float: Perda de carga localizada (em m de coluna de fluido).
        """
        return coeficiente_perda * (velocidade**2) / (2 * gravidade)

    def calcular_numero_reynolds(self, densidade: float, velocidade: float, diametro: float, viscosidade_dinamica: float) -> float:
        """Calcula o número de Reynolds.

        Entrada:
            densidade (float): Densidade do fluido (em kg/m³).
            velocidade (float): Velocidade média do fluido (em m/s).
            diametro (float): Diâmetro característico do escoamento (em m).
            viscosidade_dinamica (float): Viscosidade dinâmica do fluido (em Pa.s).

        Saída:
            float: Número de Reynolds (adimensional). Retorna None se a viscosidade dinâmica for zero.
        """
        if viscosidade_dinamica == 0:
            return None
        return (densidade * velocidade * diametro) / viscosidade_dinamica

    def calcular_numero_reynolds_alternativo(self, velocidade: float, diametro: float, viscosidade_cinematica: float) -> float:
        """Calcula o número de Reynolds usando a viscosidade cinemática.

        Entrada:
            velocidade (float): Velocidade média do fluido (em m/s).
            diametro (float): Diâmetro característico do escoamento (em m).
            viscosidade_cinematica (float): Viscosidade cinemática do fluido (em m²/s).

        Saída:
            float: Número de Reynolds (adimensional). Retorna None se a viscosidade cinemática for zero.
        """
        if viscosidade_cinematica == 0:
            return None
        return (velocidade * diametro) / viscosidade_cinematica

# Exemplo de uso (pode ser integrado ao seu menu):
if __name__ == "__main__":
    dinamica = DinamicaFluidos()

    # Vazão volumétrica
    area = 0.05  # m²
    velocidade = 2  # m/s
    vazao_v = dinamica.calcular_vazao_volumetrica(area, velocidade)
    print(f"Vazão Volumétrica: {vazao_v} m³/s")

    # Vazão mássica
    densidade = 1000  # kg/m³
    vazao_m = dinamica.calcular_vazao_massica(densidade, vazao_v)
    print(f"Vazão Mássica: {vazao_m} kg/s")

    # Equação da continuidade (incompressível)
    area1 = 0.1  # m²
    vel1 = 1  # m/s
    area2 = 0.05  # m²
    vel2 = dinamica.aplicar_equacao_continuidade_incompressivel(area1, vel1, area2)
    print(f"Velocidade na seção 2 (incompressível): {vel2} m/s")

    # Perda de carga distribuída
    fator_atrito = 0.02
    comprimento = 100  # m
    diametro = 0.1  # m
    velocidade_escoamento = 2  # m/s
    perda_distribuida = dinamica.calcular_perda_carga_distribuida(fator_atrito, comprimento, diametro, velocidade_escoamento)
    print(f"Perda de Carga Distribuída: {perda_distribuida:.2f} m")

    # Número de Reynolds
    viscosidade_dinamica = 1e-3  # Pa.s
    reynolds = dinamica.calcular_numero_reynolds(densidade, velocidade_escoamento, diametro, viscosidade_dinamica)
    print(f"Número de Reynolds: {reynolds:.2f}")