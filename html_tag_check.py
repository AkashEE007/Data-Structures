class Stack:
    """A Stack ADT is created inside this class with numerous methods that
    defines the stack operations."""

    def __init__(self):
        self.items = []

    def is_empty(self):
        """The method checks whether the stack is empty or not and returns Boolean
        True or False."""
        return self.items == []
    
    def push(self,item):
        """The method adds a new item at the top of the stack. Requires a parameter
        and returns nothing."""

        self.items.append(item)

    def pop(self):
        """The method removes the item that is at the top of the stack. Does not 
        requires any parameter and returns the popped item."""

        return self.items.pop()
    
    def peek(self):
        """The method returns the item that is at the top of the stack. Does not 
        requires any parameter."""

        return self.items[len(self.items) - 1]
    
    def size(self):
        """The method returns the number of items on the stack. Does not requires 
        any parameter."""

        return len(self.items)

html_doc = input("Enter an HTML document...\n")
"""Enter the HTML code as string with spaces between each words and tags."""

def tag_checker(html_doc):
    stack = Stack()
    opening_tags = ["<html>","<head>","<body>","<title>","<a>","<p>","<b>","<i>","<h1>","<h2>",
                    "<h3>","<h4>","<h5>","<h6>","<table>","<tr>","<td>","<form>"]
    
    closing_tags = ["</html>","</head>","</body>","</title>","</a>","</p>","</i>","</b>","</h1>",
                    "</h2>","</h3>","</h4>","</h5>","</h6>","</table>","</tr>","</td>","</form>"]
    
    tags_dict = {"</html>":"<html>",
                 "</head>":"<head>",
                 "</body>":"<body>",
                 "</title>":"<title>",
                 "</a>":"<a>","</p>":"<p>",
                 "</b>":"<b>","</h1>":"<h1>",
                 "</h2>":"<h2>","</h3>":"<h3>",
                 "</h4>":"<h4>","</h5>":"<h5>",
                 "</h6>":"<h6>","</tr>":"<tr>",
                 "</table>":"<table>","</td>":"<td>",
                 "</form>":"<form>"}
    
    tags_list = html_doc.split(" ")
    print(tags_list)

    for tag in tags_list:
        if tags_list[0] in closing_tags:
            print("Terminated here!")
            return False
        
        elif tag in opening_tags:
            stack.push(tag)

        elif tag in closing_tags:
            if tags_dict[tag] in stack.items:
                stack.pop()
        
    if stack.is_empty():
        return True
    
    else:
        return False
    
print(tag_checker(html_doc))