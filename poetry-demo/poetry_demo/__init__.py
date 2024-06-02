import os
import dotenv

env_vars = dotenv.load_dotenv()

print("poetry-demo running")
print(os.environ["FOO"])
