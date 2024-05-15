# using linked list
class ListNode(object):
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory(object):
    def __init__(self, homepage):
        self.current = ListNode(homepage)
    
    def visit(self, url):
        self.current.next = ListNode(url, None, self.current)
        self.current = self.current.next

    def back(self, steps):
        while self.current.prev and steps > 0:
            self.current = self.current.prev
            steps -= 1

        return self.current.val
        
    def forward(self, steps):
        while self.current.next and steps > 0:
            self.current = self.current.next
            steps -= 1

        return self.current.val
    
# using stack => more efficient
class BrowserHistory(object):
    def __init__(self, homepage):
        self.i = 0
        self.len = 1
        self.history = [homepage]
    
    def visit(self, url):
        if len(self.history) <= self.i + 1:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url

        self.i += 1
        self.len = self.i + 1

    def back(self, steps):
        self.i = max(self.i - steps, 0)

        return self.history[self.i]
        
    def forward(self, steps):
        self.i = min(self.i + steps, self.len - 1)

        return self.history[self.i]
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)