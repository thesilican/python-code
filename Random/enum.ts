enum Fruit {
  Apple = -1,
  Peach = 0,
  Orange = 1
}

// As simple as that :)
const peach: Fruit = 0;

console.log(peach === Fruit.Peach);