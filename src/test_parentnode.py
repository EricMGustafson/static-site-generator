import unittest

from leafnode import LeafNode
from parentnode import ParentNode 

class TestParentNode(unittest.TestCase):
  def test_valid_return_when_leaf_nodes(self):
    node = ParentNode("p", [
          LeafNode("b", "Bold text"),
          LeafNode(None, "Normal text"),
          LeafNode("i", "italic text"),
          LeafNode(None, "Normal text")
      ]
    )
    expected_result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
    self.assertEqual(node.to_html(), expected_result)
  
  def test_valid_return_when_parent_nodes(self):
    node = ParentNode("p", [
            ParentNode("s", [
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text")
          ])
        ]
      )
    expected_result = "<p><s>Normal text<i>italic text</i>Normal text</s></p>"
    self.assertAlmostEqual(node.to_html(), expected_result)
  
  def test_error_return_when_no_children(self):
    node = ParentNode("p", {})
    with self.assertRaises(ValueError):
      node.to_html()
    