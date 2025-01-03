import unittest

from conversions import text_node_to_html_node
from leafnode import LeafNode
from textnode import TextNode, TextType


class TestConversions(unittest.TestCase):
  def test_converts_to_html_normal(self):
        node  = TextNode("Test", TextType.TEXT.value)
        text_to_leaf_node = text_node_to_html_node(node)
        leaf_node = LeafNode(None, "Test")
        self.assertTrue(text_to_leaf_node.tag == leaf_node.tag and text_to_leaf_node.value == leaf_node.value)
      
  def test_converts_to_html_bold(self):
    node  = TextNode("Test", TextType.BOLD.value)
    text_to_leaf_node = text_node_to_html_node(node)
    leaf_node = LeafNode("b", "Test")
    self.assertTrue(text_to_leaf_node.tag == leaf_node.tag and text_to_leaf_node.value == leaf_node.value)
  
  def test_converts_to_html_italic(self):
    node  = TextNode("Test", TextType.ITALIC.value)
    text_to_leaf_node = text_node_to_html_node(node)
    leaf_node = LeafNode("i", "Test")
    self.assertTrue(text_to_leaf_node.tag == leaf_node.tag and text_to_leaf_node.value == leaf_node.value)
  
  def test_converts_to_html_code(self):
    node  = TextNode("Test", TextType.CODE.value)
    text_to_leaf_node = text_node_to_html_node(node)
    leaf_node = LeafNode("code", "Test")
    self.assertTrue(text_to_leaf_node.tag == leaf_node.tag and text_to_leaf_node.value == leaf_node.value)
  
  def test_converts_to_html_link(self):
    node  = TextNode("Test", TextType.LINK.value, "https://www.google.com")
    text_to_leaf_node = text_node_to_html_node(node)
    props = {
            "href": node.url, 
            "anchor-text": node.text,
            "target": "_blank"
          }
    leaf_node = LeafNode("a", "Test", props)
    self.assertTrue(text_to_leaf_node.tag == leaf_node.tag and text_to_leaf_node.value == leaf_node.value and text_to_leaf_node.props == leaf_node.props)
  
  def test_converts_to_html_image(self):
    node  = TextNode("Test", TextType.IMAGE.value, "https://www.google.com")
    text_to_leaf_node = text_node_to_html_node(node)
    props = {
          "src": node.url, 
          "alt": node.text
        }
    leaf_node = LeafNode("img", "Test", props)
    self.assertTrue(text_to_leaf_node.tag == leaf_node.tag and text_to_leaf_node.value == leaf_node.value and text_to_leaf_node.props == leaf_node.props)
  
  def test_error_return_when_unknownType(self):
    node = TextNode("Test", "banana")
    with self.assertRaises(ValueError):
       text_node_to_html_node(node)
      
