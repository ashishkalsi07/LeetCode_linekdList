class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

def printlist(head):
    l=[]
    curr=head
    while(curr != None):
        l.append(curr.val)
        curr=curr.next
    return 
def palindrome(lst):   
    old_list = lst[:] 
    lst.reverse()      
    return lst == old_list


head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(1)
ans=printlist(head)
f_ans=palindrome(ans)
print(f_ans)