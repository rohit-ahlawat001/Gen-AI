
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



from langchain_google_genai import ChatGoogleGenerativeAI
# from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# message = []
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.3,
    max_output_tokens=30,
    # messages = message
)

# llm = OpenAI(
#     model= "gpt-5.4-mini",
#     temperature= 0.3,
#     max_tokens= 50
# )
message = []
# for msg in message:
#     print(msg)
print("=" * 20)
print("Personal Assistant")
print("=" * 20)

while True:
    user_input = input("\nAsk Something: ")


    if user_input.lower() == "quit":
        print("\nAI: Goodbye! Have a Great Day!")
        break

    try:
        print("\nGetting your response. Please wait!")
        message.append({
                "role": "user",
                "content": user_input
            })
        response = llm.invoke(message)
        assistant_response = response.content[0]["text"]

        print(f"\nAssistant: {assistant_response}")
        message.append({"role": "assistant", "content": assistant_response})
        print("\n" + "=" * 20)
        print("Conversation History")
        print("=" * 20)

        for msg in message:
                print(f"\n{msg['role'].upper()}:")
                print(msg['content'])
    except Exception as e:
        print(f"\nError: {e}")
