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
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
## Business logic vulnerabilities <a name="business-logic-vulnerabilities"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
## Clickjacking <a name="clickjacking"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
## CORS <a name="cors"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
## Cross-Site-Scripting <a name="cross-site-scripting"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
## CSRF <a name="csrf"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
## File upload vulnerabilities <a name="file-upload-vulnerabilities"></a>
##### [![](https://img.shields.io/badge/Voltar-Sum%C3%A1rio-orange?style=plastic&logo=Acclaim)](#sumário)
## Information disclosure <a name="information-disclosure"></a>

### Information disclosure in error messages

#### Descrição
As mensagens de erro detalhadas deste LAB expõem que a aplicação está usando uma versão vulnerável de um framework de terceiros. Para solucionar o LAB, obtenha e envie o número da versão deste framework.

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
>   Apache Struts 2 2.3.31
6. Para solucionar o LAB, submeta a versão identificada.
</details>

### Links Utéis
* https://matthew-brett.github.io/curious-git/reading_git_objects.html

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
