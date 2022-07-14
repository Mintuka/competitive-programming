class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #brutforce
        #check if each subarray of s is equal to t costs n**2
        
        #optitmize
        #map count of t characters
        #save count of all characters on variable t_chars_count
        #iterate from 0 to n until char in t is found assign that index to left
        #iterate the right pointer until you find the char on left
        #repeat line 9 and 10 until you reach end of the string
        
        t_chars = Counter(t)
        t_chars_count,size = len(t),len(s)
        left,right = 0,0
        min_window = (0,10**6)
        prev_window = inf
        
        while right < size:
            
            char = s[right]
            if char in t_chars:
                t_chars[char] -= 1
                if t_chars[char] >= 0:
                    t_chars_count -= 1
            
            while t_chars_count == 0:
                
                curr_window = right - left
                if curr_window < prev_window:
                    min_window = (left,right)
                
                char = s[left]
                if char in t_chars:
                    t_chars[char] += 1
                    if t_chars[char] > 0:
                        t_chars_count += 1

                left += 1   
                prev_window = min(prev_window,curr_window)
                
            right += 1
    
        left,right = min_window
        
        return s[left:right+1] if right != 10**6 else ""