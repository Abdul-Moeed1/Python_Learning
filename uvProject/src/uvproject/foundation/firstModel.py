from pydantic import BaseModel , Field , field_validator , model_validator, computed_field 
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


# class Employee(BaseModel):
#     id:int
#     name: str = Field(... , min_length=4 , max_length=100 , examples=["Harry"]  )
#     department : Optional[str] = "General"
#     salary: float = Field(... , ge=40000)

# empInput = {"id" : 345 , "name" : "Harry" , "department" : "Development", "salary": "50000" , "age":43}

# emp = Employee(**empInput)
# print(emp)


# class UserModel(BaseModel):
#     name : str

#     @field_validator("name")
#     def validateName(cls , val):
#         if len(val) < 5:
#             raise ValueError("Name can not be less then 5 letters")
#         else:
#             return val

        
# inputValue = {"name" : "abc"}

# user = UserModel(**inputValue)
# print(user)


# class signupForm(BaseModel):
#     password : str
#     confirmPassword:  str

#     @model_validator(mode="after")
#     def passwordMatch(self):
#         if self.password != self.confirmPassword : 
#             raise ValueError("Passwords do not match.")
#         else:
#             return self

    
# inputValue = {"password" : "abc" , "confirmPassword" : "abc" }

# user = signupForm(**inputValue)
# print(user)


class Product(BaseModel):
    price : int
    quantity : int

    @computed_field
    @property
    def totalPrice(self) -> int:
        return self.price * self.quantity

    
inputValue = {"price" : "23" , "quantity" : "232" }

user = Product(**inputValue)
print(user)


