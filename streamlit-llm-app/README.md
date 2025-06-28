# streamlit-llm-app

「app.py」にコードを記述してください。
画面に入力フォームを1つ用意し、入力フォームから送信したテキストをLangChainを使ってLLMにプロンプトとして渡し、回答結果が画面上に表示されるようにしてください。なお、当コースのLesson8を参考にLangChainのコードを記述してください。
ラジオボタンでLLMに振る舞わせる専門家の種類を選択できるようにし、Aを選択した場合はAの領域の専門家として、またBを選択した場合はBの領域の専門家としてLLMに振る舞わせるよう、選択値に応じてLLMに渡すプロンプトのシステムメッセージを変えてください。また用意する専門家の種類はご自身で考えてください。
「入力テキスト」と「ラジオボタンでの選択値」を引数として受け取り、LLMからの回答を戻り値として返す関数を定義し、利用してください。
Webアプリの概要や操作方法をユーザーに明示するためのテキストを表示してください。
Streamlit Community Cloudにデプロイする際、Pythonのバージョンは「3.11」としてください。

参考Chapter8
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

first_completion = client.chat.completions.create(
   model="gpt-4o-mini",
   messages=[
       {"role": "system", "content": "あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。"},
       {"role": "user", "content": "最近眠れないのですが、どうしたらいいですか？"}
   ],
   temperature=0.5
)

print(first_completion.choices[0].message.content)