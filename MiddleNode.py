class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head=ListNode(1)
head.next=ListNode(20)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(35)

def printlist(head):
    curr=head
    while(curr != None):
        print(curr.val,end="->")
        curr=curr.next

def middlenode(head):
    curr = head
    count = 0
    while(curr):
        count=count+1
        curr=curr.next

    ans = int((count / 2) )

    l=[]
    c = 0
    curr=head

    while curr:
        if c == ans:
            return curr  # Return the head of the middle linked list
        c += 1
        curr = curr.next

    return l


ans=middlenode(head)
printlist(ans)