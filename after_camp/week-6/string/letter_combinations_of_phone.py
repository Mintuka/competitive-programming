class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        graph = defaultdict(list)
        graph['2'] = ['a','b','c']
        graph['3'] = ['d','e','f']
        graph['4'] = ['g','h','i']
        graph['5'] = ['j','k','l']
        graph['6'] = ['m','n','o']
        graph['7'] = ['p','q','r','s']
        graph['8'] = ['t','u','v']
        graph['9'] = ['w','x','y','z']

        #[a] [b] [c]
        #[ad] [ae] [af] [bd] be bf cd ce cf

        combinations = [[]]
        for digit in digits:

            current = [comb for comb in combinations]
            combinations = [[*[char_comb for char_comb in comb],char] for char in graph[digit] for comb in current]

        return ["".join(comb) for comb in combinations if comb]