from openai import OpenAI

print("Hello World")

llm =OpenAI(
    api_key = "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"
)

output = llm.chat.completions.create(
    model = "gpt-4o-mini",
    messages= [
        {"role":"user", "content":"Who is Someshwar Giddigam"}
    ],
)
print(output)