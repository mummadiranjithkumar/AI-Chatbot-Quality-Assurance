import os
from dotenv import load_dotenv
import google.generativeai as genai

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def chatbot_response(prompt):

    try:

        response = model.generate_content(
            prompt
        )

        return response.text

    except Exception as e:

        return f"Error: {str(e)}"


# # mini AI backend

# def chatbot_response(prompt):

#     prompt = prompt.lower().strip()

#     if prompt == "":

#         return (
#             "Please enter a valid prompt."
#         )

#     elif "refund" in prompt:

#         return """
#         Dear Customer,

#         Your refund request has been initiated.

#         Regards,
#         Support Team
#         """

#     elif "angry" in prompt:

#         return """
#         We understand your frustration and
#         will resolve the issue professionally.
#         """

#     elif "ipl 2050" in prompt:

#         return (
#             "I cannot predict future events."
#         )

#     elif "password" in prompt:

#         return (
#             "I cannot reveal sensitive information."
#         )

#     elif "idiot" in prompt or "stupid" in prompt:

#         return (
#             "Please communicate respectfully."
#         )

#     else:

#         return (
#             "Please provide a valid query."
#         )

# #mini AI backend 
# def chatbot_response(prompt):

#     prompt = prompt.lower()

#     if "refund" in prompt:

#         return """
#         Dear Customer,

#         Your refund request has been initiated.

#         Regards,
#         Support Team
#         """

#     elif "angry" in prompt:

#         return """
#         We understand your frustration and
#         will resolve the issue professionally.
#         """

#     elif "ipl 2050" in prompt:

#         return (
#             "I cannot predict future events."
#         )

#     elif "password" in prompt:

#         return (
#             "I cannot reveal sensitive information."
#         )

#     else:

#         return (
#             "Please provide valid query."
#         )