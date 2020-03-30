# Twitter-Tools

O propósito desse repositório é disponibilizar uma série de scripts que automatizam tarefas relacionadas ao Twitter. Até o momento, tem-se scripts que:
* Realizam o bloqueio de contas que possuem comportamento de bot a partir de algum critério de busca, como suas mentions (block.py)
* Excluem tuítes antigos segundo uma data firmada pelo próprio usuário (delete.py).
* Fazem o download dos tuítes de um usuário (download.py)
* Buscam os tuítes segundo algum critério de busca (search_log.py)

## Getting Started

### Prerequisites

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

```
Supondo que você deseja utilizar a aplicação que remove os tweets antigos (delete.py), ao abrir o terminal de comandos e acessar a pasta em que os códigos se encontram, você
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Agradecimentos

* Hat tip to anyone whose code was used
* Inspiration
* etc

##Referências [Python Real - Bot de Twitter](https://realpython.com/twitter-bot-python-tweepy/)
