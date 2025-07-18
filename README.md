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
