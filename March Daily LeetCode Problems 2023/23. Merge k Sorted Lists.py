class Solution:
    def mergeKLists(self, lists):
        n = len(lists)
        heap = []

        pointer = []
        for i in range(n):
            pointer.append(lists[i])

            if lists[i] is not None:
                heapq.heappush(heap, (lists[i].val, i))

        sen = ListNode(-1)
        current = sen

        while len(heap) > 0:
            _, index = heapq.heappop(heap)
            p = pointer[index]

            if p.next is not None:
                heapq.heappush(heap, (p.next.val, index))
            current.next = p
            current = current.next
            pointer[index] = pointer[index].next
            current.next = None
        return sen.next