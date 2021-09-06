class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        max_ = releaseTimes[0]
        max_key = keysPressed[0]
        for i, key in enumerate(keysPressed):
            delta = releaseTimes[i] - releaseTimes[i-1]
            if delta > max_:
                max_ = delta
                max_key = key
            elif delta == max_ and ord(key) > ord(max_key) :
                max_key = key
        return max_key
