#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Leemos los rdf
with open('C:/Users/XDavi/OneDrive/Documentos/Trabajo Web/output_1.nt') as fp:
    data = fp.read()
with open('C:/Users/XDavi/OneDrive/Documentos/Trabajo Web/output_2.nt') as fp:
    data2 = fp.read()
with open('C:/Users/XDavi/OneDrive/Documentos/Trabajo Web/output_3.nt',encoding="utf8") as fp:  # utf8 porque al parecer había caracteres que pertenecía ese encoging
    data3 = fp.read()
with open('C:/Users/XDavi/OneDrive/Documentos/Trabajo Web/output_4.nt') as fp:
    data4 = fp.read()
with open('C:/Users/XDavi/OneDrive/Documentos/Trabajo Web/output_5.nt') as fp:
    data5 = fp.read()
with open('C:/Users/XDavi/OneDrive/Documentos/Trabajo Web/output_6.nt') as fp:
    data6 = fp.read()
with open('C:/Users/XDavi/OneDrive/Documentos/Trabajo Web/output_7.nt') as fp:
    data7 = fp.read()
with open('C:/Users/XDavi/OneDrive/Documentos/Trabajo Web/output_8.nt') as fp:
    data8 = fp.read()
with open('C:/Users/XDavi/OneDrive/Documentos/Trabajo Web/output_9.nt') as fp:
    data9 = fp.read()
with open('C:/Users/XDavi/OneDrive/Documentos/Trabajo Web/output_10.nt') as fp:
    data10 = fp.read()

# Añadimos los datos en un mismo nt

data = data+data2+data3+data4+data5+data6+data7+data8+data9+data10
  
with open ('outputnt.nt', 'w',encoding="utf8") as fp:
    fp.write(data)

