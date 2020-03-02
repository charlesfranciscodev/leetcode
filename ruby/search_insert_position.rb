# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search_insert(nums, target)
  prev_val = nil
  index = 0
  nums.each do |num|
      return index if target <= num
      index += 1
  end
  index
end
