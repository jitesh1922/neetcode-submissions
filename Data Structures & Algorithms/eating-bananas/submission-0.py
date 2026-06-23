class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def possible( piles, h, n):
            temp = piles
            i = 0
            while h>0 and i < len(temp):
                temp[i] -= n
                if temp[i]<=0:
                    i +=1
                h -= 1
            if i == len(temp):
                return True
            else:
                return False
        
        def possible2( piles, h, n):
            reqH =0
            for i in piles:
                reqH += math.ceil(i/n)
            
            if reqH <= h:
                return True
            else:
                False

        end = max(piles)
        start = int(math.ceil(sum(piles)/h))
        prev = end
        while start<=end:
            mid = int((start+end)/2)
            yes = possible2(piles, h, mid)
            if yes:
                prev = mid
                end = mid-1
            else:
                start = mid+1
            
        return prev
