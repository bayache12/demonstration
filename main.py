import streamlit as st
from streamlit_lottie import st_lottie
import requests
import boto3
import openai

st.set_page_config(page_title='Elastik Teacher', page_icon=':rocket:', layout='wide')
textractclient = boto3.client('textract', aws_access_key_id=st.secrets['aws_key_sec'],
                              aws_secret_access_key=st.secrets['aws_secret_access_sec'], region_name="eu-west-2")
openai.api_key = st.secrets['openai_key_sec']


def img_to_text(img):
    response = textractclient.detect_document_text(
        Document={
            'Bytes': img.getvalue()},
    )

    listo = []

    for i in response['Blocks']:
        if i['BlockType'] == 'LINE':
            try:
                listo.append(i['Text'])
            except:
                continue

    return "\n".join(listo)


def get_openai_input(prompt, converted_text):
    return st.secrets['prompt_text'].format(prompt = prompt, converted_text = converted_text)


def get_grade(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.3,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


st.image('MicrosoftTeams-image.png')
st.title("elastik, _Teacher_ in a Pocket")

st.write("---")

st.subheader('Before your work can be graded, choose the prompt used and upload your handwritten piece of work!🤔')

option = st.selectbox(
    'Which of these prompts is the students handwritten work based off of?',
    ('Which is Better?', 'The Sign', '''Don't waste it''', 'The Gate.',
     'Cooking is a Skill that Everyone Should Learn'))

file = st.file_uploader('Upload your image or scan here! 👇', type=None, accept_multiple_files=False, key=None,
                        help=None,
                        on_change=None, args=None,
                        kwargs=None, disabled=False, label_visibility="visible")
st.write('---')
if file != None:
    placeholder = st.empty()
    with placeholder.container():
        title_api = st.title('Getting Student Mark...')
        st_lottie(load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_usmfx6bp.json'), height=300,
                  key='loading')
        new_text = img_to_text(file)
        testo = get_grade(get_openai_input(option, new_text))
    with placeholder.container():
        placeholder = st.empty()
        grades = [i for i in testo.split('\n') if len(i.strip()) > 1]
        print(grades)
        lottie_gifs = [i for i in open('lotties.txt').readlines()]
        st.subheader(grades[0])
        st_lottie(load_lottieurl('https://assets3.lottiefiles.com/private_files/lf30_pSQ3W3.json'), height=300,
                  key='first')
        st.write('---')
        st.subheader(grades[1])
        st_lottie(load_lottieurl('https://assets6.lottiefiles.com/packages/lf20_7xeqfabo.json'), height=300,
                  key='second')
        st.write('---')
        st.subheader(grades[2])
        st_lottie(load_lottieurl('https://assets9.lottiefiles.com/packages/lf20_fboneztl.json'), height=300,
                  key='third')
        st.write('---')
        st.subheader(grades[3])
        st_lottie(load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_N3IbTTWRWt.json'), height=300,
                  key='fourth')
        st.write('---')
        st.subheader(grades[4])
        st_lottie(load_lottieurl('https://assets7.lottiefiles.com/packages/lf20_eIphcV4GJ1.json'), height=300,
                  key='five')
        st.write('---')
        st.subheader(grades[5])
        st_lottie(load_lottieurl('https://assets5.lottiefiles.com/packages/lf20_7htpyk2w.json'), height=300, key='six')
        st.write('---')
        st.subheader(grades[6])
        st_lottie(load_lottieurl('https://assets3.lottiefiles.com/packages/lf20_xwgclkyh.json'), height=300,
                  key='seven')
        st.write('---')
        st.subheader(grades[7])
        st_lottie(load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_kwozkvd1.json'), height=300,
                  key='eight')
        st.write('---')
        st.subheader(grades[8])
        st_lottie(load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_DMgKk1.json'), height=300, key='nine')
        st.write('---')
        st.subheader(grades[9])
        st_lottie(load_lottieurl('https://assets9.lottiefiles.com/private_files/lf30_TBKozE.json'), height=300,
                  key='coding')
        st.write('---')
        st.subheader(grades[10])
        st_lottie(load_lottieurl('https://assets1.lottiefiles.com/packages/lf20_8QyKOkeQV8.json'), height=300,
                  key='eleven')
        st.write('---')
