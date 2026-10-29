

import gradio as gr
from google import genai
import os
from google.genai import types

persona = {
    "Friendly":
    "You are a friendly, enthusiastic, and highly encouraging Study Assistant. Your goal is to break down complex concepts into simple, beginner-friendly explanations. Use analogies and real-world examples that beginners can relate to. Always ask a follow-up question to check understanding",
    "Academic":
    "You are a strictly academic, highly detailed, and professional university Professor. Use precise, formal terminology, cite key concepts and structure your response. Your goal is to break down complex concepts into simple, beginner-friendly explanations. Use analogies and real-world examples that beginners can relate to. Always ask a follow-up question to check understanding"
  }

client = genai.Client(api_key = os.getenv("study_assistance_api_key"))

def study_assitance1(question, p):
  system_prompt = persona[p]
  response = client.models.generate_content(
      model = "gemini-3.6-flash",
      config = types.GenerateContentConfig(
          system_instruction = system_prompt,
          temperature = 0.4,
          max_output_tokens = 2000
      ),
      contents = question
  )
  return response.text

demo = gr.Interface(
  fn = study_assitance1,
  inputs= [
      gr.Textbox(placeholder="Ask your Question", label="Question", lines=4),
      gr.Radio(choices=list(persona.keys()), value="Frindely", label="Personality")
  ],
  outputs=gr.Textbox(lines=10, label="Answer"),
  title="AI assistance",
  description="Ask your question to get response from Study asssistance..."
)


demo.launch(debug=True)

