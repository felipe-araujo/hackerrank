""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    if not root:
        return True
    if root.left and root.left.data > root.data:
        return False
    if root.right and root.right.data < root.data:
        return False
    return check_binary_search_tree_(root.left) and check_binary_search_tree_(root.right)