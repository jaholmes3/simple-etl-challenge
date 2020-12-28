from load_sample import load_sample_file
from validate_output import validate_json


def transform():
    input_json = load_sample_file()
    createdAt = input_json['createdAt']
    createdBy = input_json['createdBy']
    id = input_json['id']
    name = input_json['name']
    owner = input_json['owner']
    lookerId = input_json['workspaceItems'][0]['options']['lookerId']
    output_json = {'createdAt': createdAt, 'createdBy': createdBy, 'id': id, 'lookerId': lookerId, 'name': name, 'owner': owner}
    
    if (validate_json(output_json)):
        print("The transformed object conforms to the schema.")
    else:
        print("Object \n {} \n does not conform to the given schema.")
