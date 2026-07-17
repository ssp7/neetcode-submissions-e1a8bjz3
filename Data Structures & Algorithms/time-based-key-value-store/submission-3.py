class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        entry = [value, timestamp]
        if not key in self.map:
            self.map[key] = [entry]
        else:
            self.map[key].append(entry)

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.map:
            return ""

        values = self.map[key]
        valForGet = ""

        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            val, prevTime = values[mid]
            if prevTime > timestamp:
                r = mid - 1
            elif prevTime <= timestamp:
                valForGet = val
                l = mid + 1
            
        return valForGet
        

        
