from db_answers import jsons


def new_class(class_name: str):
    def constructor(self, attrs: dict):
        for key in attrs.keys():
            self.__dict__[key] = attrs[key]

    return type(class_name, (object,), {"__init__": constructor})


cn = "Custom"
Custom_class = new_class(cn)
new_obj = Custom_class({'a': 1, 'b': 2})
print(type(new_obj))
print(new_obj.a)
print(new_obj.b)


def deserializer_manual(jsons):
    def add_item(item, items: list, key):
        if len(items):
            for i in items:
                if i[key] == item[key]:
                    break
            else:
                items.append(item)
        else:
            items.append(item)
        return items

    holders, equipments = [], []
    for json in jsons:
        holder, equipment = dict(), dict()
        for key in json.keys():
            if key.startswith('holder'):
                holder[key] = json[key]
            else:
                equipment[key] = json[key]

        holders = add_item(holder, holders, 'holderPhone')
        equipments = add_item(equipment, equipments, 'equipmentTitle')

    holder_objs = [new_class('Holder')(json) for json in jsons]
    equipment_objs = [new_class('Equipment')(json) for json in jsons]

    return holder_objs, equipment_objs


print(deserializer_manual(jsons))
