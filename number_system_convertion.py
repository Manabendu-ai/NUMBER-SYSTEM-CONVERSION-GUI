import streamlit as st

class NumberSystemConversion():
    def __init__(self):
        st.markdown("## Number System Conversion")
        st.session_state['ns1'] = st.selectbox("SOURCE ",['DECIMAL','BINARY','OCTAL','HEXA'])
        st.session_state['n1'] = st.text_input(f'source input: {st.session_state['ns1'].lower()}')
        st.session_state['ns2'] = st.selectbox("TARGET ",['DECIMAL','BINARY','OCTAL','HEXA'])
        st.session_state['btn'] = st.button('RUN')
        if st.session_state['n1'] or st.session_state['btn']:
            try:
               data = self.convert(st.session_state['ns1'], st.session_state['ns2'],st.session_state['n1'].lower())
               if data == None:
                   st.warning(f"source and target are same:  {st.session_state['n1']}")
               else:
                  st.session_state['res'] = st.success(f"{self.format(data)}")
            except Exception:
                st.warning("Invalid input with base!")


    def format(self, data):
        if isinstance(data, int):
            return data
        return str(data)[2:]
        
    
    def convert(self, source, target, val):
        if source == "DECIMAL" and target == "BINARY":
            return bin(int(val))
        elif source == "DECIMAL" and target == "HEXA":
            return hex(int(val))
        elif source == "DECIMAL" and target == "OCTAL":
            return oct(int(val))
        elif source == "BINARY" and target == "OCTAL":
            return oct(int(val, 2))
        elif source == "BINARY" and target == "DECIMAL":
            return int(val, 2)
        elif source == "BINARY" and target == "HEXA":
            return hex(int(val, 2))
        elif source == "HEXA" and target == "OCTAL":
            return oct(int(val,16))
        elif source == "HEXA" and target == "BINARY":
            return bin(int(val, 16))
        elif source == "HEXA" and target == "DECIMAL":
            return int(val, 16)
        elif source == "OCTAL" and target == "HEXA":
            return hex(int(val,8))
        elif source == "OCTAL" and target == "BINARY":
            return bin(int(val, 8))
        elif source == "OCTAL" and target == "DECIMAL":
            return int(val, 8)
        
        

nums = NumberSystemConversion()

