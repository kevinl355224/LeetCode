class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Initialize
        topDic = {}
        bottomDic = {}
        repeat = {}
        length = len(tops)
        minRotate = -1
        for n in range(1,7):
            topDic[n]= 0
            bottomDic[n] = 0
            repeat[n] = 0
        # Map the number
        for n in range(length):
            topDic[tops[n]] += 1
            bottomDic[bottoms[n]] += 1     
            if tops[n] == bottoms[n]:
                repeat[tops[n]] += 1
        # Analyze
        for n in range(1,7):
            # print(f"n: {n} , top: {topDic[n]}, bottom: {bottomDic[n]}, repeat: {repeat[n]}, length: {length}")
            if topDic[n] + bottomDic[n] - repeat[n] == length:
                minRotate = min(length - topDic[n], length - bottomDic[n])

        # print(topDic)
        # print(bottomDic)
        if minRotate >= 0 :
            return minRotate
        else:
            return -1 
