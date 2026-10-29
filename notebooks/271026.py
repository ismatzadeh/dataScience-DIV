# from dataclasses import dataclass
# @dataclass
# class Adam:
#     ad: str
#     soyad: str=None

# adam1 = Adam(ad='vali')


# def adamlaSohbetEle(adam, *args):
#     adaminAdi = adam1.ad
#     print (f"{adaminAdi}, salam,", *args) 

# adamlaSohbetEle('ali', 'necesen?', 'nevar ne yox?')





import streamlit as st
from pathlib import Path

MAIN_DIR = Path(__file__).parent
ADAMLAR_FAYLI = MAIN_DIR / 'adamlar.txt'
 
st.title('salamlar')
st.markdown('Amsterdamdan salamlar')

if st.button('duymeye tikla'):
    st.balloons()

ad = st.text_input('Adinizi yazin')
yash = st.number_input(
    'Yashinizi yazin', 
    min_value=0, 
    max_value=100,
    )

sheher = st.selectbox('doghuldughu sheher?',
                    ['Baki', 'Sumqayit', 'Gence']
)

print(ad)
print(yash)

def adamiSaveEt(*args):
    adaminMelumatlari ='-'.join(args)
    with open(ADAMLAR_FAYLI, mode='a') as f:
        f.writelines(f"{ad} - {yash}\n")
    

if st.button('Yadda saxla'):
    adamiSaveEt(ad, str(yash), sheher)

