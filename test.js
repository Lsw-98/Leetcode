let reg = /^[0-9]\d*$|^0$/;
console.log(reg.test("123456")) //true
console.log(reg.test("123456##")) //false