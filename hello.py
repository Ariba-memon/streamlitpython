# # # # import streamlit as st

# # # # # st.write('Hello World from Ariba Memon') # df, err, func, keras!
# # # # # st.text('Fixed width text')
# # # # # st.markdown('_Markdown_ **Pakistan**') # see *

# # # # # st.latex(r''' e^{i\pi} + 1 = 0 ''')  // equation

# # # # # st.write(['st', 'is <', 3]) index object

# # # # # st.title('My title') //h1 heading

# # # # # st.header('My header')
# # # # # st.subheader('My sub')

# # # # # st.code('for i in range(8): foo()') 
# # # # # Draw a title and some text to the app:
# # # # '''
# # # # # This is the document title

# # # # This is some _markdown_.
# # # # '''

# # # # import pandas as pd
# # # # df = pd.DataFrame({'col1': [1,2,3]})
# # # # df  # 👈 Draw the dataframe

# # # # x = 10
# # # # 200
# # # # 'x', x  # 👈 Draw the string 'x' and then the value of x

# # # # # Also works with most supported chart types
# # # # import matplotlib.pyplot as plt
# # # # import numpy as np
# # # # # //pyploty pe same graph
# # # # arr = np.random.normal(1, 1, size=100)
# # # # fig, ax = plt.subplots() 
# # # # # //multiplot bana sakty h
# # # # # histogram graph ki type h
# # # # ax.hist(arr, bins=20)

# # # # fig  # 👈 Draw a Matplotlib chart

# # # # '# Pakistan Zindaabad '
# # # # import module
# # # import streamlit as st
 
# # # # Title
# # # st.title("This is a title")

# # # # Header
# # # st.header("This is a header") 
 
# # # # Subheader
# # # st.subheader("This is a subheader")

# # # # Text
# # # st.text("Hello this is text")

# # # # Markdown
# # # st.markdown("### This is a markdown")

# # # # success
# # # st.success("Success")
 
# # # # success
# # # st.info("Information")
 
# # # # success
# # # st.warning("Warning")
 
# # # # success
# # # st.error("Error")
 
# # # # Exception - This has been added later
# # # exp = ZeroDivisionError("Trying to divide by Zero")
# # # st.exception(exp)

# # # # Write text
# # # st.write("Text with write")
 
# # # # Writing python inbuilt function range()
# # # st.write(range(10))

# # # # Display Images
 
# # # # import Image from pillow to open images
# # # from PIL import Image
# # # img = Image.open("streamlit.png")
 
# # # # display image using streamlit
# # # # width is used to set the width of an image
# # # st.image(img, width=500)

# # # # checkbox
# # # # check if the checkbox is checked
# # # # title of the checkbox is 'Show/Hide'
# # # if st.checkbox("Show/Hide"):
# # #     # display the text if the checkbox returns True value
# # #     st.text("Showing the widget")


# # # # radio button
# # # # first argument is the title of the radio button
# # # # second argument is the options for the radio button
# # # status = st.radio("Select Gender: ", ('Male', 'Female'))
 

# # # # conditional statement to print 
# # # # Male if male is selected else print female
# # # # show the result using the success function
# # # if (status == 'Male'):
# # #     st.success("Male")
# # # else:
# # #     st.success("Female")



# # # # Selection box
 
# # # # first argument takes the title of the selectionbox
# # # # second argument takes options
# # # hobby = st.selectbox("Hobbies: ",
# # #                      ['Dancing', 'Reading', 'Sports'])
 
# # # # print the selected hobby
# # # st.write("Your hobby is: ", hobby)



# # # # multi select box
 
# # # # first argument takes the box title
# # # # second argument takes the options to show
# # # hobbies = st.multiselect("Hobbies: ",
# # #                          ['Dancing', 'Reading', 'Sports'])
 
# # # # write the selected options
# # # st.write("You selected", len(hobbies), 'hobbies')




# # # # Create a simple button that does nothing
# # # st.button("Click me for no reason")
 

# # # # Create a button, that when clicked, shows a text
# # # if(st.button("About")):
# # #     st.text("Welcome To World of Generative AI!!!")



# # # # Text Input
 
# # # # save the input text in the variable 'name'
# # # # first argument shows the title of the text input box
# # # # second argument displays a default text inside the text input area
# # # name = st.text_input("Enter Your name", "Type Here ...")
 
# # # # display the name when the submit button is clicked
# # # # .title() is used to get the input text string
# # # if(st.button('Submit')):
# # #     result = name.title()
# # #     st.success(result)




# # # # slider
 
# # # # first argument takes the title of the slider
# # # # second argument takes the starting of the slider
# # # # last argument takes the end number
# # # level = st.slider("Select the level", 1, 5)
 
# # # # print the level
# # # # format() is used to print value 
# # # # of a variable at a specific position
# # # st.text('Selected: {}'.format(level))

# # # import the streamlit library
# # import streamlit as st
 
# # # give a title to our app
# # st.title('Welcome to BMI Calculator')
 
# # # TAKE WEIGHT INPUT in kgs
# # weight = st.number_input("Enter your weight (in kgs)")
 
# # # TAKE HEIGHT INPUT
# # # radio button to choose height format
# # status = st.radio('Select your height format: ',
# #                   ('cms', 'meters', 'feet'))
 
# # # compare status value
# # if(status == 'cms'):
# #     # take height input in centimeters
# #     height = st.number_input('Centimeters')
 
# #     try:
# #         bmi = weight / ((height/100)**2)
# #     except:
# #         st.text("Enter some value of height")
 
# # elif(status == 'meters'):
# #     # take height input in meters
# #     height = st.number_input('Meters')
 
# #     try:
# #         bmi = weight / (height ** 2)
# #     except:
# #         st.text("Enter some value of height")
 
# # else:
# #     # take height input in feet
# #     height = st.number_input('Feet')
 
# #     # 1 meter = 3.28
# #     try:
# #         bmi = weight / (((height/3.28))**2)
# #     except:
# #         st.text("Enter some value of height")
 
# # # check if the button is pressed or not
# # if(st.button('Calculate BMI')):
 
# #     # print the BMI INDEX
# #     st.text("Your BMI Index is {}.".format(bmi))
 
# #     # give the interpretation of BMI index
# #     if(bmi < 16):
# #         st.error("You are Extremely Underweight")
# #     elif(bmi >= 16 and bmi < 18.5):
# #         st.warning("You are Underweight")
# #     elif(bmi >= 18.5 and bmi < 25):
# #         st.success("Healthy")
# #     elif(bmi >= 25 and bmi < 30):
# #         st.warning("Overweight")
# #     elif(bmi >= 30):
# #         st.error("Extremely Overweight")


# # import streamlit as st

# # st.set_page_config(
# #     page_title="Hello",
# #     page_icon="👋",
# # )

# # st.write("# Welcome to Zia's Page!")

# # st.sidebar.success("Select a demo above.")

# import streamlit as st

# st.title('Counter Example')
# count = 0

# increment = st.button('Increment')
# if increment:
#     count += 1

# st.write('Count = ', count)



# import streamlit as st

# st.title('Counter Example')
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# increment = st.button('Increment')
# if increment:
#     st.session_state.count += 1

# st.write('Count = ', st.session_state.count)


# import streamlit as st

# st.title('Counter Example using Callbacks')
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# def increment_counter():
#     st.session_state.count += 1

# st.button('Increment', on_click=increment_counter)

# st.write('Count = ', st.session_state.count)

# import streamlit as st

# st.title('Counter Example using Callbacks with args')
# if 'count' not in st.session_state:
#     st.session_state.count = 0

# increment_value = st.number_input('Enter a value', value=0, step=1)

# def increment_counter(increment_value):
#     st.session_state.count += increment_value

# increment = st.button('Increment', on_click=increment_counter,
#     args=(increment_value, ))

# st.write('Count = ', st.session_state.count)

# import streamlit as st

# col1, col2, col3 = st.columns(3)
# # col1.header("aa")
# # python with statement
# with col1:
#    st.header("A cat")
#    st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#    st.header("A dog")
#    st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#    st.header("An owl")
#    st.image("https://static.streamlit.io/examples/owl.jpg")

# import streamlit as st
# import numpy as np

# with st.container():
#    st.write("This is inside the container")

#    # You can call any Streamlit command, including custom components:
#    st.bar_chart(np.random.randn(50, 3))

# st.write("This is outside the container")

import streamlit as st
import time

with st.empty():
    for seconds in range(10):
        st.write(f"⏳ {seconds} seconds have passed")
        time.sleep(1)
    st.write("✔️ 10 seconds over!")