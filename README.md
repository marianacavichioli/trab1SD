# Primeiro trabalho da disciplina de Sistemas Distribuídos

Este trabalho tem o objetivo de desenvolver um sistema em python que implemente uma espaço de dados compartilhado persistente, nos moldes do Linda Tuplespace (com as operações in, rd e out) que permita a implementação de um mini-blog com postagens de conteúdos por tópicos, sua leitura por tópicos e a retirada da mensagem somente por quem postou. Além disso, tem o objetivo de escrever um wrapper usando REST api neste sistema que permita a conexão de clientes remotos a este microblog se conectarem  através de REST. 

## Instruções

### Host e porta
- Ajuste devidamente o endereço e a porta em `host_port.py`
- Certifique-se de que servidor e cliente estarão usando as mesmas portas.

### Execução
Para executar o projeto você deve clonar o repositório e executar os seguintes comandos:
```sh
$ cd trab1SD
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
#### No lado do servidor
```sh
$ python server.py
```
#### No lado do cliente
```sh
$ python example.py
```

### Testando a API
Para testar a API é necessário utilizar um software de teste, como o [Insomnia REST Client](https://insomnia.rest/).
```sh
$ python server.py
$ python app.py
```

----------------------------------------------------------------------
**Mariana Cavichioli Silva - 726568**

**Rafael Bastos Saito - 726580**
