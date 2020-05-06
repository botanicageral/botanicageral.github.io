Title: Software livre para análise de dados
Date: 2018-06-07 20:00  
Category: Estatistica  
Tags: biologia, matemática, estatistica
Slug: PSPP
Author: Wilton Gonçalves  
Summary: Uma alternativa Open Source ao IBM SPSS Statistics

O IBM® SPSS Statistics® é o software estatístico líder de mercado, no mundo usado para solucionar uma ampla variedade de problemas de negócios e de pesquisas. Oferece um amplo conjunto de recursos, incluindo análise ad hoc, teste de hipótese e relatórios, facilitando o gerenciamento de dados, a seleção e execução de análises e o compartilhamento de seus resultados. Novos recursos na versão 25 incluem estatísticas bayesianas, gráficos prontos para publicação e integração aprimorada com software de terceiros. O SPSS Statistics oferece uma edição base com add-ons opcionais que expandem seus recursos de análise preditiva. Esta solução está disponível para compra por meio de uma assinatura ou de uma licença permanente. Sua assinatura está iniciando em R$ 425,68 por usuário/mês.

Fonte: [IBM SPSS Statistics](https://www.ibm.com/br-pt/marketplace/spss-statistics)

Para fugir das assinaturas, licenças de usuários e pirataria, exite uma ótima alternativa, o PSPP.

PSPP é um software livre para análise de dados, destinado a ser uma alternativa para o IBM SPSS. Ele possui uma interface gráfica de usuário e interface de linha de comando. Está escrito em C e usa a Biblioteca Científica GNU para suas rotinas matemáticas. Seu uso permite gerar relatórios tabulados, normalmente utilizados na realização de análises descritivas e inferências a respeito de correlações entre variáveis.

O software possibilita a realização de análises descritivas, testes T, regressão linear e testes não paramétricos. Ele foi especialmente projetado para realizar estas análises o mais rápido possível, independente do número de entradas.

Fonte: [Wikipédia](https://pt.wikipedia.org/wiki/PSPP)

Para fazer a instalação, basta procurar nas lojas de aplicativos de sua distribuição Linux preferida ou acessar a página oficial do projeto e baixar os binários para sua distribuição ou Sistema Operacional. Ele também funciona nos seguintes Sistemas Operacinais: Mac OS X, OpenBSD, NetBSD, FreeBSD e Windows.

[Clique aqui](https://www.gnu.org/software/pspp/) para acessar o site do GNU PSPP. Para usuários de Linux pode fazer o download direto [clicando aqui](http://gnu.c3sl.ufpr.br/ftp/pspp/). A versão atualizada enquanto escrevo este post é a 1.0.1,	publicada em 27/08/2017.

Caso tenha baixado o código do PSPP, ele vem com a extenção .tar.gz, siga os passo abaixo em um terminal para fazer a instalação:

```
tar -xzf pspp-*.tar.gz
cd pspp-*
./configure
make
sudo make install
```

O PSPP é uma ótima ferramenta para os estudantes de Graduação, Pós-Graduação e Instituições que não possuem recursos financeiros para adquirir o IBM SPSS.

Até o próximo post e bom uso da ferramenta.
