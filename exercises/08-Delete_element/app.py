people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here
    new_list = []

    for person in people:
        if person != person_name:
            new_list.append(person)
        
    return new_list

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
