class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.value == None:
            raise ValueError
        
        elif self.tag == None:
            return f"{self.value}"
        
        html_text = ""
        html_text += f"<{self.tag}"
        if self.props is not None:
            for key, value in self.props.items():
                html_text += f' {key}="{value}"'
        html_text += f">{self.value}"
        html_text += f"</{self.tag}>"
        return html_text
    
    def props_to_html(self):
        new_list = []
        for p in self.props:
            key = f"{p}"
            print(key)
            new_list.append(f" {key}='{self.props[key]}'")
        new_string = "".join(new_list)
        return new_string
    
    def __repr__(self) -> str:
        return f"TAG: {self.tag}, VALUE: {self.value}, CHILDREN: {self.children}, PROPS: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        if value == None:
            raise ValueError
        super().__init__(tag=tag, value=value, props=props)
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children):
        super().__init__(tag=tag, children=children)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError ("No Tag found")
        elif self.children == []:
            raise ValueError ("No Child found")
        
        html_text = f"<{self.tag}>"
        for child in self.children:
            text = child.to_html()
            html_text += text
        html_text += f"</{self.tag}>"
        return html_text