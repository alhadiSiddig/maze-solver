#persistence/serializer.py 

def dump(maze: Maze  , path: pathlib.Path) -> None : 
    header, body = serialize(maze)
    with path.open(mode = 'wb') as file: 
        header.write(file)
        body.write(file) 

def load(path : pathlib.Path) -> Maze : 
    with path.open('rb') as file : 
        header = FileHeader.read(file) 
        if header.format_version != FORMAT_VERSION: 
            raise ValueError('unsupported file format ') 
        
        body = FileBody.read(header ,file) 
        return deserializer(header, body) 
    