let acumulador=0; 

console.time("for");
for(let i=0; i<5000; i++){
    acumulador=acumulador+1;
}
console.timeEnd("for");
console.log("el resultado del acumulador es: "+acumulador);

