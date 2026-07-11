class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #use stack to solve8
        #first zip position and speed, sort by position
        fleet_count = 1
        #if A is behind B, yet travel time is quicker, 
        combined_list = list(zip(position, speed))
        combined_list.sort()
        combined_list.reverse()
        stack = []
        for car in combined_list:
            pos, v = car
            time = (target - pos) / v
            if not stack:
                stack.append(time)
                continue
            
            #if time of current car is longer than previous closer car
            if stack[-1] < time:
                fleet_count += 1
                stack.append(time)
            else:
                continue
        return fleet_count
