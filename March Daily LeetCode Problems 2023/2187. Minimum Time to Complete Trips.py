class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        r = min(
            time) * totalTrips + 1  # This is the worst case answer possible for any case. Could use big values like 10^15 as well but they might slow the time down for smaller cases.
        l = 0
        ans = 0

        def check_status(expected_time: int) -> int:
            nonlocal ans
            count = 0
            for i in time:
                count += expected_time // i  # Total trips with time expected_time should be integer part of expected_time // i
            if count < totalTrips:
                return 1  # Since number of trips are less then required, left moves to mid
            elif count >= totalTrips:
                ans = expected_time  # stores the latest result. This is guaranteed to be the minimum possible answer.
                return -1  # Since number of trips are greater/equal to required, right moves to mid

        while l < r - 1:  # Till Binary Search can continue.
            mid = (l + r) // 2  # mid is the current expected time.
            status = check_status(
                mid)  # The return values 1/-1 in check_status function determines which pointer to move.
            if status == 1:
                l = mid
            else:
                r = mid

        return ans