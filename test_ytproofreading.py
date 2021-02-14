import ytproofreading

appid = "Client ID obtained from the Yahoo! japan Developer Network"

kousei = ytproofreading.Kousei(appid)

text = "遙か彼方に小形飛行機が見える。"

print(kousei.proofreading_support(text))

print(kousei.proofreading_support(text, 1))

print(kousei.proofreading_support(text, 0, 1))