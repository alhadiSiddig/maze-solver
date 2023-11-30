#persistance/file_format.py

import struct
from dataclasses import dataclass
from typing import BinaryIO

MAGIC_NUMBER : bytes = b'MAZE'

@dataclass 
class FileHeader(frozen = True ): 
    format_version : int 
    width : int 
    height : int 
   
    @classmethod
    def read(cls , file : BinaryIO) -> "FileHeader": 
        assert (
            file.read(len(MAGIC_NUMBER)) == MAGIC_NUMBER
        ) , 'Unkown file type ' 
        format_version, = struct.unpack('B' , file.read(1))
        width , height = struct.unpack('<2I' , file.read(2*4))
        return cls(format_version , width , height) 
    
    


    def write( self, file : BinaryIO) -> None : 
        file.write(MAGIC_NUMBER) 
        file.write(struct.pack("B" , self.format_version))
        file.write(struct.pack("<2I" , self.width , self.height))


    