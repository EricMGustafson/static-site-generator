import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_props_to_html(self):
    props_dic = {
      "href": "https://www.google.com", 
      "target": "_blank",
    }
    expected_result = ' href="https://www.google.com" target="_blank"'
    node = HTMLNode(None, None, None, props_dic)
    self.assertEqual(node.props_to_html(), expected_result)

if __name__ == "__main__":
  unittest.main()