# Explorando Marte

## Informações iniciais
* O projeto utiliza [Python 3.9](https://www.python.org/downloads/release/python-390/);
* As classes foram separadas por domínio;
* Não foi utilizado nenhum famework ou pacote externo;
* A entrada foi feita com arquivos no diretório <code>./probes/*.txt</code>, cada arquivo representa uma Sonda;
* A saída é exibida no terminal, se der tudo certo mostra onde a Sonda parou e em caso de erro uma mensagem é exibida;
* Foi criado um arquivo de teste no diretório <code>./tests/</code>;

## Algumas regras do sistema
* As Sondas são carregadas, os dados são validados e realiza os movimentos;
* A Sonda pode se mover apenas dentro da área determinada pelo usuário;
* Se tentar adicionar uma Sonda fora da área demarcada, um erro é exibido;
* Se tentar mover uma Sonda para fora da área demarcada, o comando é ignorado;

## O que não foi feito
* Nenhuma validação de arquivo de Sonda foi implementada, validei apenas os dados existentes no mesmo. 
  Exemplo de validações necessárias: Tipo de arquivo, tamanho máximo do arquivo, numero máximo de arquivos carregados, etc.
* O teste desenvolvido não cobre todos os cenário;

## Executar código
```shell
python3 main.py
```

## Executar testes
```shell
python3 -m unittest -v tests/test_space_probe.py
```