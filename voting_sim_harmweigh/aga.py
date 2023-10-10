import random
from statistics import harmonic_mean

class Voter:
    def __init__(self, region, mvcoValue, position):
        self.region = region
        self.mvcoValue = mvcoValue
        self.position = position
    
    def cast_vote(self, candidates, votes):
        candidate_options = list(candidates.keys())
        random.shuffle(candidate_options)
        for i in range(3):
            if random.random() < self.mvcoValue / 100:
                candidate = max(candidate_options, key=lambda x: candidates[x].popularity)
            else:
                candidate = candidate_options[i]
            votes[candidate][self.region][i] += 1

class Candidate:
    def __init__(self, name, popularity, position):
        self.name = name
        self.popularity = popularity
        self.position = position

def election():
    candidates = {
        "A": Candidate("A", random.randint(1, 100), 3),
        "B": Candidate("B", random.randint(1, 100), 2),
        "C": Candidate("C", random.randint(1, 100), 1)
    }

    votes = {
        "A": {"North": [0, 0, 0], "South": [0, 0, 0], "East": [0, 0, 0], "West": [0, 0, 0], "Center": [0, 0, 0]},
        "B": {"North": [0, 0, 0], "South": [0, 0, 0], "East": [0, 0, 0], "West": [0, 0, 0], "Center": [0, 0, 0]},
        "C": {"North": [0, 0, 0], "South": [0, 0, 0], "East": [0, 0, 0], "West": [0, 0, 0], "Center": [0, 0, 0]}
    }

    regions = ["North", "South", "East", "West", "Center"]

    num_voters = 100  #adjust number of voters

    for _ in range(num_voters):
        region = random.choice(regions)
        mvcoValue = random.randint(1, 100)
        position = random.randint(1, 3)
        voter = Voter(region, mvcoValue, position)
        voter.cast_vote(candidates, votes)

    results = {}
    for candidate in candidates:
        primary_votes = [votes[candidate][region][0] for region in regions]
        secondary_votes = [votes[candidate][region][1] for region in regions]
        tertiary_votes = [votes[candidate][region][2] for region in regions]

        final_votes = [sum(primary_votes), sum(secondary_votes), sum(tertiary_votes)]

        harmonic_mean_score = harmonic_mean(final_votes)
        results[candidate] = {
            "raw_votes": {
                "Primary": primary_votes,
                "Secondary": secondary_votes,
                "Tertiary": tertiary_votes,
            },
            "final_votes": final_votes,
            "harmonic_mean_score": harmonic_mean_score,
        }

    max_harmonic_mean_score = max(results.values(), key=lambda x: x["harmonic_mean_score"])["harmonic_mean_score"]
    winner = [candidate for candidate, data in results.items() if data["harmonic_mean_score"] == max_harmonic_mean_score]

    return results, winner

if __name__ == "__main__":
    election_results, winner = election()

    for candidate, data in election_results.items():
        print(f"Candidate {candidate} - Raw Votes:")
        print(f"  Primary: {data['raw_votes']['Primary']}")
        print(f"  Secondary: {data['raw_votes']['Secondary']}")
        print(f"  Tertiary: {data['raw_votes']['Tertiary']}")
        print(f"Final Votes: {data['final_votes']}")
        print(f"Harmonic Mean Score: {data['harmonic_mean_score']:.2f}")
        print()

    print(f"Winner: {winner}")

input("press anythng to close")
