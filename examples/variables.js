// ***** var *****

function test() {
    //Output: undefined
    console.log(a);

    var a = 'hello';

    // Output: 'hello'
    console.log(a);

    if(true){
        var a = 'world';
    }

    // Output: 'world'
    console.log(a);
}
test();

if(true){
// Defined on global scope
    var b = 'haha';
}

// Output: 'haha'
console.log(b);
  
// ***** let and const *****
  
function test2() {
    // ReferenceError: Cannot access 'd' before initialization 
    console.log(d);
    let d = 'nice';

    // Output: 'nice'
    console.log(d);

    if(true){
        let d = 'popcorn';
    }

    // Output: 'nice'
    console.log(d);

    const e = 'not reassignable'

    // TypeError: Assignment to constant variable
    e = 'nice try!';
}
test2();

if(true){
    const c = 'no';
}

// ReferenceError: c is not defined
console.log(c);
