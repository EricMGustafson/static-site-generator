from htmlnode import HTMLNode


class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    html_string = ''

    if not self.tag:
      raise ValueError("ParentNode must have tag")

    if not self.children:
      raise ValueError("ParentNode must have children")
    
    for child in self.children:
      html_string = html_string + child.to_html()
    
    return f'<{self.tag}{self.props_to_html()}>{html_string}</{self.tag}>'
    
