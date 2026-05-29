'''
Minimum Genetic Mutation

https://leetcode.com/explore/featured/card/leetcodes-interview-crash-course-data-structures-and-algorithms/707/traversals-trees-graphs/4636/

A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

Example 1:

    Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
    Output: 1

Example 2:

    Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
    Output: 2

'''
from collections import deque
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        def get_all_mutations(node):
            ans = []
            for change in "ACGT":
                for i in range(len(node)):                                
                    mutation = node[:i]+ change +node[i+1:]
                    ans.append(mutation)            
            return ans
        
        queue = deque()
        queue.append((startGene,0))
        seen = set()
        set_bank = set(bank)
        seen.add(startGene)

        while queue:
            (mutation,steps) = queue.popleft() 
            if mutation == endGene:
                return steps
            
            for next_mutation in get_all_mutations(mutation):
                if  next_mutation in set_bank and next_mutation not in seen:
                    seen.add(next_mutation)
                    queue.append((next_mutation,steps+1))
        return -1


startGene = "AACCGGTT"
endGene = "AAACGGTA"
bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
sol = Solution()
res = sol.minMutation(startGene,endGene,bank)
print(res)
