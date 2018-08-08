// var snap7 = require('node-snap7');

// var s7client = new snap7.S7Client();
// function readData(index, resolve, reject) {
//     s7client.ABRead(0, index, function(err, res) {
//         if(err)
//             return console.log(' >> ABRead failed. Code #' + err + ' - ' + s7client.ErrorText(err));

//         // ... and write it to stdout
//         console.log(res)
//         console.log(x)
//         x=20;
//         glv['bien' + index] = res;
//         resolve(res);
//     });
// }
// console.log(x)

// s7client.ConnectTo('192.168.1.12', 0, 1, function(err) {
//     if(err)
//         return console.log(' >> Connection failed. Code #' + err + ' - ' + s7client.ErrorText(err));

//     var p1 = new Promise(function(resolve, reject) {
//         readData(1, resolve, reject);
//     }).then(function(result) {
//         new Promise((resolve, reject) => {
//             readData(2, resolve, reject);
//         });
//     }).then(function(result) { // (**)
//         new Promise((resolve, reject) => {
//             readData(3, resolve, reject);
//         });
//     });


// });

var glv = {
    var1: 0,
    var2: 0,
    var3: 0,
    success: false
};
var x = 0;
var isEmited = false;

function emit() {
    if (!isEmited && glv.success && x) {
        console.log('x emit emit emit', glv, x);
        isEmited = true;
    }
}

new Promise(function(resolve, reject) {
        setTimeout(() => {
            glv.var1 = 1;
            resolve(glv.var1);
        }, 1000);
    }).then(function(result) {
        console.log(result); // 1
        return new Promise((resolve, reject) => { // (*)
            setTimeout(() => {
                glv.var2 = result * 2;
                resolve(glv.var2);
            }, 1000);
        });
    }).then(function(var2) { // (**)
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                glv.var3 = var2 * 2;
                resolve(glv.var3);
            }, 1000);
        });
    }).then(function(result) {
        console.log(result); // 4
        console.log('glv', glv, x);
        glv.success = true;
    });


new Promise(function(resolve, reject) {
        setTimeout(() => {
            x = 10;
            resolve(x);
        }, 1000);
    }).then(function(result) {
        console.log(result); // 1
        console.log('x', glv, x);
        console.log('x emit emit emit', glv, x);
        
    });

// sopcet

console.log('abdc');