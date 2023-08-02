# autenticacao-whitelabel-django
Essa api pode ser usada por diferentes empresas ( unidades ), com seus respectivos usuários


<h1 align="center" id="title">Autenticação WhiteLabel Django</h1>

<p id="description">Essa aplicação web foi desenvolvida com o propósito de permitir um mecanismo de autenticação que seja reutilizável por várias empresas, cadastrando-as no sistema, sendo que cada uma terá direito à um subdomínio diferente. Por exemplo: nessa api, ao clonar o projeto, terão 3 empresas criadas por padrão (adidas, nike e puma). Para acessá-las, deve-se recorrer às seguintes urls ( http://nike.localhost:8000/accounts/login/, http://adidas.localhost:8000/accounts/login/ e http://puma.localhost:8000/accounts/login/). Cada empresa terá seus respectivos usuários. A api foi estruturada seguindo os princípios <strong>SOLID</strong> da programação orientada a objetos, aplicando  utilização de <strong>heranças</strong>, uso de <strong>Padrão arquitetural MTV</strong>, etc.</p>

  <h2> Especificações da api</h2>

*   <p><strong>Arquitetura de software: </strong></p><strong>* MTV</strong> </p>
*    <p><strong>User customizado: </strong></p>* Foi necessário modificar a classe de autenticação padrão do Django Auth para a model <strong>Usuario</strong> </p>
*    <p><strong>Sistema de Whitelabel: </strong></p> Cada empresa é representada pela model <strong> Unidade</strong>. O reconhecimento de cada <strong>Unidade</strong> se dá a partir do <strong>subdomínio</strong> passado. O subdomínio é a propriedade <strong>'nome'</strong> da model <strong>'Unidade'</strong></p>
*    <p><strong>Docker: </strong></p> Sim </p>
*    <p><strong>Testes unitários: </strong></p> Sim </p>
*    <p><strong>Proteção contra ataque CSRF: </strong></p><strong> Sim </p>
*    <p><strong>Validação de inputs: </strong></p><strong> Sim </p>
*    <p><strong>Permite cadastro de novas unidades: </strong></p><strong> Sim, a partir do painel admin. Será descrito a seguir. </p>

  
<h2>💻 Feito em</h2>

*   Django
*   Usando a biblioteca <strong>AllAuth</strong>

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
    <li><p>Se obtiver sucesso, redirecionará para a página inicial ( de informações do usuário logado )</p></li>
    <li><p>A imagem da tela de login será obtida com base no subdomínio passado</p></li>
  </ul>
  <br>
  <h5>Se 'http://adidas.localhost:8000/accounts/login/'</h5>
  <br>
   <img src="prints\login-adidas.png" alt="Logo">
   <br>
  <h5>Se 'http://nike.localhost:8000/accounts/login/'</h5>
   <br>
   <img src="prints\login-nike.png" alt="Logo" >
   <br>
  <h5>Se 'http://puma.localhost:8000/accounts/login/'</h5>
   <br>
   <img src="prints\login-puma.png" alt="Logo" >
   <br>
  <br>
  <br>
  <br>


  <h3>*Login validação input</h3>
  <ul>
    <li>Os inputs serão validados</li>
    
  </ul>

  <br>
   <img src="prints\login-email-incorreto.png" alt="Logo" >
   <br>
   <img src="prints\login-email-invalido.png" alt="Logo">
   <br>
  <br>
  <br>
  <br>



  <h3>*Cadastro</h3>
  <ul>
    <li><h5>PATH 'http://adidas.localhost:8000/accounts/signup/'</h56></li>
    <li><p>Nessa tela, o usuário preencherá o nome, email e senha para se cadastrar no sistema</p></li>
    <li><p>Se a validação for ok, logará o usuário e redirecionará para a página inicial ( de informações do usuário logado )</p></li>

  </ul>
  <br>
   <img src="prints\cadastrar.png" alt="Logo" >
   <br>
  <br>
  <br>
  <br>


  <h3>*Cadastro validação input</h3>
  <ul>
    <li>Os inputs serão validados</li>
    
  </ul>
  <br>
   <img src="prints\cadastro-email-ja-cadastrado.png" alt="Logo" >
   <br>
   <img src="prints\cadastro-senha-divergente.png" alt="Logo" >
   <br>
   <img src="prints\cadastro-validacao.png" alt="Logo" >
   <br>
  <br>
  <br>
  <br>


  
  
  <h3>*Dados do usuário ( Página Inicial ):</h3>
  <ul>
    <li><h5>PATH 'http://adidas.localhost:8000/'</h56></li>
    <li><p>Nessa página serão descritas informações sobre o usuário logado</p></li>
  </ul>
  <br>
   <img src="prints\usuario-adidas.png" alt="Logo" >
   <br>
   <img src="prints\usuario-nike.png" alt="Logo" >
   <br>
   <img src="prints\usuario-puma.png" alt="Logo" >
   <br>
  <br>
  <br>
  <br>
  
  <h3>*Editar usuário:</h3>
  <ul>
    <li><h5>PATH 'http://adidas.localhost:8000/editar/'</h56></li>
  </ul>
  <br>
   <img src="prints\edicao-usuario.png" alt="Logo" >
  <br>
  <br>
  <br>

<h3>*Validação edição usuário</h3>
  <br>
   <img src="prints\edicao-usuario-validacao.png" alt="Logo" >
   <br>
  <br>
  <br>
  <br>
  
  <h3>*Deletar usuário:</h3>
  <ul>
    <li><p>Ao clicar em 'deletar', o usuário será deletado, será deslogado e redirecionado para a página de login</p></li>
  </ul>
  <br>
   <img src="prints\deletar.png" alt="Logo" >
  <br>
  <br>
  <br>
  <h3>*Logout:</h3>
  <ul>
    <li><p>Ao clicar em 'logout', o usuário será deslogado e redirecionado para a página de login</p></li>
  </ul>
    <br>
   <img src="prints\deslogar.png" alt="Logo" ">
  <br>
  <br>
  <br>
  
   <h3>*Adição de unidades:</h3>
  <ul>
    <li><h5>Path: 'http://localhost:8000/admin/login/?next=/admin/usuarios/unidade/add/'</h5></li>
    <li><p>Deve-se preencher o nome da unidade (será o subdomínio) e inserir um link da logo da unidade</p></li>
    <li><p>Se eu criar uma unidade com o 'nome' 'xpto', deveria acessá-la pela path 'http://xpto.localhost:8000/accounts/login/'</p></li>
  </ul>
    <br>
   <img src="prints\unidade.png" alt="Logo" ">
  <br>
  <br>
  <br>


  
