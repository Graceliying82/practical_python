# practical_python
A reference repository for common Python utilities, showcasing best practices, Pytest usage, and more.

Plan to implement the following:

practical_python/
│── README.md                # Project overview and usage guide
│── pyproject.toml           # Project dependencies and configuration
│── src/                     # Source code directory
│   │── main.py              # Entry point showcasing various demos
│   │── data_types/          # Demonstrating built-in types
│   │   ├── lists_demo.py
│   │   ├── tuples_demo.py
│   │   ├── dicts_demo.py
│   │   ├── sets_demo.py
│   │── functions/           # Functions, *args, **kwargs, lambda, recursion
│   │   ├── basic_functions.py
│   │   ├── decorators.py
│   │   ├── higher_order_functions.py
│   │── classes/             # OOP concepts
│   │   ├── basic_class.py
│   │   ├── inheritance.py
│   │   ├── abstract_classes.py
│   │── file_handling/       # Read/write files, JSON, CSV
│   │   ├── read_write.py
│   │   ├── json_handling.py
│   │── concurrency/         # Threads, multiprocessing, async
│   │   ├── threading_demo.py
│   │   ├── async_demo.py
│   │── advanced_topics/     # Metaclasses, generators, context managers
│   │   ├── generators.py
│   │   ├── context_managers.py
│── test/                    # Testing folder
│   │── unit/                # Unit tests using pytest
│   │   ├── test_data_types.py
│   │   ├── test_functions.py
│   │   ├── test_classes.py
│   │── integration/         # Integration tests
│   │   ├── test_file_handling.py
│   │── behavior/            # Behavior-driven tests using behave
│   │   ├── features/
│   │   │   ├── demo.feature
│   │   ├── steps/
│   │   │   ├── test_steps.py
│── .gitignore               # Ignore unnecessary files
│── setup.cfg                # Configuration for pytest and behave
