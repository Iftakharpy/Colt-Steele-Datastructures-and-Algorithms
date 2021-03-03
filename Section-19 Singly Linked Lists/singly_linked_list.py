from typing import Union,Optional

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"{self.value}, {self.next}"


class Singly_Linked_List:
    empty_repr = "Empty"
    def __init__(self, value: Optional[Union[int, float, str]] = None) -> None:
        """Initiating the singly linked list"""
        self.head = Node(value)
        self.tail = self.head

        self.length = 0
        if value!=None:
            self.length = 1
    
    def __len__(self) -> int:
        return self.length
    
    def __iter__(self):
        iterator = next(self)
        return iterator
    
    def __next__(self):
        if self.length==0:
            return []
        temp = self.head
        while temp!=None:
            yield temp.value
            temp = temp.next
    
    def __repr__(self) -> str:
        return_string = ""
        temp = self.head
        while temp!=None:
            return_string += f"{temp.value} -> "
            temp = temp.next
        return_string = return_string[:-4]
        return return_string if return_string!="None" else self.empty_repr
    
    
    def append(self, value: Union[int, float, str]) -> None:
        """Inserts a Node in the tail and reassign the tail to the Node"""
        if value==None:
            raise ValueError("Inserting None type value is not allowed")

        if self.length==0:
            self.__init__(value)
            return

        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
    
    def pop(self) -> Union[int, float, str]:
        """Removes the last Node in found in the head and returns the value of the node"""
        if self.length == 0:
            raise ValueError("Can't pop from and empty Singly_Linked_List")
        
        elif self.length == 1:
            value = self.head.value
            self.__init__()
            return value
        
        temp = self.head
        while temp.next.next:
            temp = temp.next
        
        value = temp.next.value
        temp.next = None
        self.length -= 1
        return value

a = Singly_Linked_List()