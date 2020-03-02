# @param {Integer} num
# @return {Boolean}
def is_power_of_four(num)
  return false if num <= 0
  exponent = (Math.log(num) / Math.log(4)).to_i
  return num == 4 ** exponent
end
