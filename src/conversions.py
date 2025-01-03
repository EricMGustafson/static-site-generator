from leafnode import LeafNode
from textnode import TextType


def text_node_to_html_node(text_node):
     match (text_node.text_type):
        case TextType.TEXT.value:
            return LeafNode(None, text_node.text)
        case TextType.BOLD.value:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC.value:
            return LeafNode("i", text_node.text)
        case TextType.CODE.value:
            return LeafNode("code", text_node.text)
        case TextType.LINK.value:
            if not text_node.url:
              raise ValueError("Url is required for anchor node")
            props = {
              "href": text_node.url, 
              "anchor-text": text_node.text,
              "target": "_blank"
            }
            return LeafNode("a", text_node.text, props)
        case TextType.IMAGE.value:
          if not text_node.url:
             raise ValueError("Url is required for image node")
          props = {
            "src": text_node.url, 
            "alt": text_node.text
          }
          return LeafNode("img", text_node.text, props)
        case _:
           raise ValueError("Invalid TextType")