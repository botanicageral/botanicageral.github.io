Title: GitLab e GitHub no mesmo SO
Date: 2019-05-06 17:00  
Category: Sistemas Operacionais  
Tags: git, linux
Slug: GitLab e GitHub no mesmo SO
Author: Wilton Gonçalves  
Summary: Trabalhe com GitLab e GitHub no mesmo Sistema Operacional

A algum tempo vinha tendo problemas para trabalhar com GitLab e GitHub no mesmo sistema. Tentei vários tutorias descritos na internet e não obtive sucesso.
Depois de muita frustração para executar as atividades e depois várias leituras consegui chegar a solução para esse meu problema. Vou descrever o passo a passo que fiz e talvez essa solução não funcione para outras pessoas, devemos lembrar que isso depende de muitos fatores e variáveis.

**1.** Crie um arquivo .gitconfig na sua Home, exemplo:

   *Você pode usar o seu editor de texto preferido.*

```
[user]
	name = Seu Nome
	email = nome@mail.com
[credential]
	help = cache --timeout=3600
```

**2.** Crie um arquivo chamado config dentro da pasta .ssh e dentro do arquivo salve as suas informações dos serviços, exemplo:

   *Use também qualquer editor de texto*

```
#Default GitHub
Host seu_usuario
  HostName github.com
  User git
  IdentityFile ~/.ssh/suachave.pub
 
#Second GitLab Account
Host seu_usuario
  HostName gitlab.com
  User git
  IdentityFile ~/.ssh/suachave.pub
```

*Até esse momento o GitHub já deve estar funcionando, já o GitLab não, então:*

**3.** Crie uma pasta para colocar seus projetos a ser enviados para o GitLab, eu criei como GitLab mesmo.

**4.** Agora abra o terminal e acesse a pasta que você acabou de criar e digite:

```
$ python3 -m venv gitlab
$ source gitlab/bin/activate
```
Como isso você acaba de criar um ambinte virtual Python e de ativa-lo.

Dentro da pasta crie um outro arquivo chamado .gitconfig e uma pasta .ssh. Dentro do arquivo salve suas informações como no passo **1** e dentro da pasta .ssh salve as mesmas chaves pública e privada que você criou para o acesso ao GitLab.

**5.** Crie um novo projeto e envie para o seu repositório do GitLab como faria normalmente, depois de efetuar o trabalho desative o virtual env do Python.

```
$ deactivate
```

Da próxima vez que for enviar seus projetos para o GitLab talvés não necessite ativar o virtual env do Python e caso não consiga basta ativar o env e efetuar o envio.

Essa foi a única forma que encontrei para se trabalhar com os dois serviços no mesmo sistema. Todos esses procedimentos foram feitos no Ubuntu Mate 18.04.2 LTS.