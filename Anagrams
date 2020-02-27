class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        inp = []
        out = []
        dictionary = {}
        
        # sorting letters of every word in A
        for i in A:
            inp.append(''.join(sorted(i)))
        
        # counting same strings and replacing counted strings with ''
        for i in range(len(inp)):
            if inp[i] == '':
                continue
            dictionary[inp[i]] = [i+1]
            for j in range(i+1, len(inp)):
                if i+1 >= len(inp):
                    break
                if inp[i] == inp[j]:
                    dictionary[inp[i]].append(j+1)
                    inp[j]=''
                
        out = [ v for v in dictionary.values() ]
        return out
