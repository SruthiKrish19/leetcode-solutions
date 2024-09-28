// This is a simple Hello World program. I used this to explore the LeetCode platform.
// This is a simple function call which returns a function which in turn returns the string "Hello World".

// Time complexity: O(1)
// Space complexity: O(1)

var createHelloWorld = function () {
  return function () {
    return "Hello World";
  };
};

const f = createHelloWorld();
console.log(f());
