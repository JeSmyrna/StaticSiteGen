from enum import Enum

from htmlnode import HTMLNode, LeafNode, ParentNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "img"
    PDF = "pdf"

class TextNode( ):
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = text_type.value
        self.url = url

    def __eq__(self, other):
        if not isinstance(other, TextNode):
            return False
        elif self.text == other.text and self.text_type == other.text_type and self.url == other.url:
            return True
        else:
            return False
        
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
    def text_node_to_html_node(self):
        if self.text_type == TextType.TEXT.value:
            return LeafNode(None,self.text)
        
        elif self.text_type == TextType.BOLD.value:
            return LeafNode("b", self.text)
        
        elif self.text_type == TextType.ITALIC.value:
            return LeafNode("i", self.text)
        
        elif self.text_type == TextType.CODE.value:
            return LeafNode("code", self.text)
        
        elif self.text_type == TextType.LINK.value:
            return LeafNode("a",self.text,{"href": self.url})
        
        elif self.text_type == TextType.IMAGE.value:
            return LeafNode("img","",{"src":self.url, "alt":self.text})
        
        else:
            raise Exception("Couldn't find text type")