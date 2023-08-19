class Solution:
    def mySqrt(self, x: int) -> int:
        print("Value of x: ", x)
        if x == 1:
            return 1
        else:
            counter = 0
            result = 0
            while result <= x:
                counter +=1
                result = counter * counter
            return (counter+counter-1)//2

result = Solution()
print("Sqaure root result: ", result.mySqrt(4))
print("Sqaure root result: ", result.mySqrt(8))
