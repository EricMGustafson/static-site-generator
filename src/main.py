from textnode import TextNode, TextType


def main():
  node = TextNode("Hello", TextType.BOLD, "https://boot.dev")
  print(node.__repr__())

main()