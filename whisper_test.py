from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

audio_file = open("/path/to/file/audio.mp3", "rb")

transcription = client.audio.transcriptions.create(
    model="whisper-1",   # 또는 "gpt-4o-transcribe"
    file=audio_file,
    language="ko"        # 한국어면 명시하는게 좋음!
)

print(transcription.text)
