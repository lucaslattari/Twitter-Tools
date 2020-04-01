# Twitter-Tools

O propósito desse repositório é disponibilizar uma série de scripts que automatizam tarefas relacionadas ao Twitter. Até o momento, tem-se scripts que:
* Realizam o bloqueio de contas que possuem comportamento de bot a partir de algum critério de busca, como suas mentions (block.py)
* Excluem tuítes antigos segundo uma data firmada pelo próprio usuário (delete.py).
* Fazem o download dos tuítes de um usuário (download.py)
* Buscam os tuítes segundo algum critério de busca (search_log.py)

## Primeiros Passos

### Pré-requisitos

Para usar o referido código, se faz necessário ter as chaves de desenvolvimento para a API do Twitter. Para isso, você precisa de:
1. Ter uma conta no Twitter ¯\\_(ツ)_/¯

2. Acessar o site https://developer.twitter.com/en e aplicar para o desenvolvimento de um app. Para tal, você precisa estar logado na sua conta.
![Tela principal do site de desenvolvedores do Twitter](https://files.realpython.com/media/dev_account_01.2a5eab8edcb8.png)

3. A seguir, você deve preencher alguns formulários explicando porque motivo você quer desenvolver aplicativos usando a API do Twitter. Eu notei que, de maneira geral, eles gostam de bastante informação. Ser bem detalhado no inglês e ser sincero sobre os usos me ajudou bastante. Da última vez que preenchi de qualquer jeito eles acabaram rejeitando. Se rejeitarem, você não pode mais solicitar usando a mesma conta. Nesse caso, você precisa criar uma nova conta.
![Formulários em que você deve detalhar as informações sobre sua conta e, posteriormente, sobre seu projeto](https://files.realpython.com/media/dev_account_02.f6f23b384b33.png)

4. Sendo bem sucedido ao criar sua aplicação, você deve entrar em 'details' de sua aplicação.
![Tela que apresenta suas aplicações no Twitter](https://files.realpython.com/media/dev_account_06.fcb9c3b19939.png)

5. Ao selecionar 'Keys and tokens', você pode gerar as quatro chaves (API key, API secret, Access Token e Access Token Secret) que serão necessárias para o bom funcionamento dos scripts desse repositório.
![Tela contendo as chaves necessárias para o uso de aplicações que envolvem a API do Twitter](https://files.realpython.com/media/dev_account_07.f37afa5ab26a.efd2422a33c8.png)

6. Supondo que você deseja utilizar a aplicação que remove os tweets antigos (delete.py), ao abrir o terminal de comandos e acessar a pasta em que os códigos se encontram, você deve informar as chaves de desenvolvimento, enquanto os tokens são opcionais. Veja os exemplos abaixo:

Possibilidade 1: Informar tanto as chaves de desenvolvimento quanto os tokens.

```
python delete.py [CHAVE_CONSUMIDORA] [CHAVE_SECRETA] -tk [CHAVE_TOKEN] -ts [CHAVE_SECRETA_TOKEN] --TWEETS
```

OBS: Obviamente você deve trocar os parâmetros pelas chaves geradas no passo 5 =)

![Tela mostrando um exemplo da execução do Twitter Tools (delete.py)](https://universodiscreto.com/images/exemplo1_twitter_tools.png)

Possibilidade 2: Informar apenas as chaves de desenvolvimento.

```
python delete.py [CHAVE_CONSUMIDORA] [CHAVE_SECRETA] --TWEETS
```

Nesse caso, abre-se uma janela do navegador autorizando o uso da aplicação pela plataforma do Twitter.

![Tela do prompt com a operação realizada](https://universodiscreto.com/images/exemplo2_twitter_tools.png)

![Tela do navegador solicitando a autorização do usuário.](https://universodiscreto.com/images/exemplo3_twitter_tools.png)

Após autorizar, você deve anotar o código e informar na aplicação em execução.

![Tela com o código a ser anotado.](https://universodiscreto.com/images/exemplo4_twitter_tools.png)

![Após a inserção do código.](https://universodiscreto.com/images/exemplo5_twitter_tools.png)

Finalmente, agora você pode usar qualquer um dos utilitários desse repositório!

### Instalação

1. No terminal, acesse alguma pasta e digite o comando 'git clone https://github.com/lucaslattari/Twitter-Tools.git'

2. Na pasta do projeto, insira o comando 'pip install -r requirements.txt'

3. Faça bom uso =)

## Utilitários disponíveis

### block.py

Esse script eu fiz baseado numa sugestão que o Atila Iamarino postou no Twitter. Ele perguntou se existia alguma ferramenta que varria as respostas de um tweet e bloqueava contas com perfil de bot. Basicamente esse script analisa as mentions de um usuário e sempre que uma conta bot fez esse reply (segundo os critérios do botometer), ela é sumariamente bloqueada. Seus parâmetros estão descritos no print abaixo.

![Parâmetros de block.py.](https://universodiscreto.com/images/block.png)

Para usar esse programa, no mínimo, devem ser informadas as chaves da API do Twitter (consumer key e consumer secret) além da [chave do Botometer da RAPID API](https://rapidapi.com/OSoMe/api/botometer). Quem verifica se as contas são bots ou não é o pacote [botometer](https://botometer.iuni.iu.edu/), e no site da Rapid API você obtém a chave deles. Outro parâmetro obrigatório é o username da conta de Twitter que se recuperarão as mentions.

Vamos supor que eu queira bloquear contas bots que mencionaram @oatila.

```
python block.py [CHAVE_CONSUMIDORA] [CHAVE_SECRETA] [CHAVE_RAPID_API] oatila 
```

Lembrando que você também pode informar os tokens, caso não queira se logar manualmente pelo site do Twitter.

```
python block.py [CHAVE_CONSUMIDORA] [CHAVE_SECRETA] [CHAVE_RAPID_API] oatila -tk [CHAVE_TOKEN] -ts [CHAVE_SECRETA_TOKEN]
```

Outros parâmetros importantes são: o arquivo de log contendo um relatório dos bloqueios realizados (-f) e o limiar de bot (-b). 

O arquivo de log é salvo em formato JSON.

O limiar de bot define qual o nível de tolerância que você terá ao fazer os bloqueios baseado no botometer. O botometer dá notas de 0 a 5 para os perfis, de forma que o mais próximo de 0 é um perfil controlado por humano e 5 é administrado por um algoritmo. Você pode definir sua nota. No exemplo abaixo define-se que uma pontuação acima de 2,5 já é suficiente pra bloquear uma conta.

```
python block.py [CHAVE_CONSUMIDORA] [CHAVE_SECRETA] [CHAVE_RAPID_API] oatila -tk [CHAVE_TOKEN] -ts [CHAVE_SECRETA_TOKEN] -f block.json -b 2.5
```

### delete.py

Esse script é uma modificação em cima de outro criado em repositório antigo meu, cujo objetivo é deletar tweets antigos com maior facilidade. Seus parâmetros estão descritos no print abaixo:

![Parâmetros de delete.py.](https://universodiscreto.com/images/delete.png)

Para usar esse programa, no mínimo, devem ser informadas as chaves da API do Twitter (consumer key e consumer secret) e se você deseja remover apenas tweets (--TWEETS), curtidas (--LIKES) ou ambos (--TWEETS_AND_LIKES).

Outro parâmetro opcional importante é: até quantos dias você deseja manter os tweets ou likes (-d). Se você, por exemplo, informar '-d 7', isso faz que os tweets (e/ou likes) mais antigos do que uma semana sejam excluídos da plataforma.

Por fim, além dos tokens já explicados acima, você também pode gravar um relatório em formato JSON com os tweets deletados por meio do parâmetro -f.

Veja o exemplo abaixo, em que tweets e curtidas de um ano atrás são removidos.

```
python delete.py [CHAVE_CONSUMIDORA] [CHAVE_SECRETA] --TWEETS_AND_LIKES -tk [CHAVE_TOKEN] -ts [CHAVE_SECRETA_TOKEN] -f delete.json -d 365
```

### download.py

Esse script tem como objetivo fazer downloads de seus tweets. Seus parâmetros estão descritos no print abaixo:

![Parâmetros de download.py.](https://universodiscreto.com/images/download.png)

Para usar esse programa, no mínimo, devem ser informadas as chaves da API do Twitter (consumer key e consumer secret).

Outro parâmetro opcional importante é: qual o nome do arquivo de relatório em formato JSON com os tweets da sua timeline, por meio do parâmetro -f.

Veja o exemplo abaixo.

```
python download.py [CHAVE_CONSUMIDORA] [CHAVE_SECRETA] -tk [CHAVE_TOKEN] -ts [CHAVE_SECRETA_TOKEN] -f tweets.json
```

### search_log.py

Esse script tem como objetivo buscar os tweets de acordo com um determinado critério de busca e salvá-los em disco. Seus parâmetros estão descritos no print abaixo:

![Parâmetros de search_log.py.](https://universodiscreto.com/images/search_log.png)

Para usar esse programa, no mínimo, devem ser informadas as chaves da API do Twitter (consumer key e consumer secret) e o termo a ser buscado.

Outro parâmetro opcional importante é: qual o nome do arquivo de relatório em formato JSON com os tweets retornados a partir da busca, por meio do parâmetro -f.

Veja o exemplo abaixo.

```
python search_log.py [CHAVE_CONSUMIDORA] [CHAVE_SECRETA] termo_buscado -tk [CHAVE_TOKEN] -ts [CHAVE_SECRETA_TOKEN] -f log.json
```

## Desenvolvido com

* [Tweepy](https://www.tweepy.org/) - Interface amigável pra usar a API do Twitter
* [Botometer](https://botometer.iuni.iu.edu/#!/) - Biblioteca útil para identificar bots do Twitter

## Contribuindo

Sinta-se a vontade para forkar, propor correções ou fazer modificações de código a fim de estender as funcionalidades desse repositório.

## Autor

* **Lucas Lattari** - [lucaslattari](https://github.com/lucaslattari)

## Agradecimentos

* Minha esposa [biaportes](https://github.com/biaportes) pela paciência de me ver programando por tanto tempo e não me trucidar.

## Referências 

* [Python Real - Bot de Twitter](https://realpython.com/twitter-bot-python-tweepy/)
