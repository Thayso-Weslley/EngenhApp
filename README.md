# Projeto: Calculadora de Propriedades de Materiais e Sistemas Fluido-Mecânicos

## Descrição

Este projeto é uma aplicação em Python desenvolvida para auxiliar estudantes e professores de Engenharia e áreas afins no cálculo e consulta de propriedades de materiais, sistemas fluido-mecânicos e tabelas de materiais. O sistema possui uma interface de terminal interativa, organizada em menus, que permite realizar diversos cálculos, consultar propriedades e gerenciar uma base de dados de materiais.

Claro que o projeto está longe de ser perfeito. Há muita coisa que poderia ser enxugda e melhor implementada. Isso é algo que pretendo está corrigindo e aprimorando ao longo do tempo, mas por favor, sinta-se a vontade para entar colaborando também, pois não é um projeito exclusivamente meu, mas para os outros estudantes de engenharia e tecnologia também.

---

## Funcionalidades Principais

- **Menu Principal** com acesso a:
  - Ciência dos Materiais
  - Sistemas Fluido-Mecânicos
  - Tabela de Propriedade dos Materiais
  - Encerramento do programa

- **Ciência dos Materiais**
  - Difusão (cálculo de fluxo, coeficiente e distância de difusão)
  - Propriedades Elétricas (resistividade, condutividade, permeabilidade, força magnética)
  - Propriedades Mecânicas (tensão, deformação, módulo de Young, dureza, ductilidade, etc.)
  - Propriedades Térmicas (calor específico, capacidade calorífica, condutividade térmica, expansão térmica)
  - Transformador de Fase (fração de fases, temperatura de transformação, microestrutura prevista)

- **Sistemas Fluido-Mecânicos**
  - Bombas e Turbinas (altura manométrica, potência, eficiência)
  - Dinâmica dos Fluidos (vazão, perda de carga, número de Reynolds, etc.)
  - Estática dos Fluidos (forças hidrostáticas, centro de pressão)
  - Propriedades dos Fluidos (densidade, peso específico, viscosidade, compressibilidade, tensão superficial)
  - Transferência de Calor (condução, convecção, radiação, trocador de calor)

- **Tabela de Materiais**
  - Consultar materiais cadastrados e visualizar propriedades
  - Cadastrar novos materiais
  - Deletar materiais existentes

---

## Como Usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Execute o programa principal:**
   ```bash
   python main.py
   ```

3. **Navegue pelos menus** usando as opções apresentadas no terminal.

---

## Requisitos Funcionais

- O sistema deve validar entradas do usuário e impedir valores inválidos.
- O usuário pode retornar ao menu anterior em todos os submenus.
- Todos os resultados de cálculos são destacados em verde no terminal.
- O sistema permite encerrar o programa de forma segura pelo menu principal.

---

## Estrutura do Projeto

```
A3/
├── CienciaMateriais/
│   ├── Difusao.py
│   ├── PropriedadesEletricasMagneticas.py
│   ├── PropriedadesMecanicas.py
│   ├── PropriedadesTermicas.py
│   └── TransformadorDeFase.py
├── SistemasFluidoMecanicos/
│   ├── BombasTurbinas.py
│   ├── DinamicaFluidos.py
│   ├── EstaticaFluidos.py
│   ├── PropriedadesFluidos.py
│   └── TransferenciaCalor.py
├── TabelaMateriais/
│   ├── Cadastro.py
│   ├── materiais.json
│   └── TabelaPropriedades/
│       └── (arquivos .json de propriedades de materiais)
├── Estilo/
│   └── Cores.py
├── main.py
└── Apresentar.md
```
---

## Créditos

Desenvolvido por Thayso Weslley para apresentação na disciplina de Ciencia dos Materiais e Sistemas FLuidoMecânicos - UNIFG.

---

## Licença

Este projeto é livre para uso acadêmico e educacional.
