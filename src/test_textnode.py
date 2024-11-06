import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_Normal(self):
        node = TextNode("this is some text", TextType.TEXT, None)
        node = node.text_node_to_html_node()
        print(node.to_html())
        
    def test_BOLD(self):
        node = TextNode("this is some text", TextType.BOLD, None)
        node = node.text_node_to_html_node()
        print(node.to_html())
    
    def test_ITALIC(self):
        node = TextNode("this is some text", TextType.ITALIC, None)
        node = node.text_node_to_html_node()
        print(node.to_html())

    def test_CODE(self):
        node = TextNode("this is some text", TextType.CODE, None)
        node = node.text_node_to_html_node()
        print(node.to_html())

    def test_LINK(self):
        node = TextNode("Click Here !!!", TextType.LINK, "www.whatIsThatLink.org")
        node = node.text_node_to_html_node()
        print(node.to_html())

    def test_IMAGE(self):
        node = TextNode("Image Descirption alt Text", TextType.IMAGE, "www.whatIsThatLink.org")
        node = node.text_node_to_html_node()
        print(node.to_html())

if __name__ == "__main__":
    unittest.main()
