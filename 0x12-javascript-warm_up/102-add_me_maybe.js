#!/usr/bin/node
exports.addMeMaybe = function (number, theFunction) {
  theFunction.call(this, number + 1);
};
