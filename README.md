# AFND

## Configurações automato.txt

para configurar o automato é necessário passar algumas informações pro txt sendo elas:

primeira linha: ESTADOS do automato <br />
segunda linha: ALFABETO do automato <br />
terceira linha: ESTADO INICIAL do automato <br />
quarta linha: ESTADO FINAL do automato <br />

em sequencia a definição formal da tabela com os valores 

sendo quando não tem o caminho especificar com o numero 0 significando vazio e a letra E para o simbolo de cópia

por exemplo o seguinte automato

![image](https://user-images.githubusercontent.com/50429333/171743328-3f8bfd95-90ab-4c56-b151-a4a6a1479ed4.png)

q1 q2 q3 <br />
a b <br />
q1 <br />
q1 <br />
0 q2 q3 <br />
q2,q3 q3 0 <br />
q1 0 0 <br />

sempre separando os valores por espaço e quando tiver mais de uma possibilidade para cada alfabeto separar por virgula"," cada valor

