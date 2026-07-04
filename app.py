import streamlit as st

# 페이지 설정
st.set_page_config(page_title="인사하기", page_icon="👋")

# 배경색과 글씨색 설정
st.markdown("""
<style>
.stApp {
    background-color: #0B1F4D;
    color: white;
}

h1, h2, h3, h4, h5, h6, p, div, label {
    color: white !important;
}

.stButton > button {
    background-color: white;
    color: black !important;   /* 버튼 글씨를 검은색으로 변경 */
    font-weight: bold;
    border-radius: 10px;
    padding: 0.5em 1.2em;
}

.stButton > button:hover {
    background-color: #d9d9d9;
    color: black !important;   /* 마우스를 올려도 검은색 유지 */
}
</style>
""", unsafe_allow_html=True)
# 화면 상태 저장
if "page" not in st.session_state:
    st.session_state.page = "main"

# 메인 화면
if st.session_state.page == "main":
    st.markdown(
        "<h1 style='text-align:center;'>👋 안녕하세요</h1>",
        unsafe_allow_html=True
    )

    st.write("")

    if st.button("나도 인사하기"):
        st.session_state.page = "greet"
        st.rerun()

# 인사 화면
elif st.session_state.page == "greet":
    st.markdown(
        "<h2 style='text-align:center;'>🎉 첫 웹페이지 제작을 축하해</h2>",
        unsafe_allow_html=True
    )

    # 축하 효과
    st.balloons()

    st.write("")

    if st.button("돌아가기"):
        st.session_state.page = "main"
        st.rerun()
