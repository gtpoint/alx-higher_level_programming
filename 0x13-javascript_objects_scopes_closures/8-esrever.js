exports.esrever = function (list) {
  return list.reduce((reversedList, current) => {
    reversedList.unshift(current);
    return reversedList;
  }, []);
};
