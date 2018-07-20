# Code referenced from https://www.packtpub.com/big-data-and-business-intelligence/text-processing-using-nltk-python-video
class EditDistance:
    def __init__(self):
        pass

    def calculate(self, string1, string2):
        m = len(string1) + 1
        n = len(string2) + 1

        table = {}
        for i in range(m): table[i,0] = i
        for j in range(n): table[0,j] = j

        for i in range(1, m):
            for j in range(1, n):
                cost = 0 if string1[i-1] == string2[j-1] else 1
                table[i,j] = min(table[i,j-1] + 1, table[i-1,j] + 1, table[i-1,j-1]+cost)

        return table[i,j]