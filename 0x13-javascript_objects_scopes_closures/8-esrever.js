exports.esrever = function (list) {
  return list.map((el, index, arr) =>{
    return arr[list.length - 1 - index]
  })
};
