// Required by Webpack - do not touch
require.context('../', true, /\.(html|json|txt|dat)$/i)
require.context('../images/', true, /\.(gif|jpg|png|svg|eot|ttf|woff|woff2)$/i)
require.context('../stylesheets/', true, /\.(css|scss)$/i)

// $.ajax({
//     type: "POST",
//     url: "./databases/main.py",
//     data: { param: text}
//   }).done(function( o ) {
//      // do something
//   });

$(document).ready(function(){
    $("form").submit(function(){
      alert("Hello")
    });
  });