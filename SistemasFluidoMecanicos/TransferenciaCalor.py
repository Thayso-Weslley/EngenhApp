import math

class TransferenciaCalor:
    def calcular_conducao_calor(self, condutividade_termica: float, area: float, delta_temperatura: float, espessura: float) -> float:
        """Calcula a taxa de transferência de calor por condução (Lei de Fourier).

        Entrada:
            condutividade_termica (float): Condutividade térmica do material (em W/(m.K)).
            area (float): Área da seção transversal através da qual o calor é transferido (em m²).
            delta_temperatura (float): Diferença de temperatura entre as duas faces (em K ou °C).
            espessura (float): Espessura do material na direção da transferência de calor (em m).

        Saída:
            float: Taxa de transferência de calor por condução (em W). Retorna None se a espessura for zero.
        """
        if espessura == 0:
            return None
        return (condutividade_termica * area * delta_temperatura) / espessura

    def calcular_conveccao_calor(self, coeficiente_conveccao: float, area: float, temperatura_superficie: float, temperatura_fluido: float) -> float:
        """Calcula a taxa de transferência de calor por convecção (Lei de Newton do resfriamento).

        Entrada:
            coeficiente_conveccao (float): Coeficiente de convecção (em W/(m².K)).
            area (float): Área da superfície onde ocorre a convecção (em m²).
            temperatura_superficie (float): Temperatura da superfície (em K ou °C).
            temperatura_fluido (float): Temperatura do fluido (em K ou °C).

        Saída:
            float: Taxa de transferência de calor por convecção (em W).
        """
        return coeficiente_conveccao * area * (temperatura_superficie - temperatura_fluido)

    def calcular_radiacao_calor(self, emissividade: float, area: float, temperatura_superficie: float, temperatura_ambiente: float,
                                 constante_Stefan_Boltzmann: float = 5.67e-8) -> float:
        """Calcula a taxa de transferência de calor por radiação (Lei de Stefan-Boltzmann).

        Assume troca de calor com um ambiente muito maior.

        Entrada:
            emissividade (float): Emissividade da superfície (adimensional, 0 a 1).
            area (float): Área da superfície que emite radiação (em m²).
            temperatura_superficie (float): Temperatura da superfície (em K).
            temperatura_ambiente (float): Temperatura do ambiente (em K).
            constante_Stefan_Boltzmann (float, optional): Constante de Stefan-Boltzmann (em W/(m².K⁴)). Padrão é 5.67e-8.

        Saída:
            float: Taxa de transferência de calor por radiação (em W).
        """
        return emissividade * area * constante_Stefan_Boltzmann * (temperatura_superficie**4 - temperatura_ambiente**4)

    def calcular_trocador_calor_logaritmica(self, temperatura_entrada_quente: float, temperatura_saida_quente: float,
                                            temperatura_entrada_frio: float, temperatura_saida_frio: float) -> float:
        """Calcula a diferença de temperatura média logarítmica (DTML) para um trocador de calor.

        Assume escoamento em paralelo ou contra-corrente.
        Se as diferenças de temperatura forem iguais, retorna essa diferença.

        Entrada:
            temperatura_entrada_quente (float): Temperatura do fluido quente na entrada (em K ou °C).
            temperatura_saida_quente (float): Temperatura do fluido quente na saída (em K ou °C).
            temperatura_entrada_frio (float): Temperatura do fluido frio na entrada (em K ou °C).
            temperatura_saida_frio (float): Temperatura do fluido frio na saída (em K ou °C).

        Saída:
            float: Diferença de temperatura média logarítmica (em K ou °C).
        """
        delta_t1 = temperatura_entrada_quente - temperatura_saida_frio
        delta_t2 = temperatura_saida_quente - temperatura_entrada_frio

        if delta_t1 == delta_t2:
            return delta_t1  # Evita divisão por zero

        return (delta_t1 - delta_t2) / math.log(delta_t1 / delta_t2)

# Exemplo de uso (pode ser integrado ao seu menu):
if __name__ == "__main__":
    transferencia = TransferenciaCalor()

    # Condução
    k = 200  # W/(m.K) (exemplo: alumínio)
    A = 0.1  # m²
    dT = 50  # K
    esp = 0.01  # m
    conducao = transferencia.calcular_conducao_calor(k, A, dT, esp)
    print(f"Condução: {conducao:.2f} W")

    # Convecção
    h = 10  # W/(m².K) (exemplo: ar)
    Area = 0.2  # m²
    T_sup = 100  # °C
    T_fluido = 25  # °C
    conveccao = transferencia.calcular_conveccao_calor(h, Area, T_sup, T_fluido)
    print(f"Convecção: {conveccao:.2f} W")

    # Radiação
    emissividade = 0.8
    area_rad = 0.05
    T_superficie = 400 + 273.15  # K
    T_ambiente = 25 + 273.15  # K
    radiacao = transferencia.calcular_radiacao_calor(emissividade, area_rad, T_superficie, T_ambiente)
    print(f"Radiação: {radiacao:.2f} W")

    # Trocador de calor
    T_quente_in = 150
    T_quente_out = 100
    T_frio_in = 30
    T_frio_out = 80
    DTML = transferencia.calcular_trocador_calor_logaritmica(T_quente_in, T_quente_out, T_frio_in, T_frio_out)
    print(f"DTML: {DTML:.2f} °C")