
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



# from langchain_google_genai import GoogleGenerativeAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = GoogleGenerativeAI(
#     model="user_input",
#         temperature=0.3,
#         max_output_tokens=100,
# )

# print("=" * 20)
# print("Persnal Assistant")
# print("=" * 20)

# print(llm.model)

# while True:
#     user_input = input("Ask Someting: " )

#     if user_input.lower() == "quit":
#         print("\nAI: Goodbye Have A Great Day!")
#         break

#     response = llm.invoke(user_input)
#     print("Getting your Response. Please Wait!")
#     print(f"\nAssistant: {response}")



from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
# message = []
llm = GoogleGenerativeAI(
    model="gemini-3.7-flash",
    temperature=0.3,
    max_output_tokens=256,
    # messages = message
)
message = []

print("=" * 20)
print("Personal Assistant")
print("=" * 20)

print(message)

while True:
    user_input = input("\nAsk Something: ")


    if user_input.lower() == "quit":
        print("\nAI: Goodbye! Have a Great Day!")
        break

    try:
        print("\nGetting your response. Please wait!")
        message.append({"role": "user", "content": user_input
        })
        response = llm.invoke(message)

        print(f"\nAssistant: {response}")
        message.append({"role": "assistant", "content": response})

    except Exception as e:
        print(f"\nError: {e}")
