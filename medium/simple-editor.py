class Editor:
    
    def __init__(self):
        self.state = [""]

    def append(self, word):
        self.state.append(self.state[-1] + word)
    
    def delete(self, k):
        if k > len(self.state[-1]):
            self.state.append("")
        else:
            self.state.append(self.state[-1][:-k])        
    
    def print(self, k):
        print(self.state[-1][k-1])        
    
    def undo(self):
        self.state.pop()

# main
editor = Editor()
n = int(input())
for i in range(n):
    op_args = input().split()
    op = int(op_args[0])
    arg = None if len(op_args) == 1 else op_args[1]

    if op == 1:
        editor.append(arg)
    elif op == 2:
        editor.delete(int(arg))
    elif op == 3:
        editor.print(int(arg))
    else:
        editor.undo()