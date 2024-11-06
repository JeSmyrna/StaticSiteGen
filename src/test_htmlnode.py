import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_LeafNode_A(self):
        node = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)
        text = node.to_html()
        print(text)
    
    def test_LeafNode_B(self):
        node = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text",),
    ],)
        text = node.to_html()
        print(text)

    def test_LeafNode_C(self):
        node = ParentNode("p",
    [
        LeafNode("a", "text is werid and stupid"),
    ],)
        
        text = node.to_html()
        print(text)

    def test_LeafNode_D(self):
        node = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text",{"href" : "www.google.de"}),
    ],)
        text = node.to_html()
        print(text)

    def test_LeafNode_E(self):
        node = ParentNode("p",
        [
            HTMLNode("a", "texti text to read for you", None, {"href":"www.weirdlink_toread.us"})
        ],)
        text = node.to_html()
        print(text)

if __name__ == "__main__":
    unittest.main()