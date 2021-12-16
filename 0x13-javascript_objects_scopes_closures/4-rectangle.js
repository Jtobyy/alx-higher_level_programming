#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i = 0;
    while (i < this.height) {
      console.log('X'.repeat(this.width));
      i++;
    }
  }

  rotate () {
    let temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
  double () {
    this.height = this.height * 2;
    this.width = this.widht * 2;
  }
};
