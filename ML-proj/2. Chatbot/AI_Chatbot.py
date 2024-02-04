import streamlit as st

st.title("FOR EX\:GPT4")

def chat_actions():
    st.session_state["chat_history"].append(
        {"role": "user", "content": st.session_state["chat_input"]},
    )
    if "chat_history" in st.session_state and "human_name" not in st.session_state:
        st.session_state.human_name = st.session_state["chat_input"]
        st.session_state["chat_history"].append(
                {
                    "role": "assistant",
                    "content": f'Nice to meet you {st.session_state.human_name}. How can I help you today?',
                },  
            )
    else:
        st.session_state["chat_history"].append(
                {"role": "assistant",
                    "content": f'Repeating {st.session_state["chat_input"]}',
                },  
            )

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
    st.session_state["chat_history"].append(
        {"role": "assistant",
            "content": "Hello. I am your personal data analyst!",
        }, 
    )
    st.session_state["chat_history"].append(
        {"role": "assistant",
            "content": "May I know who do I have the pleasure of working with today?",
        }, 
    )

st.chat_input("Enter your message", on_submit=chat_actions, key="chat_input")

for i in st.session_state["chat_history"]:
    with st.chat_message(name=i["role"]):
        st.write(i["content"])