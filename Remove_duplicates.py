class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def deleteDuplicates(head):
    cur=head
    while cur and cur.next:
        if cur.val == cur.next.val:
            cur.next=cur.next.next
        else:
            cur=cur.next
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
