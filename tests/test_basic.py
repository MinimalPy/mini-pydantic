from mini_pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    friends: list[int]

def test_basic_validation():
    user = User(
        name="Alice",
        age="25",
        friends=["1", "2"]
    )

    assert user.name == "Alice"
    assert user.age == 25
    assert user.friends == [1, 2]