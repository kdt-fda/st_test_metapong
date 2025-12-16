import streamlit as st

#1. 상태 여부 체크
if 'counter' not in st.session_state:
    st.session_state.counter=0
# 상태 변경
if st. button('Increment'):
    st.session_state.counter +=1
# 상태 출력/활용
st.write('현재 Increment: {}'.format(st.session_state.counter))