class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        websites_visited = defaultdict(list)
        triplets = defaultdict(int)
        max_triplet = None
        n = len(username)
        for i in range(n):
            websites_visited[username[i]].append((timestamp[i], website[i]))
        
        for user, visits in websites_visited.items():
            websites = sorted(visits)
            w = len(websites)
            user_triplets = set()
            for i in range(w):
                for j in range(i+1, w):
                    for k in range(j+1, w):
                        triplet = (websites[i][1], websites[j][1], websites[k][1])
                        user_triplets.add(triplet)
            
            for triplet in user_triplets:
                triplets[triplet] += 1
                if (
                    (not max_triplet) or
                    (triplets[triplet] > triplets[max_triplet]) or
                    (triplets[triplet] == triplets[max_triplet] and triplet < max_triplet)
                ):
                    max_triplet = triplet
        
        return max_triplet