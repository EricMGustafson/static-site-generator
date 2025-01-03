import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq_true_when_eq(self):
      node = TextNode("This is a text node", TextType.BOLD)
      node2 = TextNode("This is a text node", TextType.BOLD)
      self.assertEqual(node, node2)

    def test_eq_false_when_not_eq_text(self):
      node = TextNode("This is a text node", TextType.BOLD)
      node2 = TextNode("This is not a text node", TextType.BOLD)
      self.assertNotEqual(node, node2)

    def test_eq_false_when_not_eq_text_type(self):
      node = TextNode("This is a text node", TextType.BOLD)
      node2 = TextNode("This is a text node", TextType.ITALIC)
      self.assertNotEqual(node, node2)

    def test_eq_false_when_not_eq_url(self):
      node = TextNode("This is a text node", TextType.BOLD)
      node2 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
      self.assertNotEqual(node, node2)

    def test_type_when_no_url(self):
      node = TextNode("This is a text node", TextType.BOLD)
      self.assertEqual(node.url.__class__.__name__, 'NoneType')

    def test_eq_false_when_not_textnode(self):
      node = TextNode("This is a text node", TextType.BOLD)
      string = ""
      self.assertNotEqual(node, string)
      
if __name__ == "__main__":
    unittest.main()