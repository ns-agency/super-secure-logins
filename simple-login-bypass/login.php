<?php

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
session_start();

$logged_in = false;

// carey: Since we want to test this without having people install a webserver
if (!isset($_SERVER['HTTP_HOST']) && count($argv) > 1) {
    parse_str($argv[1], $_POST);
}

if(isset($_POST['submit'])) {
    class DB extends SQLite3 {
        function __construct() {
            $this->open('sqlite.db');
            $this->enableExceptions(true);
        }
    }

    $db = new DB();
    $username = $_POST["username"];
    $password = $_POST["password"];
    $query = "SELECT * from users WHERE username='$username' AND password='$password'";
    $results = $db->querySingle($query,true);

    if($results) {
        echo 'SUCCESS';
    } else {
        echo 'FAILURE';
    }

    exit;
}
if($logged_in == false) {
?>
<head>
<link href="assets/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">
<script src="assets/bootstrap.min.js"></script>
<script src="assets/jquery.min.js"></script>
<link rel="stylesheet" type="text/css" href="assets/css.css">
</head>
<body>
<!-- Hello 6443! -->
<div class="wrapper fadeInDown">
  <div id="formContent">

    <form method="post">
<?php if(isset($_POST['submit'])) { ?>
<p>login failed</p> <!-- last executed query: <?= $query ?> returned nothing -->
<?php } ?>

      <input type="text" name="username" class="fadeIn second" name="login" placeholder="username">
      <input type="text" name="password" class="fadeIn third" name="login" placeholder="password">
      <input type="submit" name="submit" class="fadeIn fourth" value="Log In">
    </form>

  </div>
</div>
</body>


<?php } ?>
