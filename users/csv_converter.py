import json

def json_reader(filename: str) -> dict:

    try:
        with open(filename, 'r') as f:
            data = json.loads(f.read())
    except Exception as e:
        print(f"Exception encountered: {str(e)}")

    return data

def json_normalizer(data: dict) -> dict:
  
    new_data = dict()
    for key, value in data.items():
        if not isinstance(value, dict):
            new_data[key] = value
        else:
            for k, v in value.items():
                new_data[key + "_" + k] = v
  
    return new_data

def csv_generator(data: dict) -> str:
  
    csv_columns = data.keys()
  
    csv_data = ",".join(csv_columns) + "\n"
  
    new_row = list()
    for col in csv_columns:
        new_row.append(str(data[col]))
  
    csv_data += ",".join(new_row) + "\n"
  
    return csv_data

def write_to_file(data: str, filepath: str) -> bool:
  
    try:
        with open(filepath, "w+") as f:
            f.write(data)
    except Exception as e:
        print(f"Exception encountered: {str(e)}")

def main():
    data = json_reader(filename="dummy_api_user.json")
  
    new_data = json_normalizer(data=data)
  
    print("New dict:", new_data)
  
    csv_data = csv_generator(data=new_data)
    
    write_to_file(data=csv_data, filepath="user.csv")
  
  
if __name__ == '__main__':
    main()