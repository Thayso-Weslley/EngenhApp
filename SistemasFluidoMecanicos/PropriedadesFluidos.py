class PropriedadesFluidos:
    def calcular_densidade(self, massa: float, volume: float) -> float:

        if volume == 0:
            raise ValueError("O volume não pode ser zero.")
        return massa / volume

    def calcular_peso_especifico(self, densidade: float, gravidade: float = 9.81) -> float:
        return densidade * gravidade

    def calcular_viscosidade_cinematica(self, viscosidade_dinamica: float, densidade: float) -> float:
        if densidade == 0:
            raise ValueError("A densidade não pode ser zero.")
        return viscosidade_dinamica / densidade

    def obter_compressibilidade(self):
        """Função placeholder para obter a compressibilidade de um fluido.

        A compressibilidade pode depender de fatores como pressão e temperatura,
        e geralmente requer tabelas ou modelos mais complexos.
        Esta função pode ser expandida no futuro para incluir esses dados
        ou solicitar informações adicionais do usuário.

        Returns:
            str: Uma mensagem indicando que a funcionalidade de compressibilidade
                 pode ser mais complexa.
        """
        return "O cálculo preciso da compressibilidade depende de informações adicionais " \
        "(pressão, temperatura, tipo de fluido) e pode envolver modelos ou tabelas específicas."

    def calcular_tensao_superficial(self, forca: float, comprimento: float) -> float:
        """Calcula a tensão superficial de um líquido.

        Args:
            forca (float): Força atuando na superfície (em N).
            comprimento (float): Comprimento da linha onde a força atua (em m).S

        Returns:
            float: Tensão superficial do líquido (em N/m).
        """
        if comprimento == 0:
            raise ValueError("O comprimento não pode ser zero.")
        return forca / comprimento

# Exemplo de uso:
if __name__ == "__main__":
    propriedades = PropriedadesFluidos()

    # Calcular densidade
    massa = 10.0  # kg
    volume = 2.0  # m³
    densidade = propriedades.calcular_densidade(massa, volume)
    print(f"Densidade: {densidade} kg/m³")

    # Calcular peso específico
    peso_especifico = propriedades.calcular_peso_especifico(densidade)
    print(f"Peso Específico: {peso_especifico} N/m³")

    # Calcular viscosidade cinemática
    viscosidade_dinamica = 0.001  # Pa.s (água a 20°C)
    viscosidade_cinematica = propriedades.calcular_viscosidade_cinematica(viscosidade_dinamica, densidade)
    print(f"Viscosidade Cinemática: {viscosidade_cinematica} m²/s")

    # Obter compressibilidade
    compressibilidade_info = propriedades.obter_compressibilidade()
    print(f"Compressibilidade: {compressibilidade_info}")

    # Calcular tensão superficial
    forca_tensao = 0.0728  # N (água a 20°C, valor aproximado)
    comprimento_tensao = 0.1  # m
    tensao_superficial = propriedades.calcular_tensao_superficial(forca_tensao, comprimento_tensao)
    print(f"Tensão Superficial: {tensao_superficial} N/m")