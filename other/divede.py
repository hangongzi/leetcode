class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MIN_INT, MAX_INT = -2147483648, 2147483647
        dividend_, flag_divident = abs(dividend), dividend>0
        divisor_, flag_divisor = abs(divisor), divisor>0
        def div(dividend, divisor):
            if dividend<divisor:
                return 0
            cur = divisor
            multiple = 1
            while cur+cur<dividend:
                cur += cur
                multiple += multiple
            return multiple + div(dividend-cur, divisor)
        ret = div(dividend_, divisor_) if (flag_divident and flag_divisor) \
                                          or (not flag_divisor and not flag_divident) \
            else 0- div(dividend_, divisor_)
        if ret<MIN_INT:
            return MIN_INT
        elif MIN_INT<=ret<=MAX_INT:
            return ret
        else:
            return MAX_INT



    # def divide(self, dividend: int, divisor: int) -> int:
    #     MIN_INT, MAX_INT = -2147483648, 2147483647
    #     ret = 0
    #     dividend_ = abs(dividend)
    #     divisor_ = abs(divisor)
    #     while dividend_ >= divisor_:
    #         cur = divisor_
    #         multiple = 1
    #         while cur+cur < dividend_:
    #             cur += cur
    #             multiple += multiple
    #         dividend_ -= cur
    #         ret += multiple
    #     ret = ret if dividend*divisor>0 else 0-ret
    #     if ret<MIN_INT:
    #         return MIN_INT
    #     elif MIN_INT<ret<MAX_INT:
    #         return ret
    #     else:
    #         return MAX_INT


print(Solution().divide(-2147483648, 1))
