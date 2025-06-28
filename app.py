import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

load_dotenv()

def get_llm_response(user_input, expert_type):
    """
    入力テキストとラジオボタンの選択値を受け取り、LLMからの回答を返す関数
    
    Args:
        user_input (str): ユーザーからの入力テキスト
        expert_type (str): 選択された専門家の種類
    
    Returns:
        str: LLMからの回答
    """
    # OpenAI APIキーの確認
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return "エラー: OPENAI_API_KEYが設定されていません。"
    
    # LangChainのChatOpenAIモデルを初期化
    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.5,
        api_key=api_key
    )
    
    # 専門家に応じたシステムメッセージを設定
    system_messages = {
        "健康アドバイザー": "あなたは健康と医療に関する専門的なアドバイザーです。科学的根拠に基づいた安全で実用的なアドバイスを提供してください。",
        "キャリアコンサルタント": "あなたはキャリア開発と転職に関する経験豊富なコンサルタントです。個人の成長とキャリアの成功に向けた実践的なアドバイスを提供してください。",
        "料理専門家": "あなたは料理とレシピ開発の専門家です。美味しく、健康的で、実用的な料理のアドバイスとレシピを提供してください。"
    }
    
    system_message = system_messages.get(expert_type, "あなたは親切なアシスタントです。")
    
    # メッセージリストを作成
    messages = [
        SystemMessage(content=system_message),
        HumanMessage(content=user_input)
    ]
    
    try:
        # LLMに問い合わせ
        response = llm.invoke(messages)
        return response.content
    except Exception as e:
        return f"エラーが発生しました: {str(e)}"

# Streamlitアプリケーションのメイン部分
def main():
    # ページ設定
    st.set_page_config(
        page_title="専門家AI相談アプリ",
        layout="centered"
    )
    
    # タイトルと説明
    st.title(" 専門家AI相談アプリ")
    st.markdown("""
    ### 概要
    このアプリケーションでは、AIが様々な分野の専門家として、あなたの質問に答えます。
    
    ### 使い方
    1. 相談したい専門家を選択してください
    2. テキストボックスに質問や相談内容を入力してください
    3. 「送信」ボタンをクリックすると、選択した専門家としてAIが回答します
    
    ---
    """)
    
    # ラジオボタンで専門家を選択
    expert_type = st.radio(
        "相談したい専門家を選択してください:",
        ["健康アドバイザー", "キャリアコンサルタント", "料理専門家"]
    )
    
    # 入力フォーム
    user_input = st.text_area(
        "質問や相談内容を入力してください:",
        placeholder="例: 最近眠れないのですが、どうしたらいいですか？",
        height=100
    )
    
    # 送信ボタン
    if st.button("送信", type="primary"):
        if user_input:
            # 処理中のスピナーを表示
            with st.spinner("回答を生成中..."):
                # LLMから回答を取得
                response = get_llm_response(user_input, expert_type)
            
            # 回答を表示
            st.markdown("### 回答")
            st.markdown(f"**{expert_type}からの回答:**")
            st.write(response)
        else:
            st.warning("質問を入力してください。")

if __name__ == "__main__":
    main()