byte_st = b'\xc3\xa9sum\xc3\xa9'

decode_st = byte_st.decode('utf-8')

print(decode_st)

latin_st = decode_st.encode('latin1')

print(latin_st)

decode_latin = latin_st.decode('latin1')

print(decode_latin)
