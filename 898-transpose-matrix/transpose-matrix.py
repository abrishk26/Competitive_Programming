class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        temp = []
        for j in range(len(matrix[0])):
            temp.append([])

        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                temp[i].append(matrix[j][i])
                

        return temp
            

        