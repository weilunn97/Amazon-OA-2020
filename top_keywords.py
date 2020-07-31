from heapq import heappop, heapify
from typing import List


def top_keywords(kw: List[str], reviews: List[str], k: int) -> List[str]:
    """
    Time  : O()
    Space : O()
    """
    # CONVERT KEYWORDS INTO SET
    kw = set([k.lower() for k in kw])

    # SETUP A COUNT OF THE KEYWORDS
    kw_count = {k: 0 for k in kw}

    # PROCESS EACH REVIEW
    for r in reviews:
        process_review(r, kw_count)

    kws = [(-count, kw) for kw, count in kw_count.items()]
    heapify(kws)
    return [heappop(kws)[1] for _ in range(k)]


def process_review(r: str, kw_count: dict):
    processed = set()
    r = r.lower()
    r = ''.join([char for char in r if char.isalnum() or char == ' '])
    for word in r.split(' '):
        if word not in processed:
            if kw_count.get(word) is not None:
                kw_count[word] += 1
            processed.add(word)


if __name__ == "__main__":
    print(top_keywords(["anacell", "cetracular", "betacellular"],
                       ["Anacell provides the best services in the city",
                        "betacellular has awesome services",
                        "Best services provided by anacell, everyone should use anacell"],
                       2) == ["anacell", "betacellular"])

    print(top_keywords(["anacell", "betacellular", "cetracular", "deltacellular", "eurocell"],
                       ["I love anacell Best services; Best services provided by anacell",
                        "betacellular has great services",
                        "deltacellular provides much better services than betacellular",
                        "cetracular is worse than anacell",
                        "Betacellular is better than deltacellular."],
                       2) == ["betacellular", "anacell"])
