
# Hello Opencv

***************
Esse é um programa inicial de opencv 4.0 do livro Opencv 4 with Python.

Inicialmente serve para padronizar a estrutura de um projeto em opencv. Desta maneira você pode organizar todos os arquivos.

Cada Arquivo adicionado serve como exemplo de projeto:
```
sampleproject/
|
|---- .gitignore
|---- sampleproject.py
|---- LICENSE
|---- README.md
|---- requirements.txt
|---- setup.py
|---- tests.py
```
 ##### _.gitignore_
 > O arquivo especifica arquivos não rastreados intencionalmente que o Git deve ignorar
 
 ##### _README.md_ 
 > Usado para registrar as principais propriedades do projedo
 
    * O que seu projeto faz
    * Como instar
    * Exemplo de uso
    * Como configurar o ambiente de desenvolvimento
    * Como enviar uma mudança
    * Log de alterações
    * Licença e informações do autor

##### _sampleproject.py_
> Arquivo contém o código fonte do projeto. é a parte principal do programa.

##### _LICENCE_ 
> Documento contém a licença aplicável. Esta é sem dúvida a parte mais importante do seu repositório, além do próprio código-fonte.

##### _requirements.txt_ 
> Arquivo de requisitos de pip. deve ser colocado na raiz do repositório, que é usado para especificar as dependências necessárias para contribuir com o projeto. O arquivo pode ser gerado usando o comando a seguir:
```
$ pip freeze > requirements.txt
```

##### _setup.py_
> Arquivo permite criar pacotes que podem ser redistribuir. esse script serve para instalar seu pacote no sistema do usuário final.
Portanto, se quisermos instalar este pacote simples, podemos escrever o comando:
```sh
$ python setup.py install
```
##### _test.py_
> O scrip contém os testes da aplicação.

***************
## Instalação
Não precisa ser instalado. serve como um modelo para um projeto opencv. O ideal é começar um projeto em opencv, clonando este. 

```sh
 $ git clone https://github.com/lucasmcast/hello_opencv.git
```
## Meta
- _Lucas Martins de Castro_

- _lucas.martins.c03@gmail.com_

