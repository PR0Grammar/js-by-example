// Strings
console.log("Strings");
console.log(String(123321));

// Numbers
console.log(123);
console.log(3.14159265);
console.log(Number(123));
console.log(Number("123"));

// BigInt
console.log(10000000000000000000000000000000n);
console.log(BigInt("10000000000000000000000000000000"));

// Booleans
console.log(true);
console.log(false);
console.log(Boolean(true));

// Undefined
console.log(undefined);
let x;
console.log(x);
function emptyArg(a) {
    console.log(a);
}
emptyArg();

// Symbols
console.log(Symbol());
console.log(Symbol("with string"));

// Null
console.log(null);
let y = null;
console.log(y);
