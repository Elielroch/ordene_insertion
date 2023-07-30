class Sorter:
    def __init__(self):
        pass

    def ordene_selection(self, valores) -> [int]:
        return [1]

    def ordene_insertion(self, valores) -> [int]:
        t=len(valores)
        for i in range(1, t):
            chave = valores[i]
            j = i - 1
            while j >= 0 and chave < valores[j]:
                valores[j + 1] = valores[j]
                j -= 1
            valores[j + 1] = chave
        return valores


