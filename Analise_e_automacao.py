#!/usr/bin/env python
# coding: utf-8

# <h3 style="color: #2F666F">O que é o Yahoo Finanças?</h3>
# 
# - Site que fornece notícias sobre finanças, incluindo **cotações de ações**
# - Link: [https://br.financas.yahoo.com/](https://br.financas.yahoo.com/).

# <h3 style="color: #2F666F"> Instalar biblioteca (A instalação precisa ser feita apenas uma vez)</h3>

# In[3]:


get_ipython().system('pip install yfinance')


# <h3 style="color: #2F666F">Usando/chamando a biblioteca (Sempre que for preciso usar, deve ser chamada novamente no código)</h3>

# In[4]:


import yfinance


# *texto em itálico*<h3 style="color: #2F666F">Buscando as cotações de uma Ação</h3>
# 
# - **Ticker** é o código de uma ação.

# In[6]:


ticker = input('Digite o código da ação: ')
dados = yfinance.Ticker(ticker)


# In[7]:


dados.history()


# <h4>Configurando o período histórico</h4>
# 
# - **Ano:** y
# - **Mês:** mo
# - **Dia:** d

# In[10]:


tabela = dados.history("6mo") #Onde está "mo", pode ser colocado umas das opções citadas acima. O valor 6 se refere a quantidade de meses que será apresentado.
tabela


# # <h3 style="color: #2F666F">Selecionando apenas a coluna de Fechamento (Close)</h3>
# 
# - Para selecionar a coluna desejada, basta colocar o nome dela entre colchetes na frente da variável que está armazenando os dados

# In[12]:


fechamento = tabela.Close
fechamento


# <h3 style="color: #2F666F">Gerando um gráfico de linha</h3>
# 
# - Vamos gerar um gráfico muito simples, apenas utilizando o método **.plot()**

# In[14]:


fechamento.plot()


# <h3 style="color: #2F666F">Gerando as estatísticas</h3>
# 
# - Gerar estatísticas no Python é muito simples, pois já temos os métodos prontos para serem aplicados!
# 
# 
# - **cotação máxima:** max()
# - **votação mínima:** min()
# - **cotação atual:** é a última linha!Para acessá-la basta colocar [-1]

# In[15]:


maxima = fechamento.max()
minima = fechamento.min()
atual = fechamento[-1]

print(maxima)
print(minima)
print(atual)


# <h2 style="color: #37709F">Enviando e-mail de forma automática</h2>
# 
# - Processo de enviar um e-mail passo a passo:
#     - abrir uma nova aba no navegador (clicar em + ou CTRL + T)
#     - digitar o endereço do gmail (www.gmail.com) e digitar ENTER
#     - clicar em **Escrever**
#     - digitar o endereço de e-mail do destinatário
#     - mudar para o campo Assunto (clicar no campo ou digitar tab)
#     - digitar o Assunto
#     - mudar para campo principal do e-mail (clicar no campo ou digitar tab)
#     - escrever a mensagem
#     - clicar em **Enviar**

# <h3 style="color: #2F666F"> Instalar biblioteca (A instalação precisa ser feita apenas uma vez)</h3>

# In[16]:


get_ipython().system('pip install pyautogui #Fornece métodos para controlar mouse e teclado.')


# In[17]:


get_ipython().system('pip install pyperclip #Pyperclip é um módulo Python de plataforma cruzada para copiar e colar funções da área de transferência. ')


# <h3 style="color: #2F666F">Usando/chamando a biblioteca (Sempre que for preciso usar, deve ser chamada novamente no código)</h3>

# In[18]:


import pyautogui
import pyperclip


# <h3 style="color: #2F666F">Criando o e-mail para envio das informações</h3>

# In[19]:


destinatario = "raphaelag3@gmail.com"
assunto = "Análise diária"

mensagem = f"""  
Bom dia,

Segue abaixo as análises da ação {ticker} dos últimos seis meses:

Cotação máxima: R${round(maxima,2)}
Cotação mínima: R${round(minima,2)}
Cotação atual: R${round(atual,2)}

Atenciosamente,
Seu nome.
"""


# #### As f-strings vão servir para que você consiga colocar uma variável dentro de um texto, e isso é feito utilizando a letra “f” antes do texto e colocando a sua variável dentro de {}

# In[20]:


print(destinatario)
print(assunto)
print(mensagem)


# <h3 style="color: #2F666F">Automatizando o envio do email</h3>

# In[28]:


# configurar uma pausa entre as ações do pyautogui
pyautogui.PAUSE = 3 #3 segundos

# abrir uma nova aba
pyautogui.hotkey("ctrl", "t")

# copiar o endereço do gmail para o clipboard
pyperclip.copy("www.gmail.com")

# colar o endereço do gmail e dar um ENTER
pyautogui.hotkey("ctrl", "v")
pyautogui.press("enter")

# clicando no botão Escrever
pyautogui.click(x=106, y=220)

# Preenchendo o destinatário
pyperclip.copy(destinatario)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Preenchendo o assunto
pyperclip.copy(assunto)
pyautogui.hotkey("ctrl", "v")
pyautogui.press("tab")

# Preenchendo a mensagem
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl", "v")

# Clicar no botão Enviar
pyautogui.click(x=1265, y=1012)

# fechar a aba do gmail
pyautogui.hotkey("ctrl", "f4")

# Imprimir mensagem de enviado com sucesso
print('E-mail enviado com sucesso!')


# In[27]:


import time

time.sleep(5)
pyautogui.position() #função usada para descobrir a posição onde o mouse está


# In[ ]:




