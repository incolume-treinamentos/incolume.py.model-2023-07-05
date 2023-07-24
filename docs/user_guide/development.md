# Guia de contribuíção (Desenvolvimento)

O desenvolvimento deste projeto segue algumas regras e convenções
básicas. Como _estilo de formatação de código_,

## Código de conduta

Detalhes em [docs/user_guide/code_of_conduct.md](code_of_conduct.md).

## Padrões aplicados

Este projeto segue as recomendações descritas em
[Tecnologias](../prefacio.md#tecnologias-adotadas) e
[Convenções](../prefacio.md#convenções-adotadas) Adotadas.


## Prerequisitos

- Sistema Operacional Linux Like ou WSL
- git client
- python 3.10+
- pyenv
- pip or poetry (preferencialmente)

## Qualidade de Código

É utilizado de ferramentas validadoras de qualidade de código estático,
também denominadas linters.

Há uso das seguintes:

- black / blue
- isort
- mypy
- pydocstyle
- pylint

## Segurança

Também há preocupação com a segurança do código implementado, os pacotes
`bandit` e `safety` são utilizados para monitoramento de segurança das dependências.

### bandit
Bandit é uma ferramenta projetada para encontrar problemas de segurança comuns no código Python. Para fazer isso, o Bandit processa cada arquivo, cria um AST a partir dele e executa os plug-ins apropriados nos nodos do AST.
Depois que o Bandit terminar de escanear todos os arquivos, ele gerará um relatório.
```shell
bandit -c pyproject.toml -r incolume/ test/
```

### black
O `black` é classificado como Autoformator, são programas que
refatoram seu código para se adequar ao PEP 8 automaticamente.
```shell
black --check incolumepy tests
```
### pylama
O `pylama` é um envolucro que contém: PyFlakes, pycodestyle, McCabe.
```shell
pylama incolumepy tests
```
### isort
O `isort` é um utilitário para classificar as importações
em ordem alfabética e separadas automaticamente em seções e por tipo.
```shell
isort incolumepy tests
```
### mypy
O `Mypy` é essencialmente um analizador de código estático melhorado e com
verificador de tipos, que pode detectar muitos erros de programação
analisando o código, sem precisar executá-lo.
Ele possui um poderoso sistema de tipos com recursos como
inferência de tipos, digitação gradual, genéricos e tipos de união.
```shell
mypy incolumepy
```
### pydocstyle
O `pydocstyle` é uma ferramenta de análise estática para verificar a
conformidade com as convenções docstring do Python. Ele suporta a maior
parte do PEP 257, entretanto não deve ser considerado uma
implementação de referência.
```shell
pydocstyle incolumepy tests
```
### pylint
O `Pylint` é uma ferramenta de análise de código estático do Python
que procura erros de programação, ajuda a impor um padrão de codificação,
detecta cheiros de código e oferece sugestões simples de refatoração.
É altamente configurável, possuindo pragmas especiais para controlar
seus erros e avisos de dentro do seu código, bem como de um extenso
arquivo de configuração. Também é possível escrever seus próprios plugins
para adicionar suas próprias verificações ou para estender o `pylint`
de uma forma ou de outra.
```shell
pylint incolumepy tests
```
### safety
O `safety` verifica as dependências instaladas quanto a vulnerabilidades
de segurança conhecidas.
Por padrão, ele usa o banco de dados de vulnerabilidades Python aberto
[Safety DB](https://github.com/pyupio/safety-db).
```shell
safety check
```

## Ferramentas de Automação
Para facilitar o trabalho, várias das tarefas estão
automatizadas pelo githooks, e/ou Makefile, e/ou tox e/ou taskipy.

### Tox

#### Verificação básica

Na Verificação básica engloba:
- black
- blue
- isort
- pydocstyle
- mypy
- pylint
- py310
- py311

```shell
tox
```
#### Verificação dos testes com as versões python disponíveis ####
```shell
tox -e py310,py311
```
#### Verificação de três linters apenas no em um módulo ####
```shell
tox -e pydocstyle,black,isort -- -k incolume/py/pack/module.py
```

#### Verificação de todos os linters configurados ####
```shell
tox -e linters
```

#### Verificação e relatório de cobertura ####
```shell
tox -e stats
```

#### Verificação resumida de segurança ####
```shell
tox -e safety
```

#### Execução completa ####
Executa todas as verificações diponíveis contidas no `tox`.
```shell
tox -e ALL
```

### Makefile

O `Makefile` foi personalizado para rodar com as opções necessárias.
Com o help você verá todas as opções.
```shell
make help
```

#### Iniciar ambiente dev
Através do `Makefile`, pode-se criar um ambiente virtual para o projeto,
conforme a versão python predefinida, instalando todas as dependências
necessárias, além de ativar as configurações em passos simples.

```shell
make setup
```

#### Limpeza básica do ambiente
Limpeza de arquivos temporários, logs, compilados e afins.
```shell
make clean
```

#### Limpeza profunda do ambiente
Além da limpeza básica, são removidos dist, build, htmlcov, .tox, *_cache,
e outros conteúdos gerados pelas ferramentas de desenvolvimento.
```shell
make clean-all
```

#### Gerar a documentação atualizada
```shell
make docsgen
```

#### Verificação de segurança e exposição de motivos
```shell
make safety
```


### Taskipy
Com `taskipy` as tarefas são definidas em um arquivo
e pode-se executá-las com comandos simples.

```shell
task bandit
```

```shell
task clean
```

```shell
task clean-all
```

```shell
task docs-build
```

```shell
task docs-serve
```

```shell
task lint
```

```shell
task lint_black
```

```shell
task lint_blue
```

```shell
task lint_flake8
```

```shell
task lint_isort
```

```shell
task lint_mypy
```

```shell
task lint_pydocstyle
```

```shell
task lint_pylint
```

```shell
task patch
```

```shell
task premajor
```

```shell
task preminor
```

```shell
task prerelease
```

```shell
task safety
```

```shell
task sec
```

```shell
task changelog
```
