class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        R,C = len(image), len(image[0])
        for row in image:
            i,j = 0, C-1
            while i <= j:
                if row[i] == row[j]:
                    flip = 1-row[i]
                    row[i] = row[j] = flip
                i,j =i+1,j-1
        return image
