# 🌱 PhytoScan - Simulador de Crescimento de Raízes

**Prevenindo danos na construção civil através da simulação de crescimento radicular**

O PhytoScan surgiu durante meu tempo estacionando no ICC, onde observei vagas de estacionamento danificadas por raízes de árvores. Esta ferramenta simula o crescimento de raízes para ajudar engenheiros e arquitetos a prever e prevenir danos em estruturas urbanas.


## 🌍 Contexto do Problema
As raízes das árvores urbanas causam danos significativos à infraestrutura:
- Elevação de calçadas e pavimentos
- Danos a fundações de edifícios
- Rompimento de tubulações subterrâneas
- Destruição de vagas de estacionamento

O PhytoScan permite visualizar como as raízes podem crescer e interagir com obstáculos, ajudando no planejamento urbano sustentável.

## 🛠 Casos de Uso

### 1. Configurar Terreno Inicial
- **Descrição**: Usuário define um grid e posiciona manualmente raízes iniciais e obstáculos (estruturas de concreto, tubulações, etc.)
- **Fluxo Principal**:
  1. Usuário clica em células para alternar entre solo livre, raiz e obstáculo
  2. Sistema atualiza visualização em tempo real
  3. Usuário salva configuração para uso futuro

### 2. Simular Crescimento Radicular
- **Descrição**: Simula a expansão das raízes ao longo do tempo
- **Fluxo Principal**:
  1. Usuário clica em "Próximo Passo"
  2. Sistema expande raízes para células adjacentes livres
  3. Visualização é atualizada com novas raízes
  4. Sistema para automaticamente quando não há mais crescimento possível

### 3. Salvar/Carregar Cenários
- **Descrição**: Salva simulações para análise posterior
- **Fluxo Principal**:
  1. Usuário clica em "Salvar em JSON"
  2. Sistema serializa estado atual do terreno
  3. Usuário pode carregar cenário salvo posteriormente

## 📊 Diagrama de Classes

```plantuml
@startuml
skinparam classFontSize 14
skinparam classFontColor #000000

' Elementos Básicos
class TerrainElements {
  - x: int
  - y: int
  + get_position()
  + comportament()
  + type()
}

class FreeSoil {
  + comportament()
  + type()
}

class Root {
  + comportament()
  + type()
}

class Obstacle {
  + comportament()
  + type()
}

TerrainElements <|-- FreeSoil
TerrainElements <|-- Root
TerrainElements <|-- Obstacle

' Interface e Mixins
interface ITerrain {
  + get_root()
  + free_spaces(x, y)
  + add_root(x, y)
}

class SerializableMixin {
  + to_dict()
  + to_json(caminho)
}

' Componentes Principais
class Terrain {
  - width: int
  - height: int
  - grid: TerrainElements[][]
  - roots: Root[]
  + add_obstacle()
  + add_root()
  + free_spaces()
  + load_json()
}

class Simulator {
  - terrain: ITerrain
  - steps: int
  + step()
}

class Interface {
  - terrain: Terrain
  - sim: Simulator
  + toggle()
  + run_step()
  + refresh()
  + save()
  + load()
}

' Relacionamentos
ITerrain <|.. Terrain
SerializableMixin <|-- Terrain
Terrain *-- TerrainElements
Simulator --> ITerrain
Interface --> Terrain
Interface --> Simulator

note right of Terrain::load_json
  Carrega estado anterior
  de arquivo JSON
end note

note bottom of Simulator::step
  Expande raízes para
  células adjacentes livres
  de forma aleatória
end note
@enduml

## 📋 Diagrama de Casos de Uso

```mermaid
graph TD
    A[Usuário] --> B(Configurar Terreno Inicial)
    A --> C(Simular Crescimento Radicular)
    A --> D(Salvar Cenário)
    A --> E(Carregar Cenário)
    
    B --> B1[Adicionar Raiz]
    B --> B2[Adicionar Obstáculo]
    B --> B3[Limpar Célula]
    
    C --> C1[Executar Passo de Simulação]
    C --> C2[Visualizar Expansão]
    C --> C3[Identificar Bloqueios]
    
    D --> D1[Serializar para JSON]
    D --> D2[Armazenar Estado]
    
    E --> E1[Desserializar de JSON]
    E --> E2[Restaurar Estado]
    
    style A fill:#4CAF50,stroke:#388E3C,color:white
    style B fill:#2196F3,stroke:#0D47A1
    style C fill:#FF9800,stroke:#E65100
    style D fill:#9C27B0,stroke:#4A148C
    style E fill:#607D8B,stroke:#263238