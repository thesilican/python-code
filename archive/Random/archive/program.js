const fun = (lines) => {
  let filesystem = {};
  let pwdPath = [];
  let pwd = filesystem;
  for (let line of lines) {
    try {
      let args = line.split(" ");
      let a = args[0];
      let b = args[1];
      if (a == "cd") {
        x = pwdPath.slice();
        for (let p of b.split("/")) {
          if (p == "..") x.pop();
          else x.push(p);
          d = filesystem;
          for (let c of x) {
            d = d[c];
          }
          if (d == undefined) throw x;
          pwd = d;
          pwdPath = x;
        }
      }
      if (a == "mkdir" && !(b in pwd)) {
        pwd[b] = {};
      }
      if (a == "touch" && !(b in pwd)) {
        pwd[b] = 1;
      }
      if (a == "rm") {
        if (pwd[b] == 1) {
          delete pwd[b];
        }
        if (b == "-r") {
          delete pwd[args[2]];
        }
      }
    } catch {}
  }
  console.log("/");
  const s = (d, D = 1) => {
    for (let key in filesystem) {
      console.log(" ".repeat(D), key);
      if (d[key] != 1) s(d[key], D + 1);
    }
  };
  s(filesystem);
};

const text = `
mkdir documents
cd documents
touch document.docx
cd ..
mkdir downloads
cd downloads
touch coolgoats.mp3
touch zippedfile.zip
mkdir zippedfile
cd zippedfile
touch notavirus.exe
cd ../..
mkdir pictures
cd pictures
touch myvacation.png
`;
fun(text.trim().split("\n"));
