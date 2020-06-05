from itertools import cycle


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h = len(matrix)
        if h == 0:
            return []
        w = len(matrix[0])
        ans = []

        def directions():
            for direction in cycle(('right', 'down', 'left', 'up')):
                yield direction

        go = {
            'right': lambda i, j: (i, j + 1),
            'down': lambda i, j: (i+1, j),
            'left': lambda i, j: (i, j - 1),
            'up': lambda i, j: (i - 1, j),
        }

        def readAndMark(i, j):
            val = matrix[i][j]
            matrix[i][j] = '#'
            return val

        def validate(step):
            '''out of border or hitting the wall'''
            x, y = step
            return not (x < 0 or x == h or y < 0 or y == w or matrix[x][y] == '#')

        # curr position
        i = j = 0
        d = directions()
        direction = next(d)
        while True:
            nextStep = go[direction](i, j)
            if validate(nextStep):
                ans.append(readAndMark(i, j))
                i, j = nextStep
            else:
                # Make a turn
                direction = next(d)
                nextStep = go[direction](i, j)
                if validate(nextStep):
                    ans.append(readAndMark(i, j))
                    i, j = nextStep
                else:
                    # end
                    ans.append(readAndMark(i, j))
                    break
        return ans
