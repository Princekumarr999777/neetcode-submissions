class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        mapping_dictionary={}

        for i in range( len(strs)):
            sorted_str= "".join(sorted(strs[i]))
            if sorted_str in mapping_dictionary:
                mapping_dictionary[sorted_str].append(strs[i])
            else:
                mapping_dictionary[sorted_str]=[(strs[i])]
        result=list(mapping_dictionary.values())

        return result
        

        