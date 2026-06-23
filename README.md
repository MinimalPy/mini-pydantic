# Mini-Pydantic

a minimal implementation of pydantic, meant for understanding the basic mechanistic of data validation.

## Trying it out

min-pydantic won't be hosted on PyPI as its not inteded to be used professionally but rather educationally, so in-order to try it out we are just gonna use it in a testing environment.

```python
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
```

## Contributing

Contributions are welcome.

1. Fork the repository
2. Create a branch
3. Commit your changes
4. Open a pull request

Please ensure your code is tested and follows the project's style(simply minimal).
