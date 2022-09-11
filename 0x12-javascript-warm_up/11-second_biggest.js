#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2);
  args.sort(function (a, b) { return a - b; });
  args.reverse();
  console.log(args[1]);
}
