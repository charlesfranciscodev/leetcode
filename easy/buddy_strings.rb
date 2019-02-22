require 'set'

# @param {String} a
# @param {String} b
# @return {Boolean}
def buddy_strings(a, b)
    return false if a.length != b.length
    return false if a.empty?
    if a == b
        set = Set.new()
        for i in 0..(a.length - 1)
            c = a[i]
            if set.include?(c)
               return true 
            end
            set.add(c)
        end
        return false
    else
        pairs = []
        for i in 0..(a.length - 1)
            x = a[i]
            y = b[i]
            pairs.push([x, y]) if x != y
            return false if pairs.length >= 3
        end
        return pairs.length == 2 && pairs[0].eql?(pairs[1].reverse)
    end
end
