from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # sorting + hashmap solution
        # groups = defaultdict(list)

        # for word in strs:
        #     key = "".join(sorted(word))
        #     groups[key].append(word)
        
        # return list(groups.values())

        # fixed-length array + hashmap solution
        groups = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord('a') - ord(char)] += 1
            groups[tuple(count)].append(word)
        
        return list(groups.values())
