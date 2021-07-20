<?php
  $firstName = $_POST['firstname'];
  $lastName = $_POST['lastname'];
  $nameBadge = $_POST['namebadge'];
  $gender = $_POST['gender'];
  $instOrg = $_POST['InstOrg'];
  $country = $_POST['country'];
  $category = $_POST['category'];
  $email = $_POST['Email'];
  $strcon = mysqli_connect('mysql_prod08.intranet.ufba.br','csdsmng','csdsmn6!04!06','csdsdb');
  if (!$strcon) {
    die('Não foi possível conectar ao MySQL');
  }
  $strcon->set_charset("utf8");
  // Criando a declaração SQL:
  $sql = "INSERT INTO CadastroCSDS2019(firstName,lastName,nameBadge,gender,instOrg,country,category,email) VALUES ('$firstName','$lastName','$nameBadge','$gender','$instOrg','$country','$category','$email')";
  // Executando a declaração no banco de dados:
  $resultado = mysqli_query($strcon,$sql) or die("Error. Please try again by filling in all required fields.");
  echo "The registration has been completed!";
  mysqli_close($strcon);
  echo "<br><br><a href='index.html'>Return to the conference homepage.</a>";
?>
