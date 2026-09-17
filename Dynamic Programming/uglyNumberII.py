class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <= 5:
            return n

        uglies = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}
        idx = [(3, 2), (2, 3), (2, 5)]

        for i in range(6, n + 1):
            small = min(range(3), key=lambda j: uglies[idx[j][0]] * idx[j][1])
            candidate = uglies[idx[small][0]] * idx[small][1]
            uglies[i] = candidate

            for j in range(3):
                if uglies[idx[j][0]] * idx[j][1] == candidate:
                    idx[j] = (idx[j][0] + 1, idx[j][1])

        return uglies[n]