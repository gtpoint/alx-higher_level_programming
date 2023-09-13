#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 1; i < list.length / 2; i++)
    [list[i]] = [list[list.length - i]];
  return list;
}
