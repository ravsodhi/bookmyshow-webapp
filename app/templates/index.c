<!DOCTYPE html>
<html lang="en">

<head>
    <title>Book My Show</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="../static/css/vendor/bootstrap.min.css" rel="stylesheet">
    <link rel="shortcut icon" href="../static/img/favicon.ico">
    <script type="text/javascript" src="../static/js/vendor/jquery.min.js"></script>
    <script type="text/javascript" src="../static/js/vendor/bootstrap.min.js"></script>
    <style>
    .list-type3 {
        margin: 0 auto;
        width: 500px;
    }

.list-type3 li, .list-type3 a{
float:left;
height:35px;
       line-height:35px;
position:relative;
         font-size:15px;
         margin-bottom: 12px;
         font-family: 'Raleway', sans-serif;
transition: background-color 1.5s ease;
}
.list-type3 a{
padding:0 60px 0 12px;
background:#0089e0;
color:#fff;
      text-decoration:none;
      -moz-border-radius-bottomright:4px;
      -webkit-border-bottom-right-radius:4px;
      border-bottom-right-radius:4px;
      -moz-border-radius-topright:4px;
      -webkit-border-top-right-radius:4px;
      border-top-right-radius:4px;
}

.list-type3 a:before{
content:"";
float:left;
position:absolute;
top:0;
left:-12px;
width:0;
height:0;
       border-color:transparent #0089e0 transparent transparent;
       border-style:solid;
       border-width: 18px 12px 18px 0;
}

.list-type3 a:after{
content:"";
position:absolute;
top:15px;
left:0;
float:left;
width:6px;
height:6px;
       -moz-border-radius:2px;
       -webkit-border-radius:2px;
       border-radius:2px;
background:#fff;
           -moz-box-shadow:-1px -1px 2px #004977;
           -webkit-box-shadow:-1px -1px 2px #004977;
           box-shadow:-1px -1px 2px #004977;
}
.list-type3 a:hover{
background:#555;
}

.list-type3 a:hover:before{
    border-color:transparent #0089e0 transparent transparent;
}
    
    .navbar-no-margin {
        margin-bottom: 0!important;
    }
    
    .button {
        display: inline-block;
        padding: 7.5px 15.5px;
        font-size: 24px;
        cursor: pointer;
        text-align: center;
        text-decoration: none;
        outline: none;
        color: #fff;
        background-color: #008CBA;
        border: none;
        border-radius: 15px;
        box-shadow: 0 9px #999;
    }
    
    .button:hover {
        background-color: #4783e5
    }
    
    .button:active {
        background-color: #0b47a8;
        box-shadow: 0 5px #666;
        transform: translateY(4px);
    }
    
    * {
        box-sizing: border-box
    }
    
    body {
        font-family: Verdana, sans-serif;
    }
    
    .mySlides {
        display: none
    }
    /* Slideshow container */
    
    .slideshow-container {
        /*max-width: 1000px;*/
        width: 100% position: relative;
        margin: auto;
    }
    /* Caption text */
    
    .text {
        color: #f2f2f2;
        font-size: 15px;
        padding: 8px 12px;
        position: absolute;
        bottom: 8px;
        width: 100%;
        text-align: center;
    }
    /* Number text (1/3 etc) */
    
    .numbertext {
        color: #f2f2f2;
        font-size: 12px;
        padding: 8px 12px;
        position: absolute;
        top: 0;
    }
    /* The dots/bullets/indicators */
    
    .dot {
        height: 13px;
        width: 13px;
        margin: 0 2px;
        background-color: #bbb;
        border-radius: 50%;
        display: inline-block;
        transition: background-color 0.6s ease;
    }
    
    .active {
        background-color: #717171;
    }
    /* Fading animation */
    
    .fade {
        -webkit-animation-name: fade;
        -webkit-animation-duration: 4s;
        animation-name: fade;
        animation-duration: 4s;
    }
    
    @-webkit-keyframes fade {
        from {
            opacity: .4
        }
        to {
            opacity: 1
        }
    }
    
    @keyframes fade {
        from {
            opacity: .4
        }
        to {
            opacity: 1
        }
    }
    /* On smaller screens, decrease text size */
    
    @media only screen and (max-width: 300px) {
        .text {
            font-size: 11px
        }
    }
    </style>
</head>

<body style="background-image: url(http://wallpaperswide.com/download/light_background-wallpaper-1600x900.jpg)">
    <nav class="navbar navbar-inverse navbar-no-margin">
        <div class="container-fluid">
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#myNavbar">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Book My Show</a>
            </div>
            <div class="collapse navbar-collapse" id="myNavbar">
                <ul class="nav navbar-nav">
                    <li><a href="#">Movies</a></li>
                </ul>
                <form id="navBarSearchForm" class="navbar-form navbar-left" style="margin-left:20%">
                    <div class="input-group" style="width:200%">
                        <input type="text" class="form-control" placeholder="Search">
                        <div class="input-group-btn">
                            <button class="btn btn-default" type="submit">
                                <i class="glyphicon glyphicon-search"></i>
                            </button>
                        </div>
                    </div>
                </form>
                <ul class="nav navbar-nav navbar-right">
                    <li><a href="#"><span class="glyphicon glyphicon-user"></span> Sign Up</a></li>
                    <li><a href="#"><span class="glyphicon glyphicon-log-in"></span> Login</a></li>
                </ul>
            </div>
        </div>
        </div>
    </nav>
    <div class="slideshow-container">
        <div class="mySlides fade">
            <img src="../static/img/img1.jpg" style="width:100%; max-height:400px">
        </div>
        <div class="mySlides fade">
            <img src="../static/img/img2.jpg" style="width:100%; max-height:400px">
        </div>
        <div class="mySlides fade">
            <img src="../static/img/img3.jpg" style="width:100%; max-height:400px">
        </div>
    </div>
    <br>
    <div style="text-align:center">
        <span class="dot"></span>
        <span class="dot"></span>
        <span class="dot"></span>
    </div>
    <div class="container" >
        <h3>Now Showing</h3>
    </div>
    <!-- Ravsimar -->
    <div class="list-type3" style="width:80%;">
        <div style="background-color:powderblue;">
            <h3 style="float:left; margin-top:0;">
                HEllo
            </h3>
            <li style="float:right"><a href="#">Book Now</a></li>
        </div>
    </div>
    <!-- ravsimar -->
    <script>
    var slideIndex = 0;
    showSlides();

    function showSlides() {
        var i;
        var slides = document.getElementsByClassName("mySlides");
        var dots = document.getElementsByClassName("dot");
        for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";
        }
        slideIndex++;
        if (slideIndex > slides.length) {
            slideIndex = 1
        }
        for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
        }
        slides[slideIndex - 1].style.display = "block";
        dots[slideIndex - 1].className += " active";
        setTimeout(showSlides, 4000); // Change image every 2 seconds
    }
    </script>
</body>

</html>
