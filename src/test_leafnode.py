import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_valid_return_when_none_tag(self):
    node = LeafNode(None, "This should be raw text")
    expected_result = "This should be raw text"
    self.assertEqual(node.to_html(), expected_result)
  
  def test_valid_return_when_none_props(self):
    node = LeafNode("p", "This should be raw text")
    expected_result = "<p>This should be raw text</p>"
    self.assertEqual(node.to_html(), expected_result)

  def test_valid_return_when_prop(self):
    props_dic = {
      "href": "https://www.google.com", 
      "target": "_blank",
    }
    node = LeafNode("a", "https://www.google.com", props_dic)
    expected_result = "<a href=\"https://www.google.com\" target=\"_blank\">https://www.google.com</a>"
    self.assertEqual(node.to_html(), expected_result)
