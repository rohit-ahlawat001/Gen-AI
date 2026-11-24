
# from langchain_google_genai import GoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = GoogleGenerativeAI(
#         model="gemini-3.7-flash",
#         temperature=0.3,
#         max_output_tokens=100,
#     )
# print("=" * 30)
# print("My Ai Assistant")
# print("=" * 30)

# while True:
#     user_input = input("\nAsk Anything: " )

#     if user_input.lower() == "quit":
#         print("\nAI: Goodbye Have A Great Day!")
#         break

#     response = llm.invoke(user_input)
#     print("Getting your Response. Please Wait!")
#     print(f"\nAssistant: {response.content}")



from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = GoogleGenerativeAI(
    model="gemini-3.7-flash",
        temperature=0.3,
        max_output_tokens=100,
)

print("=" * 20)
print("Persnal Assistant")
print("=" * 20)

print(llm.model)

while True:
    user_input = input("Ask Someting: " )

    if user_input.lower() == "quit":
     print("\nAI: Goodbye Have A Great Day!")
     break

    response = llm.invoke.user_input()