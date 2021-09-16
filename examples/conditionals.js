// ***** Using booleans *****
if (true) {
    // This will print
    console.log(0);
  }
  
  if (false) {
    console.log(1);
  }
  
  // ***** Truthy and Falsy *****
  if (0) {
    console.log(2);
  }
  
  if (1) {
    // This will print
    console.log(3);
  }
  
  if (undefined) {
    console.log(4);
  }
  
  if (NaN) {
    console.log(5);
  }
  
  if (!NaN) {
    // This will print
    console.log(6);
  }
  
  // ***** Equality Check *****
  if (NaN == NaN) {
    console.log(7);
  }
  
  if (123 == "123") {
    // This will print
    console.log(8);
  }
  
  if (123 === "123") {
    console.log(9);
  }
  
  // ***** Else If ******
  if (true) {
    // This will print
    console.log(10);
  } else if (true) {
    console.log(11);
  }
  
  if (false) {
    console.log(12);
  } else if (false) {
    console.log(13);
  } else if (true) {
    // This will print
    console.log(14);
  } else if (false) {
    console.log(15);
  }
  
  // ***** Else ******
  if (false) {
    console.log(16);
  } else if (false) {
    console.log(17);
  } else {
    // This will print
    console.log(18);
  }
  