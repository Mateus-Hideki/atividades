Alunos  = [
    {"nome":"Igor", "Idade":20, "prontuario":"SP12345", "notas portugues":6, "notas matematica":8, "notas ciencias":10, "media":8},
    {"nome":"ana", "Idade":19, "prontuario":"SP45678", "notas portugues":10, "notas matematica":3, "notas ciencias":9, "media":7.3}
]

def get_info():
    return Alunos

print(Alunos)

R  = input("deseja adicionar aluno?")

if (R == "s"):

    def add_aluno():
        nome = input("Nome")
        idade = input("Idade")
        prontuario = input("Prontuario")
        NP = input("Nota de porugues")
        NM = input("Nota de matematica")
        NC = input("Nota de ciencias")
        Media = (NP+NM+NC)/3
    
