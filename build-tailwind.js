const exec = require('child_process').exec;

exec('./node_modules/.bin/tailwindcss -i ./Landingpage/static/landing/css/input.css -o ./Landingpage/static/landing/css/style.css --content ./Landingpage/templates/**/*.html --minify', (err, stdout, stderr) => {
  if (err) {
    console.error(`Error: ${stderr}`);
    process.exit(1);
  }
  console.log(stdout);
});
