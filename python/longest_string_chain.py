class Solution:
    def longestStrChain(self, strings: List[str]) -> int:
        strings.sort(key=len)
        dp = {}  # string => (next string in chain, total length)

        # compute longest chain
        for string in strings:
            for index in range(len(string)):
                small_string = string[0:index] + string[index + 1:len(string)]
                candidate = ("", 1)
                if small_string in dp:
                    candidate = (small_string, dp[small_string][1] + 1)
                if string in dp:
                    if dp[string][1] < candidate[1]:
                        dp[string] = candidate
                else:
                    dp[string] = candidate

        current_string = max(dp, key=lambda string: dp[string][1])
        return dp[current_string][1]
