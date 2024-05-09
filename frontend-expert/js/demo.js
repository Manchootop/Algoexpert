// function test() {
//   const constNum = 0;
//   let letNum = 0;
//   letNum = 2;
// //   constNum = 2; error

//   const arr = [1, 2, 3];
//   //   arr = [1, 2, 3, 4] error
//   arr.push(4);
//   console.log(arr);
//   console.log("letnum", letNum);
//   console.log("constNum", constNum);
// }

// test();

// const arr = [1, 2, 3, 3];
// // console.log(arr);

// // const arr = new Array();
// // arr.lenght = 10;
// // arr.fill(0);

// console.log(arr[1] = 10);
// console.log(arr.includes(3));
// console.log(arr.lastIndexOf(3));

// const arr = [1, 2, 3];

// arr.push(4, 5, 6);
// arr.unshift(1); // add to start
// arr.shift(1);
// // console.log(typeof arr); object -> not useful
// console.log(Array.isArray(arr)); // (arr instanceof Array)
// // console.log(arr.pop());
// // arr.pop();

// console.log(arr);

// const arr = [1, 2, 3]

// arr.splice(0, 1, 'hello', 'world');
// console.log(arr);

const arr = [1, 2, 3];

// const newArr = arr.slice(1, 2); // 2 is exclusive so its 1, 1 => arr[1]; 1, 3 => arr[1] and arr[2]
// console.log(newArr);

// const newArr = arr.concat(['hello', 'world'])
// console.log(newArr);

// arr.reverse();
// console.log(arr);

// console.log(arr.join(' | '));

// console.log(arr);

// for (let i = 0; i < arr.length; i++) {
//     console.log(arr[i]);
// }

// let i = 0;
// for (const value of arr) {
//     console.log(value);
//     i++;
// }

// arr.forEach(function(value, index, array) {
//     console.log(value, index, this);
// }, {num: 10})

const mapArray = arr.map(
  function (value, index, array) {
    console.log(array);
    return value + index + this.num;
  },
  { num: 10 }
);

console.log(mapArray);

const filteredArray = arr.filter(
  function (value, index, array) {
    return value > 1;
  },
  { num: 1 }
);

const foundValue = arr.find(
  function (value) {
    return value > this.num;
  },
  { num: 1 }
);

const allPass = arr.every(
  function (value) {
    return value > this.num;
  },
  { num: 1 }
);

const sum = arr.reduce(function (accumulator, currValue) {
  return accumulator + currValue;
}, 0);

const sumRight = arr.reduceRight(function (accumulator, currValue) {
    return accumulator + currValue;
  }, 0);
console.log(sum);
console.log(mapArray);
console.log(filteredArray);
