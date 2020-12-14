# -*- coding: utf-8 -*-
# Universidade Federal de Uberlândia - Faculdade de Engenharia Elétrica
# Alunos: André de Souza Dantas - 11521EBI009, Rafael Pagotto Miguel - 11321EBI021, Victor Hugo Nogueira de Carvalho – 11621EBI017
# Disciplina: Experimental de Circuitos Elétricos 2
# Professor: Wellington Maycon Santos Bernardes
# Tema: Circuitos Trifásicos Desequilibrados

# Importa as bibliotecas usadas
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Define variables
apptitle = "Circuitos Trifásicos Desequilibrados"

# Initiate app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css', 'https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title=apptitle
server = app.server

# Set up the layout
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Pagina Home "/"
index_page = html.Div(children=[
 # Cabecalho de navegacao entre paginas
 html.Div(className='bg-primary', children=[
  html.Div(className='container d-flex flex-row align-items-center', style={'padding':'10px 0 10px 0', 'color':'white'} , children=[
   dcc.Link('Circuitos Trifásicos Desequilibrados', style={'fontSize': '22px', 'color': 'white', 'textDecoration': 'none', 'fontWeight': 'bold'}, href='/'),
   html.Div(className='right', style={'fontSize': '16px', 'position': 'absolute', 'right':'0'} , children=[
    dcc.Link('Teoria', href='/teoria', style={'marginRight': '10px', 'color': 'white'}),
    dcc.Link('Simulações', href='/simulacoes', style={'marginRight': '10px', 'color': 'white'}),
    dcc.Link('Sobre', href='/sobre', style={'marginRight': '10px', 'color': 'white'})
   ])
  ])
 ]),
 # Corpo da página
 html.Div(className='container', style={'marginTop': '20px', 'fontSize': '16px'}, children=[
  html.H1('INTRODUÇÃO'),
  html.P('Visto que os circuitos apresentam desequilíbrios em várias situações e circuitos desequilibrados são de uso cotidiano de parte da população, é notável a importância do estudo e da compreensão do comportamento desses sistemas.'),
  html.P('Costuma-se usar um sistema de quatro fios (3F+1N) para manter a tensão estável ao fornecer um caminho para a corrente de neutro, oriunda do desequilíbrio de tensão, garantindo maior eficiência na distribuição de energia e consequentemente entregando uma maior potência ativa ao circuito, o que otimiza o funcionamento do sistema a partir da redução de perdas desnecessárias de potência e energia.'),
  html.Br(),
  html.H1('CIRCUITOS TRIFÁSICOS'),
  html.Br(),
  html.Div(className='d-flex', children=[
   html.Div(style={'margin': '5px'}, children=[
    html.H3('Estrela'),
    html.Img(src="https://i.imgur.com/U6sCduq.png")]),
   html.Div(style={'margin': '5px'}, children=[
    html.Br(),
    html.Img(src="https://i.imgur.com/kZQFUEw.png")
   ])
  ]), 
  html.Br(),
  html.H3('Triangulo'),
  html.Img(src="https://i.imgur.com/3Sq7CQL.png"), 
 ])
])

# Pagina Teoria "/teoria"
teoria_page = html.Div(children=[
 # Cabecalho de navegacao entre paginas
 html.Div(className='bg-primary', children=[
  html.Div(className='container d-flex flex-row align-items-center', style={'padding':'10px 0 10px 0', 'color':'white'} , children=[
   dcc.Link('Circuitos Trifásicos Desequilibrados', style={'fontSize': '22px', 'color': 'white', 'textDecoration': 'none', 'fontWeight': 'bold'}, href='/'),
   html.Div(className='right', style={'fontSize': '16px', 'position': 'absolute', 'right':'0'} , children=[
    dcc.Link('Teoria', href='/teoria', style={'marginRight': '10px', 'color': 'white'}),
    dcc.Link('Simulações', href='/simulacoes', style={'marginRight': '10px', 'color': 'white'}),
    dcc.Link('Sobre', href='/sobre', style={'marginRight': '10px', 'color': 'white'})
   ])
  ])
 ]),
 # Corpo da página
 html.Div(className='container', style={'marginTop': '20px', 'fontSize': '16px'}, children=[
  html.H1('CIRCUITOS TRIFÁSICOS DESEQUILIBRADOS'),
  html.Br(),
  html.H2('Situações de desequilíbrio:') ,
  html.P('Os circuitos trifásicos se encontram em desequilíbrio devido a carga, caso haja alguma variação entre as distribuições de cargas, ou pela variação da demanda. No caso do desequilíbrio oriundo das fontes, esse se deve a diferentes tensões e/ou fasores entre as elas.'),
  html.Br(),
  html.H2('Análises:'),
  html.P('Sistema 3F+N'),
  html.P('Esses sistemas podem ser resolvidos por meio das análises de malha ou nodal, já sabendo que as impedâncias são diferentes então usa-se as seguintes equações para determinar as correntes.'),
  html.Br(),
  html.P('Ia=  Van/Za;          Ib=  Vbn/Zb;            Ic=  Vcn/Zc.'),
  html.P('Visto que as correntes de linha apresentaram valores distintos,conclui-se que a corrente no neutro é diferente de zero e pode ser encontrada a partir de:'),
  html.P('In = -(Ia+Ib+Ic)'),
  html.P('A presença do neutro mantém a estabilidade das tensões de fase nas cargas. No caso da desconexão do mesmo, é gerada uma diferença de potencial entre o ponto neutro da fonte e o ponto neutro da carga, por isso, as tensões de fase na carga não são as mesmas tensões de fase provenientes da fonte. '),
  html.H3('Sistema 3F'),
  html.P('Quando há três fios em estrela, sem terra, a tensão de linha AB se dá do maior potencial para o menor, e assim sucessivamente. No caso abaixo, lidando com o maior potencial sendo o de A:'),
  html.Img(src="https://i.imgur.com/ocTDiQr.png"), 
  html.P('Vab = (Ian * Za) -  (Ibn * Zb)'),
  html.P('Vbc = (Ibn * Zb) - (Icn * Zc)'),
  html.P('Vca = (Icn * Zc) - (Ian * Za)'),
  html.H4('Então:'),
  html.P('Ian = [(Vab * Zc) - (Vca * Zb)] / (Za*Zb) + (Za*Zc) + (Zb*Zc)'),
  html.P('Ibn = [(Vbc * Za) - (Vab * Zc)] / (Za*Zb) + (Za*Zc) + (Zb*Zc)'),
  html.P('Icn = [(Vca * Zb) - (Vbc * Za) / (Za*Zb) + (Za*Zc) + (Zb*Zc)'),
  html.H3('Potências:'),
  html.P('Unidades de medida (W) Watts, (VA) Volt-Ampere, (VAr) Volt-Ampere reativo.'),
  html.H3('Triângulo de potências:'),
  html.Img(src="https://i.imgur.com/WR64uBv.png"),
  html.H3('Fator de potência'),
  html.P('cos φ : Factor de Potência'),
  html.P('P[W]/S[VA] = cos φ'),
  html.P('Um baixo fator de potência da carga é causa de perdas na linha de alimentação devido a quedas de tensão na linha por excesso de corrente'),
  html.H3('Ativa'),
  html.P('P = (VI cos φ) ← Potência Ativa (W)'),
  html.P('Potência consumida pelo equipamento'),
  html.H3('Reativa'),
  html.P('Q = S sen φ ← Potência Reativa (VAr)'),
  html.P('Energia trocada entre a fonte e a carga (conjunto bobina e condensador) Potencia ‘inútil’, perdas.'),
  html.H3('Aparente'),
  html.P('P = S cos φ ← S: Potência Aparente (VA)'),
  html.P('Valor nominal de equipamentos de potência, ex: transformadores. Magnitude da potência total.'),
  html.H2('Aplicações'),
  html.P('Os sistemas desequilibrados são vistos por exemplo, em situações em que uma distribuição possui duas residências e uma indústria, cujos equipamentos possuem uma necessidade maior do que os residenciais. A presença do neutro visa a manutenção do fornecimento de tensão estável, por possibilitar um trajeto para In, que resulta do desequilíbrio de tensão.'),
  html.P('Existe uma norma que trata do valor máximo de desequilíbrio permitido, que o estabelece como 20%, e caso esse valor seja atingido ou até ultrapassado, mudanças precisaram ser feitas. Uma diferença de corrente nas fases de um circuito primário, pode aumentar bastante a queda de tensão na fase com maior carga, o que pode gerar uma corrente no neutro em decorrência de um desequilíbrio na tensão'),
  html.H2('CONCLUSÃO'),
  html.P('A partir da análise dos circuitos foi notada uma perda de potência ativa devido a existência de uma diferença de potencial entre os neutros das cargas e o das fontes. No caso da conexão dos dois neutros, conclui-se que ambos se tornam agora equipotenciais, reduzindo a perda de corrente oriunda da diferença de potencial que existia entre eles.'),
  html.H2('REFERÊNCIAS'),
  html.P('[1]HART, W. Daniel. Eléctronica de Potencia. Madrid: Pearson Educación, 2001. Disponível em:https://www.amperonline.com/sites/library/Electronica%20de%20Potencia.%201ra-Edicion-Daniel-W-Hart.pdf. Acesso em 06 de dez. de 2020. '),
  html.P('[2]SANTOS, N. José. Compensação do Factor de Potência. FEUP, 2006. Disponível em: https://paginas.fe.up.pt/~jns/material_didatico/CorreccaoFactorPotenciaFinal.pdf. Acesso em 04 de dez. de 2020.'),
  html.P('[3] GOMES, V. Flávio. Circuitos Trifásicos Equilibrados e Desequilibrados. UFJF, 2012. Disponível em: https://www.ufjf.br/flavio_gomes/files/2012/11/Aula-04_ENE005.pdf. Acesso em: 26 de nov. de 2020.'),
  html.P('[4] BOYLESTAD, L. Robert. Análise de Circuitos. 12. Ed. – São Paulo: Pearson Prentice Hall, 2012.'),
 ])
])

# Pagina Sobre "/sobre"
aboutus_page = html.Div(children=[
 # Cabecalho de navegacao entre paginas
 html.Div(className='bg-primary', children=[
  html.Div(className='container d-flex flex-row align-items-center', style={'padding':'10px 0 10px 0', 'color':'white'} , children=[
   dcc.Link('Circuitos Trifásicos Desequilibrados', style={'fontSize': '22px', 'color': 'white', 'textDecoration': 'none', 'fontWeight': 'bold'}, href='/'),
   html.Div(className='right', style={'fontSize': '16px', 'position': 'absolute', 'right':'0'} , children=[
    dcc.Link('Teoria', href='/teoria', style={'marginRight': '10px', 'color': 'white'}),
    dcc.Link('Simulações', href='/simulacoes', style={'marginRight': '10px', 'color': 'white'}),
    dcc.Link('Sobre', href='/sobre', style={'marginRight': '10px', 'color': 'white'})
   ])
  ])
 ]),
 # Corpo da página
 html.Div(className='container', style={'marginTop': '20px', 'fontSize': '16px'}, children=[
  html.H1('Sobre'),
  html.Br(),
  html.H3('Alunos'),
  html.P('André de Souza Dantas - 11521EBI009'),
  html.P('Rafael Pagotto Miguel - 11321EBI021'),
  html.P('Victor Hugo Nogueira de Carvalho - 11621EBI017'),
  html.Br(),
  html.P('Professor: Wellington Maycon Santos Bernardes'),
  html.P('Tema: Circuitos Trifásicos Desequilibrados'),
  html.P('Disciplina Experimental de Circuítos Elétricos 2 - Turma E3')
 ])
])

# Pagina Simulacao "/simulacoes"
simulacao_page = html.Div(children=[
 # Cabecalho de navegacao entre paginas
 html.Div(className='bg-primary', children=[
  html.Div(className='container d-flex flex-row align-items-center', style={'padding':'10px 0 10px 0', 'color':'white'} , children=[
   dcc.Link('Circuitos Trifásicos Desequilibrados', style={'fontSize': '22px', 'color': 'white', 'textDecoration': 'none', 'fontWeight': 'bold'}, href='/'),
   html.Div(className='right', style={'fontSize': '16px', 'position': 'absolute', 'right':'0'} , children=[
    dcc.Link('Teoria', href='/teoria', style={'marginRight': '10px', 'color': 'white'}),
    dcc.Link('Simulações', href='/simulacoes', style={'marginRight': '10px', 'color': 'white'}),
    dcc.Link('Sobre', href='/sobre', style={'marginRight': '10px', 'color': 'white'})
   ])
  ])
 ]),
 # Corpo da página
 html.Div(className='container', style={'marginTop': '20px', 'fontSize': '16px'}, children=[
  html.H1('GRÁFICOS'),
  html.Br(),
  html.H3('Dado o seguinte circuito:'),
  html.Img(src="https://i.imgur.com/bA022gn.png"),
  html.Img(src="https://i.imgur.com/RpZavtT.png"),
  html.P('No sistema 3F+N, as correntes são diferentes, e para manter as tensões das cargas semelhantes àquelas das fontes, a corrente no neutro chega a quase 1A. As concessionárias indicam o uso do Neutro exatamente para manter os valores de tensão na carga.'),
  html.Img(src="https://i.imgur.com/xr286Ro.png", style={'maxWidth':'100%', 'width': '600px'}),
  html.P('O desequilíbrio pode fazer com que a tensão nas cargas seja maior do que a tensão das fontes. Nesse caso, a tensão em Vbn passa de 180V, enquanto a tensão da fonte era de 115V. Van = 148V e  Vcn = 51V.'),
 ])
])

 # Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])

# Funcao que determina a nevagacao entre paginas
def display_page(pathname):
    if pathname == '/':
        return index_page
    elif pathname == '/teoria':
        return teoria_page
    elif pathname == '/simulacoes':
        return simulacao_page
    elif pathname == '/sobre':
        return aboutus_page
    else:
        return index_page
 
if __name__ == '__main__':
 app.run_server(debug=True)