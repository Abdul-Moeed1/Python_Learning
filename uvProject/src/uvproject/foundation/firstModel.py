from pydantic import BaseModel , Field
from typing import List, Dict , Optional

# class UserType(BaseModel):
#     id: int
#     name :str
#     isActive : bool

# class ProductType(BaseModel):
#     id:int
#     name:str
#     price:float
#     inStock:bool = True

# class CartType(BaseModel):
#     userId: int
#     items : List[str]
#     quantities: Dict[str, int]

# class BlogPost(BaseModel):
#     title: str
#     content: str
#     imageUrl : Optional[str] = None

# inputData = {"id" :4435 , "name" : "Harry" , "isActive" : "True"}

# user = UserType(**inputData)
# print(user)


class Employee(BaseModel):
    id:int
    name: str = Field(... , min_length=4 , max_length=100 , examples=["Harry"]  )
    department : Optional[str] = "General"
    salary: float = Field(... , ge=40000)

empInput = {"id" : 345 , "name" : "Harry" , "department" : "Development", "salary": "50000" , "age":43}

emp = Employee(**empInput)
print(emp)
