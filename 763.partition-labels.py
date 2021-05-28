#
# @lc app=leetcode id=763 lang=python3
#
# [763] Partition Labels
#

# The idea of this solution is greedily construct our partition, let us consider the example
# S = ababcbacdefegdehijhklij. We need to start with letter a and we can not stop, until we reach the last occurence of a: so, we need to take ababcba part at least. But if we take this part, we need to consider letters b and c as well and also traverse our string until we meet the last occurence of these letters, so we need to take ababcbac. Here we can stop, because we already take into account all symbols inside this string. So, we go to the next symbol and repeat our partition. So, what we have in my code:

#     First, we need to know all ends for each letter in advance, I call it ends.
#     Also, curr is current index and last is index we need to traverse until. For each group of symbols we need to do: last = ends[S[curr]]: we find the place we need to traverse; while we do no reach this place, we look at the next symbol and update our last. So, we stop, when curr become greater than last.
#     We add curr to our out result.
#     Note, that we need to have [8,7,8] for our example, but we get [8,15,23], places where our partitions are. So, we evaluate differences 8-0, 15-8, 23-15 and return them.

# Complexity: time complexity is O(n), we traverse our string twice: one time when we evaluate ends and second time when we do partitions. Space complexity is O(26): to keep our ends (also we have answer, but it can not be greater than 26 as well).


# @lc code=start

from collections import defaultdict
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c: i for i, c in enumerate(S)}
        curr, out = 0, [0]

        while curr < len(S):
            highest = last[S[curr]]
            while curr <= highest:
                char = S[curr]
                highest = max(highest, last[char])
                curr += 1 
            out.append(curr)
        
        return [out[i] - out[i-1] for i in range(1, len(out))]

        
# @lc code=end

