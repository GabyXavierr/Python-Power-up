# Automatização com PyAutoGUI: Automatizando Entrada de Dados 🚀

Este projeto demonstra como automatizar o processo de abrir um aplicativo web, fazer login e importar dados de um arquivo CSV para um sistema usando Python e a biblioteca PyAutoGUI. Ele é projetado para ser uma maneira simples e eficiente de economizar tempo e reduzir erros em tarefas repetitivas, como entrada de dados. 💻📊🎉

---

## Visão Geral do Projeto 📌

### Etapas Realizadas

1. **Abrir o Sistema**
   - Automatiza a abertura do Google Chrome e a navegação para uma página de login específica.

2. **Fazer Login**
   - Insere automaticamente as credenciais de login e acessa o aplicativo.

3. **Importar Dados**
   - Lê um arquivo CSV (`produtos.csv`) contendo informações sobre os produtos.

4. **Automatização de Entrada de Dados**
   - Faz um loop pelo arquivo CSV para inserir os dados de cada produto na interface do sistema.

---

## Pré-Requisitos 🛠️

Antes de executar o script, certifique-se de que você tem o Python instalado junto com as bibliotecas necessárias.

### Passos para Instalação 🖥️

1. **Instalar o Python**
   - Baixe e instale o Python no site oficial: [python.org](https://www.python.org/). 🐍

2. **Instalar Bibliotecas Necessárias**
   - Use o `pip` para instalar as bibliotecas requeridas:

     ```bash
     pip install pyautogui pandas openpyxl
     ```

     - `pyautogui`: Usada para simular ações de teclado e mouse.
     - `pandas`: Usada para ler e manipular o arquivo CSV.
     - `openpyxl`: Necessária para o pandas manipular arquivos Excel (se necessário). 📊

---

## Como Usar o Script 📋

1. **Prepare os Dados**
   - Crie um arquivo CSV chamado `produtos.csv` com as seguintes colunas:
     - `codigo`: Código do produto.
     - `marca`: Marca do produto.
     - `tipo`: Tipo do produto.
     - `categoria`: Categoria do produto.
     - `preco_unitario`: Preço unitário do produto.
     - `custo`: Custo do produto.
     - `obs`: Observações adicionais (opcional).

2. **Ajuste as Coordenadas da Tela**
   - Atualize as coordenadas no script (`pyautogui.click(x=..., y=...)`) para corresponder ao layout da sua tela.
     - Use o seguinte comando para identificar as posições na tela:

       ```python
       import pyautogui
       pyautogui.displayMousePosition()
       ```

3. **Execute o Script**
   - Salve o script como `codigo.py` e execute-o no terminal:

     ```bash
     python codigo.py
     ```

4. **Automatização em Ação**
   - O script abrirá o sistema, fará login e inserirá sequencialmente os dados do arquivo CSV no aplicativo web.🖱️

---

## Observações Importantes ⚠️

- **Delays e Pausas**:
  - O script inclui `time.sleep()` e `pyautogui.PAUSE` para garantir que o sistema tenha tempo de carregar entre as ações.

- **Tratamento de Erros**:
  - Certifique-se de que o arquivo CSV esteja formatado corretamente e que todos os dados necessários estejam presentes para evitar erros.

- **Ajustes Específicos do Sistema**:
  - Dependendo do layout do sistema, pode ser necessário ajustar as coordenadas de cliques e sequências de tabulação. 

---

## Limitações❗

- Este script foi criado para tarefas específicas e pode precisar de modificações para outros sistemas.
- O uso do PyAutoGUI depende do layout da interface gráfica. Quaisquer mudanças na interface do sistema podem exigir atualizações no script.🛠️

---

## Aviso 📢

- O script presume que você tem permissão para automatizar tarefas no sistema que está acessando.
- Lide com informações sensíveis, como credenciais de login, de forma segura; evite inseri-las diretamente no código. 🔐

---

## Melhorias Futuras 💡

- Adicionar tratamento de exceções para lidar com erros inesperados durante a automação.
- Usar um método seguro para armazenar e recuperar credenciais de login.
- Melhorar a flexibilidade para se adaptar dinamicamente a diferentes resoluções de tela.

---

