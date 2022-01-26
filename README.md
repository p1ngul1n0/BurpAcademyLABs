# Laboratórios da Burp Academy

# Sumário
- [Authentication](#authentication)
- [Business logic vulnerabilities](#business-logic-vulnerabilities)      
- [Clickjacking](#clickjacking)
- [CORS](#cors)
- [Cross-Site-Scripting](#cross-site-scripting)
- [CSRF](#csrf)
- [File upload vulnerabilities](#file-upload-vulnerabilities)
- [Information disclosure](#information-disclosure) 
- [OAuth authentication](#oauth-authentication)
- [Server-side request forgery (SSRF)](#server-side-request-forgery)
- [SQL injection](#sql-injection)
- [WebSockets](#websockets)
- [XML external entity (XXE) injection](#xxe-injection)

## Authentication <a name="authentication"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange)](#sumário)
## Business logic vulnerabilities <a name="business-logic-vulnerabilities"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange)](#sumário)
## Clickjacking <a name="clickjacking"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange)](#sumário)
## CORS <a name="cors"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange)](#sumário)
## Cross-Site-Scripting <a name="cross-site-scripting"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange)](#sumário)
## CSRF <a name="csrf"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange)](#sumário)
## File upload vulnerabilities <a name="file-upload-vulnerabilities"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange)](#sumário)

## Information disclosure <a name="information-disclosure"></a> ![](https://img.shields.io/badge/5%2F5-COMPLETED-orange)
<details>
  <summary>Visualizar LABs</summary>
  
### Information disclosure in error messages

#### Descrição
Este LAB possui mensagens de erro detalhadas que expõem o uso de uma versão vulnerável de um framework de terceiros. Para solucionar o LAB, obtenha e envie o número da versão deste framework.

### Solução
<details>
  
<summary>:bulb:</summary>

1. Acesse os detalhes de qualquer produto do catálogo.
2. Uma chamada GET com o parâmetro `productId` é realizada:
> GET /product?productId=2
3. Substitua o parâmetro por um caractere especial qualquer:
> GET /product?productId='
4. Reenvie a chamada com o parâmetro alterado.
5. Uma mensagem de erro detalhada será recebida, observando a última linha da mensagem, é possível identificar a versão do Apache Struts utilizada.
> 	at java.base/java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:635)
>	  at java.base/java.lang.Thread.run(Thread.java:833)
>
>  Apache Struts 2 2.3.31
6. Para solucionar o LAB, submeta a versão identificada.
</details>

### Information disclosure on debug page

#### Descrição
Este LAB contém uma página de debug que expõe informação sensível da aplicação. Para solucionar o LAB, obtenha e envie a variável de ambiente `SECRET_KEY`. 

### Solução
<details>
  
<summary>:bulb:</summary>

1. Busque por comentários na página, é possível identificar o comentário.
> \<!-- \<a href=/cgi-bin/phpinfo.php>Debug</a> -->
2. Acesse a página presente no comentário, no caso `/cgi-bin/phpinfo.php`.
3. Na página acessada é possível visualizar a variável de ambiente `SECRET_KEY`.
4. Para solucionar o LAB, submeta o valor da variável encontrada.
</details>

### Source code disclosure via backup files

#### Descrição
Este LAB vaza seu código fonte através de arquivos de backup que estão em um diretório escondido. Para solucionar o LAB, identifique e envie a senha do banco de dados, que esta fixa e exposta no código.

### Solução
<details>
  
<summary>:bulb:</summary>

1. Enumerando os diretórios da aplicação, é possível identificar o diretório `backup`.
2. Acesse o diretório descoberto, onde é possível visualizar o arquivo `ProductTemplate.java.bak`.
3. Acesse o arquivo identificado.
4. No código, é possível identificar os dados de conexão do banco de dados, sendo possível obter a senha de acesso.
```java
    ConnectionBuilder connectionBuilder = ConnectionBuilder.from(
                "org.postgresql.Driver",
                "postgresql",
                "localhost",
                5432,
                "postgres",
                "postgres",
                "kw9ce735cw5r1r1syf3cxkx0dar4zp29"
```
5. Para solucionar o LAB, submeta a senha do banco de dados.
</details>

### Authentication bypass via information disclosure

#### Descrição
A interface administrativa deste LAB tem uma vulnerabilidade de bypass na autenticação, porém é impraticável explorar sem conhecimento do cabeçalho HTTP customizado utilizado pelo front-end.

Para solucionar o LAB, obtenha o cabeçalho e utilize-o para bypassar a autenticação. Acesse o painel administrativo e delete a conta do Carlos.

### Solução
<details>
  
<summary>:bulb:</summary>

1. Autentique utilizando o usuário e senha `wiener:peter`.
2. Envie uma requisição com método HTTP TRACE para o endpoint `/admin`.
3. Observando a resposta é possível identificar o cabeçalho `X-Custom-IP-Authorization: 189.54.133.189`.
4. Envie outra requisição para o endpoint `/admin` mas desta vez com método GET e o cabeçalho obtido anteriormente com o IP `127.0.0.1`.
5. A chamada ficará desta forma e sua resposta apresentará o painel administrativo
```
GET /admin HTTP/1.1 
[...]
X-Custom-IP-Authorization: 127.0.0.1  
```
6. Para solucionar o LAB, delete o usuário de Carlos.
</details>

### Information disclosure in version control history

#### Descrição
Este LAB expõe informação sensível através do seu histórico de controle de versão. Para solucionar este LAB, obtenha a senha do usuário administrador, realize login e delete a conta de Carlos.

### Solução
<details>
  
<summary>:bulb:</summary>

1. Realize o mapeamento da URL do LAB, o diretório `./git` será identificado.
2. Verifique o conteúdo do arquivo `COMMIT_EDITMSG`, é possível identificar uma frase que indica que a senha do administrador estava fixa no código.
> Remove admin password from config
3. Realize download dos arquivos presentes na pasta `objects`.
4. Utilizando Python é possível ler o conteúdo dos objetos GIT baixados ([Código](https://github.com/sampzzz/BurpAcademyLABs/blob/83fca3be10b16b7c9f05907d89735aa332e6b7ae/Information%20disclosure/Information%20disclosure%20in%20version%20control%20history/exploit.py)).
5. O programa python irá retornar a linha de código que expõe a senha do administrador: 
> 'b'blob 36\x00ADMIN_PASSWORD=322ix05781cxs4gp4nvn\n'
6. Para solucionar o LAB, autentique-se com o usuário `administrator` utilizando a senha obtida e delete o usuário `carlos`.
</details>

### Links Utéis
* https://matthew-brett.github.io/curious-git/reading_git_objects.html
</details>

##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
## OAuth authentication <a name="oauth-authentication"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
## Server-side request forgery (SSRF) <a name="server-side-request-forgery"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
## SQL injection <a name="sql-injection"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
## WebSockets <a name="websockets"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
## XML external entity (XXE) injection <a name="xxe-injection"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
