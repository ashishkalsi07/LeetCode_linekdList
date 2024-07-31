class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head=ListNode(10)
head.next=ListNode(12)
head.next.next=ListNode(14)
head.next.next.next=ListNode(16)
head.next.next.next.next=ListNode(18)

head1=ListNode(1)
head1.next=ListNode(12)
head1.next.next=ListNode(3)
head1.next.next.next=ListNode(14)
head1.next.next.next.next=ListNode(5)
Finallist=[]
def traverselist(head):
    curr=head
    
    while curr!= None:
        Finallist.append(curr.val)
        curr=curr.next

def list_to_linkedlist(lst):
    if not lst:  # If the list is empty, return None
        return None
    
    # Create the head of the linked list
    head = ListNode(lst[0])
    current = head
    
    # Iterate through the list and create the linked list
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def printlist(head):
    curr=head
    while(curr != None):
        print(curr.val,end="->")
        curr=curr.next

traverselist(head)
traverselist(head1)
print(Finallist)
Finallist.sort()
print(Finallist)
heaad=list_to_linkedlist(Finallist)
printlist(heaad)