import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers 




def get_Llama2_output(input_text, no_words, blog_style):

    Llama2 = CTransformers(model = 'models/llama-2-7b-chat.ggmlv3.q8_0.bin', model_type = 'llama', 
                           config = { 'max_new_tokens':256,
                                      'temperature':0.01 })

    template = """
    Write a blog for {blog_style} job profile for a topic {input_text}
    within {no_words} words.
    """

    prompt = PromptTemplate(input_variables = ['blog_style', 'input_text', 'no_words'], template = template )


    response = Llama2(prompt.format(blog_style = blog_style, input_text = input_text, no_words = no_words))
    print(response)

    return response






st.set_page_config(page_title = 'Generate Blogs', layout = 'centered')

st.header('Generate Blogs')

# Taking the input
input_text = st.text_input('Enter the Blog Topic')


# Two Inputs for Number of words and Blog style
column1, column2 = st.columns([5,5])


with column1:
    no_words = st.text_input('Number of Words')
with column2:
    blog_style = st.selectbox('Writing the Blog for', ('Researchers', 'Data Scientist', 'Common People'), index = 0)

submit = st.button("Generate")


if (submit):
    st.write(get_Llama2_output(input_text, no_words, blog_style))


