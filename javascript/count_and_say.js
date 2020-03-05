/**
 * @param {number} n
 * @return {string}
 */

let countAndSay = function(n) {
  let term = "1";
  while (n > 1) {
      let current_digit = '';
      let current_count = 0;
      let next_term = "";
      for (let i = 0; i < term.length; i++) {
          let digit = term[i];
          if (current_count === 0) {
              current_digit = digit;
              current_count++;
          } else if (digit === current_digit) {
              current_count++;
          } else {
              next_term += current_count.toString() + current_digit;
              current_digit = digit;
              current_count = 1;
          }
      }
      next_term += current_count.toString() + current_digit;
      term = next_term;
      n--;
  }
  return term;
};
