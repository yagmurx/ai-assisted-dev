import dotenv

print("hello world")
dotenv.load_dotenv()
print("Environment Variables Loaded:")

print("Secret Key:", dotenv.get_key(".env", "LOCAL_SECRET_KEY"))