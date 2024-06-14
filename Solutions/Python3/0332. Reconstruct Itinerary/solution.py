class Solution(object):
    def findItinerary(self, tickets):
        go_to_places = {}
        for start, finish in sorted(tickets):
            if go_to_places.get(start) is None:
                go_to_places[start] = []
            go_to_places[start].append(finish)
        
        route = []
        stack = ["JFK"]

        while stack:
            while stack[-1] in go_to_places and go_to_places[stack[-1]] != []:
                next_airport = go_to_places[stack[-1]].pop(0)
                stack.append(next_airport)
            route.append(stack.pop())

        return route[::-1]