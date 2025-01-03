from enum import Enum

from leafnode import LeafNode

class TextType(Enum):
    TEXT = "normal" 
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code" 
    LINK = "link"
    IMAGE = "image"


class TextNode():
  def __init__(self, text, text_type, url=None):
     self.text = text
     self.text_type = text_type
     self.url = url
  
  def __eq__(self, other):
     if not isinstance(other, TextNode):
        return False
     return (self.text == other.text and self.text_type == other.text_type and self.url == other.url)

  def __repr__(self):
     return f"{self.__class__.__name__}({self.text}, {self.text_type.value}, {self.url})"