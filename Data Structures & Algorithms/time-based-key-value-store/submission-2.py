class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append([timestamp, value])
        else:
            self.map[key] = [[timestamp, value]]

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""
        
        values = self.map[key]
        left, right = 0, len(values) - 1

        res = ""
        while left <= right:
            mid = (left + right) // 2
            time, val  = values[mid]

            if time > timestamp:
                right = mid - 1
            elif time <= timestamp:
                res = val
                left = mid + 1

        return res
