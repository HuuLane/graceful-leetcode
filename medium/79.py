class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word, 0):
                    return True
        return False

    def helper(self, board, i, j, word, wordIndex) -> bool:
        if len(word) == wordIndex:
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            # out of boundary
            return False

        if board[i][j] != word[wordIndex]:
            return False
        else:
            # lock it, cuz "The same letter cell may not be used more than once."
            board[i][j] = '#'

        # recursively find
        found = self.helper(board, i + 1, j, word, wordIndex + 1) \
            or self.helper(board, i - 1, j, word, wordIndex + 1) \
            or self.helper(board, i, j + 1, word, wordIndex + 1) \
            or self.helper(board, i, j - 1, word, wordIndex + 1) \

        # release lock
        board[i][j] = word[wordIndex]
        return found
