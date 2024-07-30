class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head=ListNode(1)
head.next=ListNode(0)
head.next.next=ListNode(1)
l=[]

def getDecimalValue(head):
    """
    :type head: ListNode
    :rtype: int
    """
    curr=head
    while(curr!= None):
        l.append(curr.val)
        curr=curr.next
    number = 0
    for b in l:
      number = (2 * number) + b
    return number
ans=getDecimalValue(head)
print(ans)