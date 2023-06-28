import json

class BaseModel:
    def __init__(self, DATA_BASE_PATH) -> None:
        self.DATA_BASE_PATH = DATA_BASE_PATH
    
    @property
    def id(self) -> int:
        return self.auto_generate_id()
    
    def auto_generate_id(self) -> int:
        ids = self.get_data().keys()
        if len(ids) > 0:
            return int(list(ids)[-1]) + 1
        else:
            return 1
        
    def create(self, attribute: dict) -> None:
        data = self.data_to_insert(attribute)
        with open(self.DATA_BASE_PATH, 'w', encoding="utf-8") as file:
            file.write(data)
            file.close()
        
    def data_to_insert(self, attributes: dict) -> str:
        content = self.get_data()
        content[self.id] = attributes
        return json.dumps(content)
    
    def get_data(self) -> dict:
        content = open(self.DATA_BASE_PATH,encoding="utf-8").read()
        if content:
            content = json.loads(content)
        else:
            content = {}
        return content
    
    def get_items(self, attributes, separator) -> list:
        data = self.get_data()
        items = []
        for id, data_item in data.items():
            items.append(id + ' - ' + data_item[attributes[0]] + separator + data_item[attributes[1]])
        return len(data), items
    
    def list_options(self, attributes) -> list:
        return self.get_items(attributes, ' ')[1]
    
    def get_item(self, id) -> dict:
        return self.get_data()[str(id)]
