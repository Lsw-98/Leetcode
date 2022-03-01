from asyncio.windows_events import NULL
from lib2to3.pytree import Node


def copyRandomList(head):
  if not head:
    return 
  dic = {
    
  }

  cur = head
  while cur:
    dic[cur] = Node(cur.val)
    cur = cur.next
  cur = head
  while cur:
    dic[cur].next = dic.get(cur.next)
    dic[cur].random = dic.get(cur.random)
    cur = cur.next
  return dic[head]