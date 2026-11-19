# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# import os

# load_dotenv()

# client = ChatGoogleGenerativeAI(
#         model="gemini-3.7-flash",
#         temperature=0.3,
#         max_output_tokens=50,
#     )
# # print(client)

# print("=" * 20)
# print("My AI Asssistant")
# print("=" * 20)

# while True:
#     user_query = input("\nUser: " )

#     if user_query.lower() == "quit":
#         print("\n Assistant: Goodbye! Have a Great Day.")
#         break

#     response = client.invoke(user_query)

#     print(f"\nAssistant: {response.content}")