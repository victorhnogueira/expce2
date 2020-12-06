#Universidade Federal de Uberlândia
#Alunos: Isabela de Carvalho Favareto - 11711EBI025, Maria Luiza de Oliveira R. Pereira - 11811EBI023, Mariana Rigo Estevão - 11711EBI023
#Professor: Wellington Maycon Santos Bernardes
#Matéria: Experimental de Circuitos Elétricos 2
#Tema: Filtros Passivos 

import dash
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate

from cmath import polar, rect
from math import degrees, radians, sqrt
import numpy as np

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = "Filtros Passivos"
app.config['suppress_callback_exceptions']=True
server = app.server

ultima_contagem_de_clique = 0

app.layout = html.Div(children=[
	html.Link(href="https://fonts.googleapis.com/css2?family=Indie+Flower&family=Open+Sans+Condensed:ital,wght@0,300;1,300&display=swap", rel="stylesheet"),
	html.H1("Filtros Passivos"),
	html.H3("Alunos: Isabela de Carvalho Favareto, Maria Luiza de Oliveira R. Pereira e Mariana Rigo Estevão", style={"font-family": 'Open Sans Condensed'}),
  html.H4("Professor: Wellington Maycon Santos Bernardes",  style={"font-family": 'Open Sans Condensed'}),
	dcc.Tabs(id="abas", value="aba-Filtros", children=[
		dcc.Tab(label="Filtros Passivos", value="aba-Filtros Passivos"),
        dcc.Tab(label="Tipos de Filtros", value="aba-Tipos de Filtros"),
		dcc.Tab(label="Calculadora", value="aba-calculadora"),
	]),
	html.Div(id="conteudo"),
])

a = rect(1.0, radians(120))
link_equacao = "https://latex.codecogs.com/svg.latex?{}"
#tensão de fase (Tensão de entrada/sqrt(3) * T)
#tensão de linha (Tensão de entrada/sqrt(3) * variavel_de_conversao)
#correntes linha = fase [(Tensão de entrada/sqrt(3))/Z]

def formatarComplexo(z):
	complexo_polar = polar(z)
	modulo = complexo_polar[0]
	angulo_radianos = complexo_polar[1]
	angulo_graus = degrees(angulo_radianos)
	return "{}\\angle {}\\degree ".format(modulo, angulo_graus)

@app.callback(Output('conteudo', 'children'),
			[Input('abas', 'value')])
def renderizar_aba(aba):
	if aba == "aba-introducao":
		#mostrar conteúdo da parte de informações
		return html.Div(children=[
                        html.Link(href="https://fonts.googleapis.com/css2?family=Indie+Flower&family=Open+Sans+Condensed:ital,wght@0,300;1,300&display=swap", rel="stylesheet"),
                        html.H6("CIRCUITOS TRIFÁSICOS EQUILIBRADOS", style={"font-family": 'Open Sans Condensed'}),
                        html.Br(),
			html.P("O sistema trifásico é equilibrado pelo fato das três tensões, também chamadas de fases, estarem defasadas em 120° uma da outra, quando isso não acontece temos um circuito trifásico desequilibrado."),
                        html.P("Para a geração de tensão alternada trifásica de um gerador, temos três bobinas defasadas em 120 graus elétricos no espaço que geram um conjunto de três tensões de mesmo valor máximo, defasadas de 120 graus elétricos no tempo. Em um gerador trifásico, podemos configurar a conexão das bobinas de diversas formas diferentes, como: ligação em estrela e ligação  em triângulo."),
                        html.Br(),
                        html.Img(src="https://uploaddeimagens.com.br/images/002/897/739/original/gerador.png?1601298591"),
			html.P("Figura 1 - Esquema de gerador com três bobinas defasadas em 120°"),
                        html.Br(),
                        html.Br(),
                        html.H6("LIGAÇÃO ESTRELA", style={"font-family": 'Open Sans Condensed'}),
                        html.Br(),
                        html.P("Na ligação estrela temos um ponto em comum com as três bobinas do circuito, além de um neutro que também se encontra nesse mesmo ponto. Em sistemas trifásicos cujo o fechamento é feito em estrela é possível obter dois níveis de tensão."),
                        html.P("A tensão de linha é medida em uma fase-fase, já a tensão de fase é medida de uma fase com relação ao neutro, entretanto caso a ligação estrela não tenha um neutro o valor da tensão de linha e de fase será a mesma, além disso a corrente de linha é a mesma que a corrente de fase."),
                        html.Br(),
                        html.Img(src="https://uploaddeimagens.com.br/images/002/897/743/original/Esquema_de_liga%C3%A7%C3%A3o_estrela.png?1601298799"),
			html.P("Figura 2 - Esquema de ligação estrela"),
                        html.Br(),
			html.P("De acordo a figura temos:"),
                        html.Br(),
                        html.Img(src="https://uploaddeimagens.com.br/images/002/897/746/original/tabela1.png?1601298868"),
                        html.P("Tabela 01 - Tensões"),
                        html.Br(),
                        html.P("Um gerador conectado em estrela tem a possibilidade de ser configurado em duas sequências de fases diferentes, essa sequência é determinada pela ordem que as tensões das fases passam pelo seu valor máximo."),
                        html.P("Temos a sequência de fase direta (positiva) - ABC e a sequência de fase indireta (negativa) - CBA."),
                        html.Br(),
                        html.Img(src="https://uploaddeimagens.com.br/images/002/897/750/original/Sequ%C3%AAncia_positiva_%28direta%29_-_ABC.png?1601298982"),
                        html.P("Figura 3 - Sequência positiva (direta) - ABC"),
                        html.Br(),
                        html.Img(src="https://uploaddeimagens.com.br/images/002/897/752/original/Diagrama_de_fases_sequ%C3%AAncia_positiva_%28direta%29_-_ABC.png?1601299059"),
                        html.P("Figura 4 - Diagrama de fases sequência positiva (direta) - ABC"),
                        html.Br(),
                        html.Img(src="https://uploaddeimagens.com.br/images/002/897/758/original/Sequ%C3%AAncia_negativa_%28indireta%29_-_CBA.png?1601299237"), 
                        html.P("Figura 5 - Sequência negativa (indireta) - CBA"),
                        html.Br(),
                        html.Img(src="https://uploaddeimagens.com.br/images/002/897/763/original/Diagrama_de_fases_Sequ%C3%AAncia_negativa_%28indireta%29_-_CBA.png?1601299337"), 
                        html.P("Figura 6 - Diagrama de fases Sequência negativa (indireta) - CBA"),
			html.Br(),
                        html.Br(),
                        html.P("- Para uma sequência direta, a tensão de linha é a tensão de fase multiplicada por √3 e adiantada 30º, assim temos a seguinte relação:"),
                        html.Br(),
                        html.Img(src="https://uploaddeimagens.com.br/images/002/897/875/original/for1.png?1601302350"), 
			html.Br(),
                        html.Br(),
                        html.P("- Para uma sequência indireta, tensão de linha é a tensão de fase multiplicada por √3 e atrasada de 30º, assim temos a seguinte relação:"),
                        html.Br(),
                        html.Img(src="https://uploaddeimagens.com.br/images/002/897/878/original/for2.png?1601302419"), 
			html.Br(),
                        html.Br(),
                        html.P("O circuito estrela-estrela abaixo é formado por uma fonte trifásica em estrela equilibrada ligada com uma carga em estrela também em equilíbrio, para esse circuito iremos calcular as correntes de linha, corrente de neutro e as tensões de linha."),
                        html.Br(),
                        html.Img(src="https://uploaddeimagens.com.br/images/002/897/939/original/Untitled_Diagram_%283%29.png?1601304105"),
                        html.P("Figura 7 - Gerador conectado em Y com uma carga conectada em Y"),
                        html.Br(),
                        html.Br(),
                        html.P("Os centros das estrelas n e N estão ao mesmo potencial, e como o trabalharemos com um circuito totalmente equilibrado, a corrente do fio neutro In será zero, assim:"),
                        html.Br(),
                        html.Img(src="https://uploaddeimagens.com.br/images/002/897/916/original/correntes.png?1601303612"),
                        html.Br(),
                        html.Br(),
                        html.P("Para calcular as correntes deste circuito, fizemos seguindo o modelo abaixo."),
                        html.Br(),
                        html.Img(src="https://uploaddeimagens.com.br/images/002/897/921/original/formulacorrente.png?1601303734"),
                        html.Br(),
                        html.Br(),
                        html.P("Após ver a parte teórica é possível realizar os cálculos, ou então,  colocar na nossa calculadora os dados necessários para obter as respostas desejadas."),
                        
		])
	if aba == "aba-calculadora":
		#mostrar conteúdo da parte da calculadora
		return html.Div(children=[
			html.Br(),
                        html.H6("INSTRUÇÕES:", style={"font-family": 'Open Sans Condensed'}),
                        
			dcc.Markdown('''
			> Para inserir as impedâncias use a forma: x+yj, onde x e y são valores numéricos. Se usar x+jy não funcionará.
			>
			> Observações:
			> - Para divisões: use **1j**/z ou z/**1j**;
			> - Para multiplicar por j, use (z)\***1j**, onde Z é um numéro real ou complexo.
			'''),
                        html.Br(),
			dcc.Dropdown(id="seletor-sequencia", value="ABC", clearable=False, options=[
				{"label": "Sequência Direta", "value": "ABC"},
				{"label": "Sequência Inversa", "value": "CBA"}
			]),
			html.Div(style={"display": "flex"}, children=[
				dcc.Input(id="campo-tensao", type="number", placeholder="Valor da tensão"),
				dcc.Input(id="campo-impedancia-linha", type="text", placeholder="Valor da impedância de Linha", style={"flex-grow":'1'}),
				dcc.Input(id="campo-impedancia-fase", type="text", placeholder="Valor da impedância de Fase", style={"flex-grow":'1'}),
				html.Button("Calcular", id="btn-calcular"),
			]),
			html.Div(id="resultado-calculadora")
		])
	return ""

@app.callback(Output('resultado-calculadora', 'children'),
			[Input('seletor-sequencia', 'value'),
			Input('campo-tensao', 'value'),
			Input('campo-impedancia-linha', 'value'),
			Input('campo-impedancia-fase', 'value'),
			Input('btn-calcular', 'n_clicks')])
def calcular(sequencia, tensao, impedancia_linha, impedancia_fase, cliques_btn_calcular):
	global ultima_contagem_de_clique
	if cliques_btn_calcular is not None:
		if cliques_btn_calcular > ultima_contagem_de_clique:
			ultima_contagem_de_clique = cliques_btn_calcular
			if sequencia == "ABC":
				T = np.array([1, a*a, a])
				variavel_de_conversao = rect(sqrt(3), radians(30))
				
				if tensao is None:
					return "Insira a tensão"
				
				matriz_tensoes = (tensao/sqrt(3))*T
				Van = matriz_tensoes[0]
				Vbn = matriz_tensoes[1]
				Vcn = matriz_tensoes[2]

				matriz_tensoes_linha = matriz_tensoes * variavel_de_conversao
				Vab = matriz_tensoes_linha[0]
				Vbc = matriz_tensoes_linha[1]
				Vca = matriz_tensoes_linha[2]

				if impedancia_fase is None:
					return "Insira a impedancia de fase"
				if impedancia_linha is None:
					return "Insira a impedancia de linha (caso não exista, coloque 0)"

				Z = eval(impedancia_fase + "+" + impedancia_linha)

				matriz_correntes = Van/Z * T
				Ian = matriz_correntes[0]
				Ibn = matriz_correntes[1]
				Icn = matriz_correntes[2]

				return html.Div(children=[
					html.Br(),
                                        html.P("Valor eficaz das tensões de linha:"),
					html.Img(src=link_equacao.format("V_{AN_{RMS}} = " + str(formatarComplexo(Van)) + "V" )),
					html.Br(),
					html.Img(src=link_equacao.format("V_{BN_{RMS}} = " + str(formatarComplexo(Vbn)) + "V" )),
					html.Br(),
					html.Img(src=link_equacao.format("V_{CN_{RMS}} = " + str(formatarComplexo(Vcn)) + "V" )),
					html.Br(),
					html.Br(),
                                        html.Br(),
                                        html.P("Valor eficaz das tensões de fase:"),
					html.Img(src=link_equacao.format("V_{AB_{RMS}} = " + str(formatarComplexo(Vab)) + "V" )),
					html.Br(),
					html.Img(src=link_equacao.format("V_{BC_{RMS}} = " + str(formatarComplexo(Vbc)) + "V" )),
					html.Br(),
					html.Img(src=link_equacao.format("V_{CA_{RMS}} = " + str(formatarComplexo(Vca)) + "V" )),
					html.Br(),
					html.Br(),
                                        html.Br(),
                                        html.P("Valor eficaz das correntes:"),
					html.Img(src=link_equacao.format("I_{Afase_{RMS}} = I_{Alinha_{RMS}} = " + str(formatarComplexo(Ian)) + "A" )),
					html.Br(),
					html.Img(src=link_equacao.format("I_{Bfase_{RMS}} = I_{Blinha_{RMS}} = " + str(formatarComplexo(Ibn)) + "A" )),
					html.Br(),
					html.Img(src=link_equacao.format("I_{Cfase_{RMS}} = I_{Clinha_{RMS}} = " + str(formatarComplexo(Icn)) + "A" )),
					html.Br(),
				])
			if sequencia == "CBA":
				T = np.array([1, a, a*a])
				variavel_de_conversao = rect(sqrt(3), radians(-30))

				if tensao is None:
					return "Insira a tensão"
				
				matriz_tensoes = (tensao/sqrt(3))*T
				Van = matriz_tensoes[0]
				Vbn = matriz_tensoes[1]
				Vcn = matriz_tensoes[2]

				matriz_tensoes_linha = matriz_tensoes * variavel_de_conversao
				Vab = matriz_tensoes_linha[0]
				Vbc = matriz_tensoes_linha[1]
				Vca = matriz_tensoes_linha[2]

				if impedancia_fase is None:
					return "Insira a impedancia de fase"
				if impedancia_linha is None:
					return "Insira a impedancia de linha (caso não exista, coloque 0)"
				
				Z = eval(impedancia_fase + "+" + impedancia_linha)

				matriz_correntes = Van/Z * T
				Ian = matriz_correntes[0]
				Ibn = matriz_correntes[1]
				Icn = matriz_correntes[2]

				return html.Div(children=[
					html.Br(),
                                        html.P("Valor eficaz das tensões de linha:"),
                                        html.Img(src=link_equacao.format("V_{AN_{RMS}} = " + str(formatarComplexo(Van)) + "V" )),
					html.Br(),
					html.Img(src=link_equacao.format("V_{BN_{RMS}} = " + str(formatarComplexo(Vbn)) + "V" )),
					html.Br(),
					html.Img(src=link_equacao.format("V_{CN_{RMS}} = " + str(formatarComplexo(Vcn)) + "V" )),
					html.Br(),
                                        html.Br(),
					html.Br(),
                                        html.P("Valor eficaz das tensões de fase:"),
					html.Img(src=link_equacao.format("V_{AB_{RMS}} = " + str(formatarComplexo(Vab)) + "V" )),
					html.Br(),
					html.Img(src=link_equacao.format("V_{BC_{RMS}} = " + str(formatarComplexo(Vbc)) + "V" )),
					html.Br(),
					html.Img(src=link_equacao.format("V_{CA_{RMS}} = " + str(formatarComplexo(Vca)) + "V" )),
					html.Br(),
					html.Br(),
                                        html.Br(),
                                        html.P("Valor eficaz das correntes:"),
					html.Img(src=link_equacao.format("I_{Afase_{RMS}} = I_{Alinha_{RMS}} = " + str(formatarComplexo(Ian)) + "A" )),
					html.Br(),
					html.Img(src=link_equacao.format("I_{Bfase_{RMS}} = I_{Blinha_{RMS}} = " + str(formatarComplexo(Ibn)) + "A" )),
					html.Br(),
					html.Img(src=link_equacao.format("I_{Cfase_{RMS}} = I_{Clinha_{RMS}} = " + str(formatarComplexo(Icn)) + "A" )),
					html.Br(),
				])
	raise PreventUpdate
	return ""

if __name__ == '__main__':
	app.run_server(debug=True)
