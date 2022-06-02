# AFND

## Configurações automato.txt

para configurar o automato é necessário passar algumas informações pro txt sendo elas:

primeira linha: ESTADOS do automato <br />
segunda linha: ALFABETO do automato <br />
terceira linha: ESTADO INICIAL do automato <br />
quarta linha: ESTADO FINAL do automato <br />

em sequencia a definição formal da tabela com os valores 

Quando não temos o caminho especificar com o numero 0 significando vazio <br /> 
E a letra E para o simbolo de cópia 

por exemplo o seguinte automato

![image](https://user-images.githubusercontent.com/50429333/171743328-3f8bfd95-90ab-4c56-b151-a4a6a1479ed4.png)

![image](https://user-images.githubusercontent.com/50429333/171745660-67422df8-2017-4b0b-b11d-0a98a38f1f1a.png)


q1 q2 q3 --- ESTADOS <br />
a b --- ALFABETO<br />
q1 ---ESTADO INICIAL<br />
q1 --- ESTADO FINAL<br />
--- TABELA COM OS VALORES SENDO AS COLUNAS NA SEQUENCIA DO ALFABETO <br />
A  B  E --- APENAS PARA DEMONSTRAR A COLUNA(NÃO PRECISA ESTAR NO ARQUIVO ESSA INFORMAÇÃO <br />
0 q2 q3 --- LINHA DO PRIMEIRO ESTADO(q1)<br />
q2,q3 q3 0 --- LINHA DO SEGUNDO ESTADO(q2)<br />
q1 0 0 --- LINHA DO TERCEIRO ESTADO(q3)<br />

sempre separando os valores por espaço e quando tiver mais de uma possibilidade para cada alfabeto separar por virgula"," cada valor

