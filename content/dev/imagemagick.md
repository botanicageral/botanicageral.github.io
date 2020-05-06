Title: ImageMagick
Date: 2018-05-25 14:00  
Category: Imagens
Tags: grafico, linux, terminal
Slug: ImageMagick
Author: Wilton Gonçalves
Summary: Manipulando imagens com o ImageMagick

**Definição**

O ImageMagick é uma suíte de software livre para a criação, modificação e exibição de imagens de bitmap.

Convertendo várias imagens numa pasta
A sintaxe do comando é mogrify [options] input-file. Mais pode e deve ser visto sobre esse comando, pelo Terminal: man mogrify.

Abra o Terminal nessa pasta e digite, por exemplo: mogrify -format jpg *.gif

**Convertendo de .tif para .jpeg:**

mogrify -format jpg -quality 90 *.tif
Onde -quality 90, representa a qualidade do arquivo .tif criado, e que pode ser mudado pelo usuário.

Mais conversão de formatos:

convert exemplo.png exemplo.jpg

convert exemplo.png exemplo.pdf

convert exemplo.pdf exemplo.png

convert image.cdr image.png

Fonte: [Ask Ubuntu](http://askubuntu.com/questions/22600/open-or-convert-cdr-files)

**Convertendo de PDF para PNG/JPG:**

convert sample.pdf sample.png

convert sample.pdf sample.jpg

**Gerar PDF de Lote de Imagens:**

convert *.jpg revista.pdf
Alterando o formato de acordo com suas necessidades. Terminado o processo terá um arquivo PDF das imagens.

Fonte: [Software Livre Brasil](http://softwarelivre.org/relsi/tuxtilt/gerar-pdf-de-lote-de-imagens)

**Convertendo para grayscale:**

convert image.jpg -monochrome image-bw.jpg
ou
mogrify -monochrome image.jpg

**ImageMagick - Exemplo de utilização:**

Para utilizar o ImageMagick, você deve incluir o comando convert e suas variações em sua aplicação, que podem ser visualizados utilizando o comando puramente através do terminal, temos alguns exemplos:

- animate – Anima imagens e mostra na tela
- compare – Compara matematicamente e visualmente duas imagens
- composite – Adiciona uma imagem em cima da outra
- conjure – Interpretador de scripts em linguagem Magick (MSL)
- convert – Converte e altera imagens em diversos formatos e formas
- display – Mostra imagens ou sequências de imagens na tela
- identify – Mostra informações e características de uma imagem
- import – Salva o conteúdo da tela em um arquivo (famoso print-screen)
- mogrify – Mesma coisa que o convert, só que sobrescreve os arquivos que está trabalhando
- montage – Junta várias imagens em uma só
- stream – Extrai porções e/ou pixels das imagens e salva em outro local

**Curiosidades**

Há um fork dele - [GraphicsMagick].(http://www.graphicsmagick.org/)

Há uma interface dele em Java - JMagick

Essa é uma ótima ferramenta para manipulação de imagens do mundo Linux.
