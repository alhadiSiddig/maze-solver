from dataclasses import dataclass
from functools import cached_property 
from typing import Iterator 


from maze_solver.models.role import Role 
from maze_solver.models.square import Square


@dataclass(frozen = True)
class Maze : 
    squares : tuple [Square, ... ] 


    def __post_init__(self) -> None: 
          validate_indices(self) 
          validate_rows_columns(self) 
          validate_exit(self)
          validate_enterance(self) 


    def __iter__(self) -> Iterator[Square]: 
        return iter(self.squares) 
    
    def __getitem__(self, index : int ) -> Square: 
        return self.squares[index] 
    
    @cached_property
    def height(self): 
        return max(square.row for square in self) +1 
    

    @cached_property 
    def width(self):
        return max(square.column for square in self )+1
    
    @cached_property
    def enterance(self): 
        return next(sq for sq in self if sq.role is Role.ENTERANCE)
    

    @cached_property
    def exit(self) -> Square: 
        return next(sq for sq in self if sq.role is Role.EXIT ) 
    
def validate_indices(maze: Maze)-> None: 
        assert [ square.index for square in maze] == list(
        range(len(maze.squares))    
        ),"wrong square.index "
    
def validate_rows_columns(maze: Maze) -> None : 
    for y in range(maze.height): 
        for x in range(maze.width): 
            square = maze [ y * maze.width + x ] 
            assert square.row ==y , 'wrong square.row '
            assert square.column == x , "Wrong square.column" 

def validate_enterance(maze: Maze) -> None: 
    assert 1 == sum(
        1 for square in maze if square.role is Role.ENTERANCE
    ) , "Must be exactly one enterance " 


def validate_exit(maze: Maze ) -> None: 
    assert 1 == sum(
        1 for square in maze if square.role is Role.EXIT
        ) , "Must be exactly one exit" 
        
