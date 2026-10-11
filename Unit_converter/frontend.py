import streamlit as st

from backend import list_quantities,list_units,convert_value,format_value

st.title("Unit Converter")

with st. sidebar:
    quantity=st.radio("Select a quantity",list_quantities())
units=list_units(quantity)
from_unit_col,to_unit_col=st.columns(2)
with from_unit_col:
    from_unit = st.selectbox("From", units)
with to_unit_col:
    to_unit = st.selectbox("To", units, index=1)
#input_num=float(st.text_input("Value to convert",value=0))
input_num = st.number_input("Value to convert",value=0.0,step=1.0,format="%f")
places=None
if st.checkbox("Round result?",value=False):
    places=st.number_input("Decimal places to round to",value=2,min_value=0)
result=convert_value(quantity,from_unit,to_unit,input_num)
from_display=format_value(result.from_value,result.from_unit.abbrev)
to_display=format_value(result.to_value,result.to_unit.abbrev,places)
from_value_col,to_value_col=st.columns(2)
from_value_col.metric("From",from_display,delta=None)
to_value_col.metric("To",to_display,delta=None)