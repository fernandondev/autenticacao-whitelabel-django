# autenticacao-whitelabel-django
Essa api pode ser usada por diferentes empresas ( unidades ), com seus respectivos usuários


<h1 align="center" id="title">Autenticação WhiteLabel Django</h1>

<p id="description">Essa aplicação web foi desenvolvida com o propósito de permitir um mecanismo de autenticação que seja reutilizável por várias empresas. Por exemplo: nessa api, tem 3 empresas criadas (adidas, nike e puma). Para acessá-las, deve-se recorrer às seguintes urls ( http://nike.localhost:8000/accounts/login/, http://adidas.localhost:8000/accounts/login/ e http://puma.localhost:8000/accounts/login/). Cada empresa terão seus respectivos usuários. A api foi estruturada seguindo os princípios <strong>SOLID</strong> da programação orientada a objetos, aplicando  utilização de <strong>heranças</strong>, uso de <strong>Padrão arquitetural</strong>, etc.</p>

  <h2> Especificações da api</h2>

*   <p><strong>Arquitetura de software: </strong></p><strong>* MVT</strong> </p>
*    <p><strong>User customizado: </strong></p>* Foi necessário modificar a classe de autenticação padrão do Django Auth para a model <strong>Usuario</strong> </p>
*    <p><strong>Sistema de Whitelabel: </strong></p> Cada empresa é representada pela model <strong> Unidade</strong>. O reconhecimento de cada <strong>Unidade</strong> se dá a partir do <strong>subdomínio</strong> passado. O subdomínio é a propriedade <strong>'nome'</strong> da model <strong>'Unidade'</strong></p>
*    <p><strong>Arquitetura de software: </strong></p><strong>* MVT</strong> </p>

  
<h2>💻 Feito em</h2>

*   Django

  <h2>Contas Default</h2>
  <p><strong>url</strong>: http://nike.localhost:8000/accounts/login/</p>
  <p><strong>email</strong>:nike@nike.com</p>
  <p><strong>senha</strong>:nike123456</p>

  <p><strong>url</strong>: http://adidas.localhost:8000/accounts/login/</p>
  <p><strong>email</strong>:adidas@adidas.com</p>
  <p><strong>senha</strong>:adidas123456 </p>

  <p><strong>url</strong>: http://puma.localhost:8000/accounts/login/</p>
 <p><strong>email</strong>:puma@puma.com</p>
  <p><strong>senha</strong>:puma123456</p>

  <p><strong>superuser</strong>:</p>
  <p><strong>email</strong>: fernando@fernando.com</p>
  <p><strong>senha</strong>:123456</p>

  
  
  <h2>Páginas</h2>
  <br>
  <br>

<h3>*Login</h3>
  <ul>
    <li><h5>PATH : 'http://adidas.localhost:8000/accounts/login/'</h56></li>
    <li><p>O usuário deverá preencher o email e senha e clicar em logar, para se autenticar</p></li>
  </ul>
  <br>
   <img src="prints\projeto-livro-login.png" alt="Logo" width="1000" height="700">
   <br>
  <br>
  <br>
  <br>


  <h3>*Login validação input</h3>

  <br>
   <img src="prints\projeto-livro-login-validacao.png" alt="Logo" width="1000" height="700">
   <br>
  <br>
  <br>
  <br>



  <h3>*Cadastro</h3>
  <ul>
    <li><h5>PATH '/paginaCadastro'</h56></li>
    <li><p>Nessa tela, o usuário preencherá o nome, email e senha para se cadastrar no sistema</p></li>

  </ul>
  <br>
   <img src="prints\projeto-livro-cadastro.png" alt="Logo" width="1000" height="700">
   <br>
  <br>
  <br>
  <br>


  <h3>*Cadastro validação input</h3>
  <ul>
    <li><h5>PATH '/paginaCadastro'</h56></li>
  </ul>
  <br>
   <img src="prints\projeto-livro-cadastro-validacao.png" alt="Logo" width="1000" height="700">
   <br>
  <br>
  <br>
  <br>


  
  
  <h3>*Dados do usuário ( Página Inicial ):</h3>
  <ul>
    <li><h5>PATH '/'</h56></li>
    <li><p>Nessa tela, deverá ser preenchido o input 'Pesquisar livro' e clicar em 'Pesquisar'</p></li>
    <li><p>Após isso, o backend fará uma requisição para o Google api, que retornará os dados</p></li>
    <li><p>O sistema tratará os dados e exibirá 40 livros correspondentes à chave da pesquisa em diversos cards</p></li>
  </ul>
  <br>
   <img src="prints\projeto-livro-tela-inicial.png" alt="Logo" width="1000" height="700">
   <br>
  <br>
  <br>
  <br>
  <h3>*Editar usuário:</h3>
  <ul>
    <li><h5>PATH '/livro'</h56></li>
    <li><p>Os livros serão listados em formatos de card, contendo foto, título e nome do autor </p></li>
    <li><p>Há ainda o botão 'Detalhes' e 'Preview</p></li>
  </ul>
  <br>
   <img src="prints\projeto-livro-livros.png" alt="Logo" width="1000" height="700">
  <br>
  <br>
  <br>
  <h3>*Deletar usuário:</h3>
  <ul>
    <li><p>Abre-se um modal contendo a descrição, foto, autor, data de publicação e editora do livro selecionado</p></li>
  </ul>
  <br>
   <img src="prints\projeto-livro-detalhes.png" alt="Logo" width="1000" height="700">
  <br>
  <br>
  <br>
  <h3>*Logout:</h3>
  <ul>
    <li><p>Há um redirecionamento para a página da google contendo uma preview de algumas páginas do livro</p></li>
  </ul>
    <br>
   <img src="prints\projeto-livro-preview.png" alt="Logo" width="1000" height="700">
  <br>
  <br>
  <br>
   <h3>*Responsividade: </h3>
    <br>
   <img src="prints\projeto-livro-responsividade.png" alt="Logo" width="400" height="700">

  
