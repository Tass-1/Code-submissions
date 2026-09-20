from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        folders = defaultdict(list) 
        
        for word in strs:
            label = "".join(sorted(word))
            folders[label].append(word) 
            
        return list(folders.values())