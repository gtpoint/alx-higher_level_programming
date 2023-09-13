#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((acc, current) => current === searchElement ? acc + 1 : acc, 0);
};
