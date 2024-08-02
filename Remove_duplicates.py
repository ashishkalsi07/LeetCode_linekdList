class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

def printlist(head):
    cur = head
    l = []
    while cur:
        l.append(cur.val)
        cur = cur.next
    return l

head = ListNode(10)
head.next = ListNode(15)
head.next.next = ListNode(15)
head.next.next.next = ListNode(20)
head.next.next.next.next = ListNode(20)


head = deleteDuplicates(head)

print(printlist(head)) 
