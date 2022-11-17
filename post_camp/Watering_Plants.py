class Solution:
    
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        total_steps = 0
        pre_sum = 0
        for idx,num in enumerate(plants):
            pre_sum += num
            if pre_sum > capacity:
                pre_sum = num
                total_steps += 2*idx
            total_steps += 1
        return total_steps
        