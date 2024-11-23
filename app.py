import streamlit as st

st.title('Title -> GeeksForGeeks')   #title
st.header('Title -> GeeksForGeeks')   # header
st.subheader('Title -> GeeksForGeeks')   #subheader
st.text('Title -> GeeksForGeeks')      #text

st.markdown('# GeeksForGeeks')
st.markdown('## GeeksForGeeks')
st.markdown('### GeeksForGeeks')
st.markdown('#### GeeksForGeeks')

st.success('Success')     #success
st.info('Information')    #information
st.warning('Warning')    #WARNING
st.error('Error')        #Error

exp=ZeroDivisionError('Division not possible with zero')   #exception
st.exception(exp)

st.help(ZeroDivisionError)               #help

st.write("range(1,10)")
st.write(range(1,10))
st.write('1+2+3')
st.write(1+2+3)

st.code('x=10 \n'                            #code
        'for i in range(x): \n'
            '\t print(i)')

st.checkbox('Male')                    #checkbox
st.checkbox('Female') #two checkbox of same name is not allowedf
if(st.checkbox('Adult')):              #checkbox with validation
    st.write('You are an adult')

#Radio Button
radioButton = st.radio('select : ', ('Male','Female','Other'))
if(radioButton == 'Male'):
    st.write("You're a Male")
if(radioButton == 'Female'):
    st.write("You're a Female")
if(radioButton == 'Other'):
    st.write("You're a Other Gender")


#Selectbox
st.subheader('SelectBox')
selectBox = st.selectbox("Data Science :", ['Data Analysis','Web Scraping','Machine Learning','Deep Learning',
                          'NLP','Computer Vision'])
st.write("You've selected : ",selectBox)

#Multi-selectBox
st.subheader('MultiSelect Box')
multiSelBox = st.multiselect("Data Science :", ['Data Analysis','Web Scraping','Machine Learning','Deep Learning',
                          'NLP','Computer Vision'])
st.write("You've selected : ",len(multiSelBox), 'courses')

#Button
st.subheader('Button')
st.button('click')
if(st.button('click me')):
    st.write('Thanks for clicking')

#Slider
st.subheader('Slider')
st.slider('Select the level',1,10,step=1)
vol= st.slider('Select the volume',1,50,step=2)
st.write("The volumne is :" , vol)

#text_input
st.subheader("User Input")
name = st.text_input("Enter your name : ")
if(name):
    st.write('hi,',name)
password = st.text_input("Enter password : ", type='password')

#textArea   use to write a paragraphs
st.subheader("Text Area")
textArea = st.text_area("Write something interesting about yourself in 500 words")
st.write(textArea)

#Input-Number
st.subheader("Input Number")
st.number_input("Select your age",18,110)

#Input-Date
st.subheader("Input Date")
st.date_input("Date")

#Input-Time
st.subheader("Input Time")
st.time_input("Time")
