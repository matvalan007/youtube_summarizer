from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai

def summarize(url):
  api_key = "YOUR_GEMINI_API_KEY"
  video_id = url.split("watch?v=")[-1]
  transcript = YouTubeTranscriptApi.get_transcript(video_id)
  transcript = " ".join([line['text'] for line in transcript])
  prompt = f'"Summarize the given text. \ntext = "{transcript}.""'
  genai.configure(api_key=api_key)

  model = genai.GenerativeModel("gemini-1.5-flash")
  response = model.generate_content(prompt)
  return response.text
