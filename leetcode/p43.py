class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = self.get_num(num1)
        n2 = self.get_num(num2)

        product = n1 * n2
        #return str(product)

        result = []
        while True:
            result.append(chr(ord("0") + (product % 10)))
            product //= 10
            if product == 0:
                break

        return "".join(result[::-1])

    def get_num(self, num):
        result = 0
        power = 1
        for n in num[::-1]:
            result += (ord(n) - ord("0")) * power
            power *= 10
        return result

print(Solution().multiply("2", "3"))
print(Solution().multiply("123", "456"))
print(Solution().multiply("123", "0"))
