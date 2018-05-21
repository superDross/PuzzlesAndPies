''' LeetCode 2

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

def addTwoNumbers(l1, l2):
    node1 = l1
    node2 = l2
    list1 = []
    list2 = []
    while node1 is not None:
        list1.append(node1.val)
        node1 = node1.next
    while node2 is not None:
        list2.append(node2.val)
        node2 = node2.next
    convert1 = int(''.join([str(x) for x in list1[::-1]]))
    convert2 = int(''.join([str(x) for x in list2[::-2]]))
    strlist = list(str(convert1+convert2))[::-1]
    return [int(x) for x in strlist]
