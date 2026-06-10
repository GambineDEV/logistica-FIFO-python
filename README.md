# 📦 Sistema de Gestão de Expedição Logística

Um simulador de terminal desenvolvido em Python para gerenciar o fluxo de despacho de pacotes em docas de carregamento. O sistema foi desenhado para automatizar e organizar o histórico de saídas de galpões logísticos e distribuidoras.

## 🎯 O Problema Resolvido
Em operações logísticas de alto volume, manter o controle exato de qual pedido deve ser despachado primeiro é fundamental para evitar atrasos. Este projeto resolve isso aplicando a metodologia **FIFO (First In, First Out)**, garantindo que o lote mais antigo na fila de espera seja sempre o primeiro a ser direcionado para o transporte.

## 🚀 Funcionalidades

- **[1] Entrada de Estoque:** Cadastro de novos pacotes informando ID do Pedido, Cidade de Destino e Peso. Os itens são alocados automaticamente no final da fila.
- **[2] Doca de Despacho:** Remoção automatizada do pacote mais antigo da fila de espera (FIFO) e transferência para o histórico de pedidos despachados.
- **[3] Relatório Operacional:** Geração instantânea do balanço diário, exibindo a relação de pedidos que já saíram e os que ainda aguardam despacho.

## 🛠️ Tecnologias Utilizadas
- **Python 3:** Lógica principal, loops de repetição (`while True`), e controle de fluxo (`if/elif/else`).
- **Estruturas de Dados:** Uso intensivo de matrizes (listas de listas) para armazenar os pacotes e manipulação de índices com `.append()` e `.pop()`.

## 💻 Como executar o projeto

1. Clone este repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/SeuUsuario/sistema-gestao-expedicao.git](https://github.com/SeuUsuario/sistema-gestao-expedicao.git)