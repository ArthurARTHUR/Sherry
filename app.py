import streamlit as st
import datetime

target_date = datetime.date(2025,12,31)

st.sidebar.title('尹雪活爹请输入')
payout_date = st.sidebar.date_input('发放时间:25年底至26年4月30号之间',min_value=datetime.date(2025,12,31),max_value=datetime.date(2026,4,30))
reviewer = st.sidebar.selectbox('年终评审人',['Chery','有人文气息的新老板'])
supplier_of_the_year = st.sidebar.selectbox('哪个供应商最气人',['众鑫','繁荣','都不是好东西'])
self_rating = st.sidebar.radio('年终自评',['S','A','B','C','D'])
working_hour_qualified = st.sidebar.radio('是否242全年打满:',['是','否'])


st.title("尹雪活爹年终奖预测仪",text_alignment='center')
st.divider()
if st.sidebar.button('提交'):
    st.header('预测参数')
    col1, col2 = st.columns(2)
    with col1:
        st.write('年终发放时间:',payout_date)
        st.write('年终评审人:',reviewer)
        st.write('年度垃圾供应商:',supplier_of_the_year)
    with col2:
        st.write('年终自评:',self_rating)
        st.write('是否242全年打满:',working_hour_qualified)
    st.divider()
    st.header('预测结果')
    if self_rating in ['S'] and working_hour_qualified == '否':
        st.warning('你想屁吃，242没有上满，还敢自评S')
        st.warning('0个月的年终奖！')
    elif self_rating in ['A'] and working_hour_qualified == '否':
        st.warning('放屁，242没有上满，还敢自评A')
        st.warning('0个月的年终奖！')
    elif self_rating in ['S','A'] and reviewer == '有人文气息的新老板':
        st.warning('你不是说你新老板连你周报都不听吗，你还自评那么高')
        st.warning('3个月的年终奖！')
    elif self_rating == 'B':
        st.success('B绩效只有一个月年终奖')
    elif self_rating in ['A','S']:
        st.warning('呸，自评那么高，整天想请假')
        st.success('三个月的年终奖')
    else:
        st.warning('C和D没有年终奖')
        st.warning('0个月的年终奖')




