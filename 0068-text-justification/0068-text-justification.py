class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res = []
        i = 0
        n = len(words)
        
        while i < n:
            
            j = i
            line_len = 0
            while j < n and line_len + len(words[j]) + (j - i) <= maxWidth:
                line_len += len(words[j])
                j += 1
            
            num_words = j - i
            num_spaces = maxWidth - line_len
            
            
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))
            else:
                
                base_space = num_spaces // (num_words - 1)
                extra_space = num_spaces % (num_words - 1)
                
                parts = []
                for k in range(i, j - 1):
                    parts.append(words[k])
                    
                    parts.append(" " * (base_space + (1 if (k - i) < extra_space else 0)))
                parts.append(words[j - 1])
                line = "".join(parts)
            
            res.append(line)
            i = j
            
        return res