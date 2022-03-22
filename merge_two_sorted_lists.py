"""
71 ms, faster than 15.89% of Python3 online submissions (bad)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_list(ln):
    head = ln
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
def from_list(list_input):
    ln = None
    if list_input:
        ln = ListNode()
        head = ln
    while list_input:
        head.val = list_input.pop(0)
        if list_input:
            head.next = ListNode()
            head = head.next
    return ln


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        hl1 = list1
        hl2 = list2
        if hl1 or hl2:
            rl = ListNode()
        else:
            return None
        rhead = rl
        q0 = []
        while hl1 or hl2:
            buff = []
            if hl1:
                buff.append(hl1.val)
                hl1 = hl1.next
            if hl2:
                buff.append(hl2.val)
                hl2 = hl2.next
            q0 += buff
            q0.sort()
        while q0:
            rl.val = q0.pop(0)
            if q0:
                rl.next = ListNode()
                rl = rl.next
        return rhead


ln = ListNode(1)
ln.next = ListNode(2)
ln.next.next = ListNode(3)
assert to_list(ln) == [1,2,3]

result = to_list(from_list([1,2,3,4,5]))
assert result == [1,2,3,4,5]

s = Solution()    
if 1:
    ln0 = from_list([1,2,4])
    ln1 = from_list([1,3,4])
    result = to_list(s.mergeTwoLists(ln0, ln1))
    assert result == [1,1,2,3,4,4]

    ln0 = from_list([])
    ln1 = from_list([])
    result = to_list(s.mergeTwoLists(ln0, ln1))
    assert result == []

    ln0 = from_list([])
    ln1 = from_list([0])
    result = to_list(s.mergeTwoLists(ln0, ln1))
    assert result == [0]

if 1:
    ln0 = from_list([5])
    ln1 = from_list([1,2,4])
    result = to_list(s.mergeTwoLists(ln0, ln1))
    assert result == [1,2,4,5]


if 1:
    ln0 = from_list([1])
    ln1 = from_list([])
    result = to_list(s.mergeTwoLists(ln0, ln1))
    assert result == [1]

print("All good")