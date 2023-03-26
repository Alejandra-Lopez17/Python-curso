import re

text = "Este es un ejemplo de una página web: https://github.com/Alejandra-Lopez17 y también podemos visitar https://github.com/Alejandra-Lopez17"

pattern = "https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.findall(pattern, text)

print(result)