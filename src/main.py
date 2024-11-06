print("hello world")
from textnode import TextNode, TextType
def main():
    new_instance = TextNode("this is text", TextType.NORMAL, "https://www.boot.dev")
    print(new_instance)

main()