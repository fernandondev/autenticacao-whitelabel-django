# autenticacao-whitelabel-django
Essa api pode ser usada por diferentes empresas ( unidades ), com seus respectivos usuários


<h1 align="center" id="title">Consulta de livros laravel</h1>

<p id="description">Essa aplicação web foi desenvolvida com o propósito de permitir buscas de livros fazendo integração com a api da google Books Api. A api foi estruturada seguindo os princípios <strong>SOLID</strong> da programação orientada a objetos, aplicando <strong>inversão de dependência</strong>, utilização de <strong>heranças</strong>, uso de <strong>Padrão arquitetural</strong>, etc.</p>

  <h2> Especificações da api</h2>

*   <p><strong>Arquitetura de software: </strong></p><strong>* MVT</strong> </p>

  
<h2>💻 Feito em</h2>

*   Django

  <h2>Contas</h2>
  url: http://nike.localhost:8000/accounts/login/
  email:nike@nike.com
  senha:nike123456

  url: http://adidas.localhost:8000/accounts/login/
  email:adidas@adidas.com
  senha:adidas123456 

  url: http://puma.localhost:8000/accounts/login/
  email:puma@puma.com
  senha:puma123456

  superuser:
  email: fernando@fernando.com
  senha:123456

  
  
  <h2>Páginas</h2>
  <br>
  <br>

<h3>*Login</h3>
  <ul>
    <li><h5>PATH '/paginaLogin'</h56></li>
    <li><p>O usuário deverá preencher o email e senha e clicar em logar, para se autenticar</p></li>
  </ul>
  <br>
   <img src="prints\projeto-livro-login.png" alt="Logo" width="1000" height="700">
   <br>
  <br>
  <br>
  <br>


  <h3>*Login validação input</h3>
  <ul>
    <li><h5>PATH '/paginaLogin'</h56></li>
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


  
  
  <h3>*Ao logar:</h3>
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
  <h3>*Após pesquisar o livro:</h3>
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
  <h3>*Ao clicar em detalhes:</h3>
  <ul>
    <li><p>Abre-se um modal contendo a descrição, foto, autor, data de publicação e editora do livro selecionado</p></li>
  </ul>
  <br>
   <img src="prints\projeto-livro-detalhes.png" alt="Logo" width="1000" height="700">
  <br>
  <br>
  <br>
  <h3>*Ao clicar em preview:</h3>
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

  
