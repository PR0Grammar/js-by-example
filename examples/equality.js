const obj = {};
const arr = [];

// **** Loose equality ****
console.log("123" == 123); // True
console.log(undefined == null); // True
console.log(false == 0); // True
console.log(NaN == false); // False
console.log(NaN == NaN); // False
console.log([1, 2, 3] == "1,2,3"); // True
console.log("abc" == "abc"); // True
console.log({} == {}); // False
console.log([] == []); // False
console.log(obj == obj); // True
console.log(arr == arr); // True

// **** Strict equality ****
console.log("123" === 123); // False
console.log(undefined === null); // False
console.log(false === 0); // False
console.log(NaN === false); // False
console.log(NaN === NaN); // False
console.log([1, 2, 3] === "1,2,3"); // False
console.log("abc" === "abc"); // True
console.log({} === {}); // False
console.log([] === []); // False
console.log(obj === obj); // True
console.log(arr === arr); // True
