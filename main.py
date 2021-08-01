from selenium import webdriver
import json
navegador = webdriver.Chrome()
'''
Link para a app br: http://177.71.114.188/58  (58 é um numero exemplificativo)      Xpath: /html/body/pre
 
Link para a app en: http://177.71.114.188/en/58  (58 é um numero exemplificativo)   Xpath: /html/body/pre
'''
nums = [1, 5, 12, 300, 999, -1, -5, -12, -300, -999]
txt_nums_BR = ["um", "cinco", "doze", "trezentos", "novecentos e noventa e nove", "menos um", "menos cinco",
               "menos doze", "menos trezentos", "menos novecentos e noventa e nove"]
txt_nums_EN = ["one", "five", "twelve", "three hundred", "nine hundred ninety nine", "minus one", "minus five",
               "minus twelve", "minus three hundred", "minus nine hundred ninety nine"]

resultado = ""
acerto = 0
erros = 0

for i in range(10):
    url = "http://177.71.114.188/" + str(nums[i])
    navegador.get(url)
    navegador.implicitly_wait(5)
    resultado = navegador.find_element_by_xpath('/html/body/pre').text
    resultado = json.loads(resultado)
    if resultado["extenso"] == txt_nums_BR[i]:
        acerto += 1
    else:
        print("Erro na app BR, conversão do numero " + str(nums[i]))
        erros += 1

if (acerto == 10):
    print("Tudo certo com a aplicação em Protuguês")
if (erros > 0):
    print("Teve " + str(erros) + " erros na app BR")

acerto = 0
erros = 0
for i in range(10):
    url = "http://177.71.114.188/en/" + str(nums[i])
    navegador.get(url)
    navegador.implicitly_wait(5)
    resultado = navegador.find_element_by_xpath('/html/body/pre').text
    resultado = json.loads(resultado)
    if resultado["full"] == txt_nums_EN[i]:
        acerto += 1
    else:
        print("Erro na app EN, conversão do numero " + str(nums[i]))
        erros += 1

if (acerto == 10):
    print("Tudo certo com a aplicação em Inglês")
if (erros>0):
    print("Teve "+str(erros)+" erros na app EN")

navegador.close()





