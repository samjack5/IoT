const express = require('express');
const app = express();
const Gpio = require('onoff').Gpio; // Módulo para controlar GPIO en Raspberry Pi

const ledVerde = new Gpio(17, 'out'); // Pines GPIO para los LEDs
const ledAmarillo = new Gpio(18, 'out');
const ledRojo = new Gpio(27, 'out');

app.use(express.static('public'));

app.get('/encender/:color', (req, res) => {
  const color = req.params.color;
  let led;

  switch (color) {
    case 'verde':
      led = ledVerde;
      break;
    case 'amarillo':
      led = ledAmarillo;
      break;
    case 'rojo':
      led = ledRojo;
      break;
    default:
      res.send('Color no válido');
      return;
  }

  led.writeSync(1); // Enciende el LED
  res.send(`Encendiendo LED ${color}`);
});

app.get('/apagar/:color', (req, res) => {
  const color = req.params.color;
  let led;

  switch (color) {
    case 'verde':
      led = ledVerde;
      break;
    case 'amarillo':
      led = ledAmarillo;
      break;
    case 'rojo':
      led = ledRojo;
      break;
    default:
      res.send('Color no válido');
      return;
  }

  led.writeSync(0); // Apaga el LED
  res.send(`Apagando LED ${color}`);
});

app.listen(3000, () => {
  console.log('Servidor escuchando en http://localhost:3000');
});
