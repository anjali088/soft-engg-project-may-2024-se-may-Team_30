<template>
    <div class="calculator" v-if="isVisible">
      <div class="display">{{ displayValue }}</div>
      <div class="buttons">
        <button v-for="button in buttons" :key="button" @click="onButtonClick(button)">
          {{ button }}
        </button>
      </div>
      <button class="close" @click="closeCalculator">Close</button>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CalculatorBox',
    data() {
      return {
        isVisible: false,
        displayValue: '0',
        buttons: [
          'MC', 'MR', 'MS', 'M+', 'M-',
          '7', '8', '9', '×', '÷',
          '4', '5', '6', '+', '-',
          '1', '2', '3', '(', ')',
          '0', '.', '+/-', '=', 'C',
          'π', 'e', 'sin', 'cos', 'tan', 'sinh', 'cosh', 'tanh', 'sin⁻¹', 'cos⁻¹', 'tan⁻¹', 'sinh⁻¹', 'cosh⁻¹', 'tanh⁻¹',
          'x²', 'x³', 'xʸ', 'y√x', 'x!', '√', '∛', 'log', 'ln', 'logy(x)', 'eˣ'
        ]
      }
    },
    methods: {
      onButtonClick(button) {
        if (button === 'C') {
          this.displayValue = '0';
        } else if (button === '=') {
          this.calculate();
        } else {
          this.displayValue += button;
        }
      },
      calculate() {
        try {
          this.displayValue = eval(this.displayValue.replace('×', '*').replace('÷', '/'));
        } catch (e) {
          this.displayValue = 'Error';
        }
      },
      openCalculator() {
        this.isVisible = true;
      },
      closeCalculator() {
        this.isVisible = false;
      }
    }
  }
  </script>
  
  <style scoped>
  .calculator {
    position: fixed;
    bottom: 20px;
    right: 20px;
    width: 300px;
    background: #333;
    color: #fff;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
  }
  .display {
    width: 100%;
    background: #000;
    padding: 10px;
    margin-bottom: 10px;
    text-align: right;
    font-size: 2em;
  }
  .buttons {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
  }
  button {
    padding: 20px;
    font-size: 1em;
    background: #444;
    border: none;
    color: #fff;
    border-radius: 5px;
  }
  button.close {
    grid-column: span 5;
    background: red;
  }
  </style>
  