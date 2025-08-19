==============================================
Atividade Prática: Criptografia Assimétrica com RSA
==============================================

Este projeto é uma implementação de um sistema de criptografia assimétrica utilizando o algoritmo RSA em Python. A aplicação permite gerar um par de chaves (pública e privada), encriptar mensagens para um destinatário e decriptar mensagens recebidas, tudo através de um menu interativo no terminal.

Este trabalho foi desenvolvido para a disciplina de Segurança de Sistemas, demonstrando os conceitos fundamentais da criptografia de chave pública.


--------------------
FUNCIONALIDADES
--------------------

O script `atividade_completa.py` oferece as seguintes opções:

1. Gerar Novas Chaves: Cria um novo par de chaves RSA de 2048 bits (`chave_privada.pem` e `chave_publica.pem`). Atenção: Esta ação sobrescreve as chaves existentes.

2. Encriptar Mensagem: Criptografa uma mensagem digitada pelo usuário utilizando uma chave pública. O resultado é exibido em formato Base64, pronto para ser compartilhado.

3. Decriptar Mensagem: Decriptografa uma mensagem em Base64 utilizando a `chave_privada.pem` local.

4. Mostrar Minha Chave Pública: Exibe o conteúdo da sua chave pública (`chave_publica.pem`), que pode ser compartilhada com outras pessoas para que elas possam lhe enviar mensagens seguras.

5. Sair: Encerra o programa.


--------------------
PRÉ-REQUISITOS
--------------------

- Python 3.6 ou superior


--------------------
INSTALAÇÃO
--------------------

Antes de rodar o programa, é necessário instalar a biblioteca `cryptography`. Abra seu terminal ou prompt de comando e execute:

   pip install cryptography


--------------------
COMO EXECUTAR
--------------------

1. Navegue pelo terminal até o diretório onde você salvou o arquivo `atividade_completa.py`.

2. Execute o seguinte comando:

   python atividade_completa.py

3. O menu interativo será exibido, e na primeira execução, os arquivos `chave_privada.pem` e `chave_publica.pem` serão gerados automaticamente.


--------------------
EXEMPLO DE USO (AUTOTESTE)
--------------------

Para verificar o funcionamento completo do ciclo de criptografia:

1. Execute o programa. As chaves serão geradas se não existirem.

2. Escolha a opção 2 (Encriptar Mensagem).
   - Quando perguntado pelo caminho da chave pública, apenas pressione Enter para usar sua própria chave.
   - Digite uma mensagem, por exemplo: Testando o sistema RSA.
   - O programa exibirá o texto original, o texto encriptado em bytes e o resultado final em Base64.

3. Copie todo o texto em Base64 que foi gerado.

4. Volte ao menu principal e escolha a opção 3 (Decriptar Mensagem).

5. Cole o texto em Base64 que você copiou e pressione Enter duas vezes.

6. O programa exibirá o texto decriptado, que deve ser idêntico ao original: Testando o sistema RSA.


--------------------
COMO FUNCIONA A COMUNICAÇÃO COM OUTRA PESSOA
--------------------

1. Você (Receptor):
   - Execute o script. Suas chaves serão geradas.
   - Escolha a opção 4 para ver sua chave pública.
   - Copie e envie o conteúdo do arquivo `chave_publica.pem` para o seu colega.

2. Seu Colega (Remetente):
   - Ele deve salvar a sua chave pública em um arquivo (ex: `chave_do_colega.pem`).
   - Ele executa o script dele, escolhe a opção 2 e, quando solicitado, informa o caminho para o arquivo `chave_do_colega.pem`.
   - Ele digita a mensagem e envia o resultado em Base64 para você.

3. Você (Receptor):
   - Escolha a opção 3 no seu programa, cole a mensagem recebida e veja a mensagem original decifrada.