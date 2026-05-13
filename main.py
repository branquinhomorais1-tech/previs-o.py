import streamlit as st
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression

st.title('ensinar a máquina a prever o futuro')
st.write('preve o campeão da copa')

st.header('opções de campeão...')

#dados -
#
Dados = pd.DataFrame ({
'gols':[12,15,10,18,14,11,16],
'ranking':[1,3,2,1,4,10,2],
'pais':['Brasil', 'Argentina','França','Brasil', 'França','Argentina']

})

# alinhamento do modelo
modelo_copa = DecisionTreeClassifier
modelo_copa.fit(Dados[['gols','ranking']], Dados['país'])

gols_input = st.number_input('Quantos gols o time fez?'),0,30,15
rank_input = st.number_input('Qual e a posição',1,100,1)
if st.button ('prever'):
    #previsão
    resultado_copa = modelo_copa.predict ([[gols_input, rank_input]])
    st.success(f' O provavel campeão é {resultado_copa}')
    Dados = pd.DataFrame
    #----------------------------------------------------------
    

    import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")
```python
import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.header("Previsão de Vendas")

# Dados: [Investimento em Marketing] -> Faturamento
dados_vendas = pd.DataFrame({
    'investimento': [100, 200, 300, 400, 500, 600],
    'faturamento': [1200, 2500, 3200, 4800, 5100, 6300]
})

# objetivo: previsão de FATURAMENTO 

previsão_faturamento = DecisionTreeClassifier
previsão_faturamento.fit(Dados[ 'investimento': [100, 200, 300, 400, 500, 600]]) (Dados[['faturamento' 1200, 2500, 3200, 4800, 5100, 6300]])
