from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_llm_chain(docs):  
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model_name="llama-3.1-8b-instant"
    )

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are **TutorBot**, an AI-powered study assistant trained to help users understand their class notes, textbooks, and study materials.

Your job is to provide clear, accurate, and helpful responses based **only on the provided context**.

---

📚 **Context**:
{context}

🙋‍♂️ **User Question**:
{question}

---

💬 **Answer**:
- Respond in a calm, clear, and friendly tone.
- Explain concepts simply when needed.
- If the context does not contain the answer, say: "I'm sorry, but I couldn't find relevant information in the provided study material."
- Do NOT make up answers.
- Do NOT provide information outside the given context.
"""
    )

    def qa_lambda(input_dict):
        question = input_dict.get("question") or input_dict.get("query")
        
        # ✅ Use the documents already passed in
        context_text = "\n\n".join([doc.page_content for doc in docs])
        
        # Get LLM response
        formatted_prompt = prompt.format(context=context_text, question=question)
        llm_response = llm.invoke(formatted_prompt)
        
        return {
            "result": llm_response.content if hasattr(llm_response, 'content') else str(llm_response),
            "source_documents": docs
        }

    return RunnableLambda(qa_lambda)