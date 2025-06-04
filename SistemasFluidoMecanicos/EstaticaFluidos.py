class EstaticaFluidos:
    def calcular_variacao_pressao_profundidade(self, densidade: float, delta_profundidade: float, gravidade: float = 9.81) -> float:
        """Calcula a variação da pressão em um fluido estático com a profundidade.

        Entrada:
            densidade (float): Densidade do fluido (em kg/m³).
            delta_profundidade (float): Diferença na profundidade (z1 - z2) (em m).
            gravidade (float, optional): Aceleração da gravidade (em m/s²). Padrão é 9.81.

        Saída:
            float: Variação da pressão (P2 - P1) (em Pa).
        """
        return densidade * gravidade * delta_profundidade

    def calcular_forca_hidrostatica_plana(self, pressao_centroide: float, area: float) -> float:
        """Calcula a força hidrostática resultante em uma superfície plana submersa.

        Entrada:
            pressao_centroide (float): Pressão no centroide da área (em Pa).
            area (float): Área da superfície (em m²).

        Saída:
            float: Força hidrostática resultante (em N).
        """
        return pressao_centroide * area

    def calcular_centro_pressao_superficie_plana(self, y_centroide: float, momento_inercia_xcg: float, area: float) -> float:
        """Calcula a coordenada y do centro de pressão em uma superfície plana submersa.

        O eixo x passa pelo centroide da área. O eixo y é na direção da profundidade.

        Entrada:
            y_centroide (float): Coordenada y do centroide da área (em m).
            momento_inercia_xcg (float): Momento de inércia da área em relação ao eixo x que passa pelo centroide (em m⁴).
            area (float): Área da superfície (em m²).

        Saída:
            float: Coordenada y do centro de pressão (em m).
        """
        if area == 0:
            raise ValueError("A área não pode ser zero.")
        return y_centroide + (momento_inercia_xcg / (y_centroide * area))

    def calcular_forca_hidrostatica_curva_horizontal(self, pressao_centroide_projecao_vertical: float, area_projecao_vertical: float) -> float:
        """Calcula a componente horizontal da força hidrostática em uma superfície curva submersa.

        Entrada:
            pressao_centroide_projecao_vertical (float): Pressão no centroide da projeção vertical da área (em Pa).
            area_projecao_vertical (float): Área da projeção vertical da superfície (em m²).

        Saída:
            float: Componente horizontal da força hidrostática (em N).
        """
        return pressao_centroide_projecao_vertical * area_projecao_vertical

    def calcular_forca_hidrostatica_curva_vertical(self, peso_volume_fluido_acima: float) -> float:
        """Calcula a componente vertical da força hidrostática em uma superfície curva submersa.

        Entrada:
            peso_volume_fluido_acima (float): Peso do volume de fluido diretamente acima da superfície curva (em N).

        Saída:
            float: Componente vertical da força hidrostática (em N).
        """
        return peso_volume_fluido_acima

# Exemplo de uso:
if __name__ == "__main__":
    estatica = EstaticaFluidos()

    # Variação da pressão com a profundidade
    densidade_agua = 1000  # kg/m³
    delta_z = 5  # m
    delta_pressao = estatica.calcular_variacao_pressao_profundidade(densidade_agua, delta_z)
    print(f"Variação da pressão com 5m de profundidade: {delta_pressao:.2f} Pa")

    # Força hidrostática em superfície plana
    pressao_cg = 10000  # Pa
    area_plana = 2  # m²
    forca_plana = estatica.calcular_forca_hidrostatica_plana(pressao_cg, area_plana)
    print(f"Força hidrostática em superfície plana: {forca_plana:.2f} N")

    # Centro de pressão em superfície plana (exemplo de um retângulo vertical)
    y_cg_retangulo = 2  # m
    largura_retangulo = 1  # m
    altura_retangulo = 4  # m
    area_retangulo = largura_retangulo * altura_retangulo
    I_xcg_retangulo = (largura_retangulo * (altura_retangulo**3)) / 12
    y_cp_retangulo = estatica.calcular_centro_pressao_superficie_plana(y_cg_retangulo, I_xcg_retangulo, area_retangulo)
    print(f"Coordenada y do centro de pressão (retângulo): {y_cp_retangulo:.2f} m")

    # Força hidrostática em superfície curva (componente horizontal - exemplo)
    pressao_cg_vertical = 15000  # Pa
    area_vertical = 1.5  # m²
    forca_horizontal_curva = estatica.calcular_forca_hidrostatica_curva_horizontal(pressao_cg_vertical, area_vertical)
    print(f"Componente horizontal da força em superfície curva: {forca_horizontal_curva:.2f} N")

    # Força hidrostática em superfície curva (componente vertical - exemplo)
    peso_volume_acima = 5000  # N
    forca_vertical_curva = estatica.calcular_forca_hidrostatica_curva_vertical(peso_volume_acima)
    print(f"Componente vertical da força em superfície curva: {forca_vertical_curva:.2f} N")