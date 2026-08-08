# gh-stack-test

## Usage

```python
from greeting import greet
from farewell import farewell
from shout import shout

greet("Ada")      # "Hello, Ada!"
farewell("Ada")    # "Goodbye, Ada!"
shout("ada")       # "ADA!!!"
```

Each function falls back to `DEFAULT_NAME` ("World") when given a blank name.