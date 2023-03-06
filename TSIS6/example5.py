import os

print(os.environ)
pip freeze
print(os.environ['PATH'])
print(os.getenv('a', '12345'))
