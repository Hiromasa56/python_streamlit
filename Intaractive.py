#from nbformat import write
import streamlit as st
from PIL import Image
import time

st.write('プログレスバーの表示')

leatest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    leatest_iteration.text(f'Interation {i+1}')
    bar.progress(i+1)
    time.sleep(0.01)

st.write('レイアウトとインタラクティブ')
st.sidebar.write('Interactive Widgets')

if st.checkbox('Show Image'):    #チェックするかどうかでTrue or Falseを設定できる
    img = Image.open('image.png')
    st.image(img, caption='市場規模', use_column_width=True)

option = st.selectbox(
    '好きな数字は？',
    list(range(1, 11))
)
'選んだのは', option, 'です'

#sidebarを付けると、インタラクティブに動かせる部分がサイドバーに表示されるようになる
text = st.sidebar.text_input('趣味は？')
'趣味:', text

state = st.sidebar.slider('調子は？',0, 100, 50)
'コンディション:', state

#左右に表示と押すと表示
left_column, right_column = st.columns(2)
button = left_column.button('押すと右に文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('もし返品したくなったら')
expander.write('30日以内ならOK')