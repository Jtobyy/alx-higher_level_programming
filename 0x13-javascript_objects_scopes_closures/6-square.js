#!/usr/bin/node
const pSquare = require('./5-square');

module.exports = class Square extends pSquare {
  charPrint (c) {
    if (c == null) super.print();
    else {
      let i = 0;
      while (i < this.height) {
        console.log(c.repeat(this.width));
        i++;
      }
    }
  }
};
