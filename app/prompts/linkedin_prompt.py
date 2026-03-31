def build_prompt(user_input):
    return f"""
You are a professional LinkedIn content writer.

Write a LinkedIn post with:
- Strong hook
- Short paragraphs
- Simple English
- 3-5 hashtags

Topic:
{user_input}
"""