class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """Given two strings s and t, return true if they are equal 
        when both are typed into empty text editors. 
        '#' means a backspace character.

        Args:
            s (str): a string (a-z, #)
            t (str): a string (a-z, #)

        Returns:
            bool: resulting strings are identical or not

        Time complexity:
            Best O(max(s, t))
            Worst O(max(s, t))
            where s and t are the input strings

        Space complexity:
            Best O(1) for strings containing all '#' characters
            Worst O(max(s, t))
            where s and t are the input strings
        """
        stack_s = Stack()
        stack_t = Stack()
        
        # Push all words to stack and 
        # pop item from stack if word is '#'
        for word in s:
            if word != '#':
                stack_s.push(word)
            elif word == '#':
                if not stack_s.isEmpty():
                    stack_s.pop()
        for word in t:
            if word != '#':
                stack_t.push(word)
            elif word == '#':
                if not stack_t.isEmpty():
                    stack_t.pop()
        
        # Compare each item in stack
        same = True
        while same and not stack_s.isEmpty() and not stack_t.isEmpty():
            word_s = stack_s.pop()
            word_t = stack_t.pop()
            same = word_s == word_t
            
        # Edge case: Difference length of words
        if not same or not stack_s.isEmpty() or not stack_t.isEmpty():
            return False
        
        return same
        
        
class Stack:
    def __init__(self):
        self.rear = None
        self.nodes = 0

    def __len__(self):
        return self.nodes

    def isEmpty(self):
        return len(self) == 0

    def push(self, item):
        node = Node(item)
        prev = self.rear
        if prev is not None:
            prev.next = node
        node.prev = prev
        self.rear = node
        self.nodes += 1

    def pop(self):
        if not self.isEmpty():
            item = self.rear.payload
            new_rear = self.rear.prev
            if new_rear is not None:
                new_rear.next = None
            self.rear = new_rear
            self.nodes -= 1
            return item

class Node:
    def __init__(self, payload, prev=None, next=None):
        self.payload = payload
        self.prev = prev
        self.next = next