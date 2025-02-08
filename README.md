# BackupThis

Este script Python, `backup_app.py`, é uma aplicação de interface gráfica (GUI) desenvolvida com `tkinter` para facilitar a criação de backups de pastas no sistema Ubuntu. Com uma interface amigável, o Backup Manager Pro permite que você configure e execute tarefas de backup de forma simples e eficiente.

## Funcionalidades

*   **Interface Gráfica Intuitiva:** Desenvolvida com `tkinter`, oferece uma experiência de usuário amigável e fácil de usar.
*   **Gerenciamento de Tarefas de Backup:** Permite criar múltiplas tarefas de backup, cada uma com sua própria configuração de origem e destino.
*   **Seleção de Pastas:** Facilidade na escolha das pastas de origem e destino através de um diálogo de seleção de diretórios.
*   **Progresso em Tempo Real:** Barra de progresso visual para acompanhar o andamento de cada tarefa de backup.
*   **Controle Flexível:** Opções para iniciar, pausar e cancelar as tarefas de backup a qualquer momento.
*   **Menu e Barra de Ferramentas:** Menu principal com opções de 'Arquivo' (Nova Tarefa, Salvar Configurações, Sair) e 'Ajuda' (Sobre), além de uma barra de ferramentas com botões de acesso rápido para as principais ações.
*   **Status da Operação:** Barra de status informativa que exibe mensagens sobre o estado atual do aplicativo e das tarefas de backup.

## Pré-requisitos

Antes de executar o `backup_app.py`, certifique-se de ter o seguinte instalado no seu sistema Ubuntu:

*   **Python 3:**  Ubuntu geralmente já vem com Python 3 instalado por padrão. Você pode verificar a versão instalada abrindo o terminal e executando:
    ```bash
    python3 --version
    ```
    Se o Python 3 não estiver instalado, você pode instalá-lo com:
    ```bash
    sudo apt update
    sudo apt install python3
    ```
*   **tkinter:** A biblioteca `tkinter` é necessária para a interface gráfica. Caso não esteja instalada, você pode instalá-la com:
    ```bash
    sudo apt install python3-tk
    ```

## Como Executar no Ubuntu

Siga estes passos para executar o `backup_app.py` no Ubuntu:

1.  **Salve o arquivo `backup_app.py`:** Certifique-se de ter o código do script salvo em um arquivo com o nome `backup_app.py` em um diretório de sua escolha no seu sistema Ubuntu.

2.  **Abra o Terminal:** Abra o terminal do Ubuntu. Você pode fazer isso pressionando `Ctrl+Alt+T` ou procurando por "Terminal" no menu de aplicativos.

3.  **Navegue até o diretório do script:** Utilize o comando `cd` para navegar até o diretório onde você salvou o arquivo `backup_app.py`. Por exemplo, se você salvou o arquivo na pasta `Documentos`, o comando seria:
    ```bash
    cd Documentos
    ```

4.  **Execute o script:** Para executar o script Python, utilize o comando `python3` seguido do nome do arquivo:
    ```bash
    python3 backup_app.py
    ```

    Após executar este comando, a interface gráfica do "Backup Manager Pro" deverá abrir, e você poderá começar a configurar e executar suas tarefas de backup.

## Utilização

Após executar o script, a janela principal do "Backup Manager Pro" será exibida. Para utilizar o aplicativo, siga as instruções abaixo:

1.  **Adicionar uma Tarefa de Backup:**
    *   Clique no botão "+ Tarefa" na barra de ferramentas ou selecione "Nova Tarefa" no menu "Arquivo".
    *   Uma nova aba com o nome "Nova Tarefa" será criada. Você pode criar múltiplas abas para diferentes tarefas de backup.

2.  **Configurar a Tarefa:**
    *   Na aba da tarefa, você verá campos para "Origem" e "Destino".
    *   **Origem:** Clique no botão "Procurar" ao lado do campo "Origem" para selecionar a pasta que você deseja fazer backup.
    *   **Destino:** Clique no botão "Procurar" ao lado do campo "Destino" para selecionar a pasta onde você deseja salvar o backup.

3.  **Iniciar o Backup:**
    *   Após configurar a origem e o destino, clique no botão "▶ Iniciar" na barra de ferramentas para começar o processo de backup da tarefa selecionada.
    *   A barra de progresso na aba da tarefa mostrará o andamento do backup, e a label de status exibirá mensagens informativas.

4.  **Pausar/Retomar o Backup:**
    *   Para pausar o backup durante a execução, clique no botão "⏸ Pausar". O botão mudará para "▶ Retomar".
    *   Para retomar um backup pausado, clique no botão "▶ Retomar".

5.  **Cancelar o Backup:**
    *   Se você precisar interromper o backup completamente, clique no botão "⏹ Cancelar".

6.  **Remover uma Tarefa de Backup:**
    *   Selecione a aba da tarefa que você deseja remover.
    *   Clique no botão "- Tarefa" na barra de ferramentas.

7.  **Menu Arquivo:**
    *   **Nova Tarefa:** Cria uma nova aba de tarefa de backup.
    *   **Salvar Configurações:**  *Funcionalidade em desenvolvimento.* Atualmente, esta opção exibe apenas uma mensagem informativa.
    *   **Sair:** Fecha o aplicativo "Backup Manager Pro".

8.  **Menu Ajuda:**
    *   **Sobre:** Exibe uma janela com informações sobre o "Backup Manager Pro", incluindo versão e desenvolvedor.

9.  **Barra de Status:**
    *   Localizada na parte inferior da janela, exibe mensagens de status sobre as ações que estão sendo realizadas no aplicativo.

## Notas

*   **Arquivos Existentes:** O script foi configurado para pular arquivos que já existem na pasta de destino, evitando a sobrescrita de arquivos.
*   **Cancelamento e Pausa:** As operações de backup podem ser pausadas e canceladas a qualquer momento, oferecendo flexibilidade durante o processo.
*   **Funcionalidade "Salvar Configurações":** A funcionalidade "Salvar Configurações" no menu "Arquivo" está atualmente em desenvolvimento e não possui funcionalidade implementada nesta versão.
*   **Versão:** Esta é a versão 2.2 do "Backup Manager Pro", desenvolvida especificamente para o sistema operacional Ubuntu.

Este `readme.md` fornece uma visão geral do script `backup_app.py` e instruções básicas para sua execução e utilização no Ubuntu. Para dúvidas ou sugestões, consulte a seção "Ajuda" no menu do aplicativo ou entre em contato com o desenvolvedor.
