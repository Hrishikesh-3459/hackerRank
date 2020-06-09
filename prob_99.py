""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    return validate(root)
    
def validate(node, minVal = float('-inf'), maxVal = float('inf')):
    if not node:
        return True
    if not minVal < node.data < maxVal:
        return False
    return (validate(node.left, minVal, node.data) and validate(node.right, node.data, maxVal))
        
