#!/usr/bin/node
const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor(w, h, size){
    super(w, h);
    this.size = size;
  }
}
