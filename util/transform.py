from load_sample import load_sample_file
from validate_output import validate_json

def transform():
    input_json = load_sample_file()
    item1 = input_json['workspaceItems'][0]['name']
    item2 = input_json['workspaceItems'][0]['options']
    owner = input_json['owner']
    id = input_json['id']
    createdAt = input_json['createdAt']
    createdBy = input_json['createdBy']




    ### Write transformation here ###

    ### Assign result of transformation here ###
    output_json = {id}
    
    if (validate_json(output_json)):
        print("The transformed object conforms to the schema.")
    else:
        print("Object \n {} \n does not conform to the given schema.")