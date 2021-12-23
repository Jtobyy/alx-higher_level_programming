#!/usr/bin/node

exports.logMe = function (item) {
  if (global.i == null) global.i = 0;
  else global.i += 1;
  console.log(global.i + ':' + item);
};
