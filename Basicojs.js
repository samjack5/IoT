
//* 
//basico de javascript IoT
//TIPOS DE VARIABLES
const msg="el mensaje"; //CONST varible constante yno se puede cambiar /variable global 
var msg2="el menasje 2"; //VAR variable globar que puede ser  cambiada 
let msg3="el mensaje 3"; //LET para variables globales que pueden ser cambiadas

const led_verde=LED(14)

//para escribir una funcion: 
function encenderLed(msg){
           console.log(msg)
}

//como funcionan los print de tipo F
//se utiliza el slahs para poder escribir el mensaje
console.log(`el mensaje es ${msg}`)

//contadores 
var contador=0; 
function IncrementarConteo(contador){
    contador+=1;
    console.log(`el contador es ${contador}`)    
}

//tambien nos sirven para imprimir variables_
"este es un String"
'Este es otro String'
`Este es String`

//condicional if 
// !== exactamente diferentes
// === exactamente iguales
// == casi iguales
// != casi diferentes
// < menor que
// > mayor que
// <= menor o igual que
// >= mayor o igual que
// && and
// || or
// ! not  
let numero=1;
if(numero === 1){
    console.log("el numero es 1") 
}else{
 cononcole.log("el numero no es 1")
}

//ciclos for
let Arreglo= [1,2,3,4,5,6,7,8,9,10];
Arreglo.forEach((numero)=> console.log(numero*numero)

Arreglo.forEach((numero)=> {
    let cuadrado= numero*numero
    console.log(cuadrado)}
})