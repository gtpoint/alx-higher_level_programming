#!/usr/bin/node
if (process.argv.length < 3) {
  console.log(0);
} else {
  let nb_sec_max = process.argv.slice(2).sort()[process.argv - 4];
  console.log(nb_sec_max);
}
