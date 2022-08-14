import streamlit as st

st.title('10 Cool Beginner Python Tricks That Will Make Your Life Easier')
st.write('Simple but effective tips for every python lovers')

st.write("The compactness of Python can make a developer’s life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities. \nIn today’s article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time.")

st.subheader('1. Walrus operator')
st.write("The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc.")
st.code('Mylist = [1,2,3]\nif(l := len(mylist) > 2) \nprint(l)')
st.write('Output:')
st.code('3')

st.subheader('2. Splitting a string')
st.write("If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier!")
st.code('string = “hello world” \nstring.split()')
st.write('Output:')
st.code('[‘hello’, ‘world’]')

st.subheader('3. Reversing a string')
st.write("If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string.")
st.code('str=”hello world!” \na=str[::-1] \nprint(a)')
st.write('Output:')
st.code('!dlrow olleh')

st.subheader('4. Merging two dictionaries')
st.write("This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary:")
st.code('d1 = {“a”: 10, “b”:20} \nd2 = {“c”: 30, “d”:40} \nd3 = {**d1, **d2} \nprint(d3)')
st.write('Output:')
st.code('{‘a’: 10, ‘b’: 20, ‘c’: 30, ‘d’: 40}')

st.subheader('5. The zip() function')
st.write("The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length.")
st.code('colour = [“red”, “yellow”, “green”] \nfruits = [‘apple’, ‘banana’, ‘mango’] \nfor colour, fruits in zip(colour, fruits):\nprint(colour, fruits)')
st.write('Output:')
st.code('red apple \nyellow banana \ngreen mango')
