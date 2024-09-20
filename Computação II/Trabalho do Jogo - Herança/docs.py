import random
import base

class Personalidades (base.Entidades):
    def __init__(self, fisicalidade, racionalidade, emocionalidade):
        super().__init__(fisicalidade, racionalidade, emocionalidade)
        self.banco_fisicalidade = ['Esse mundo precisava mesmo de um Estrondo', 'Essa é a maneira certa de parar de se preocupar sobre o Fim e amá-lo de uma vez por todas. Faça você mesmo! ;)',
        'Não há motivos para arrependimentos', 'Um novo mundo repleto de blasfêmia, tão belo!', 'A moral não se aplica nessa terra!']

        self.banco_combate_fisicalidade = ['Não há misericórdia', 'EXTERMINE\n\nEXTERMINE\n\n\EXTERMINE', 'Esse é o lugar onde os fracos não tem vez!',
        'Esse é um mundo sem redenção!', 'Expie pelos seus pecados!', 'People dont change. They just become more of who they really are']

        self.banco_racionalidade = ['Pelos meus cálculos, a chance de sobrevivência é de 5%. Vambora!', 'Radiação, monstros, solidão? TRIVIAL, deu até sorte de que a atmosfera não queimou junto haha',
        'Fim do Mundo? Tá mais pra uma sexta-feira no Fundão', 'Olhe pelo lado bom, não tem mais 500 planilhas para serem preenchidas no Excel', 'Como é bom finalmente aplicar meus conhecimentos de engenheiro nuclear']

        self.banco_combate_racionalidade = ['Com um bom torque, até o mais terrível dos monstros sucumbirá!', 'Beleza, se eu calcular o quanto ele se desloca, com uma simples derivada segunda é possível saber a...\nNÃO DÁ TEMPO!',
        '∫F(x) dx...\nÀs vezes, é só tentar não morrer mesmo, caramba!', 'Se eu derrotar essa aberração, as chances de sobrevivência aumentam em 0.00000000002%\nJá é um início!', 'Tem uma maneira bem simples de derrotá-lo: BOMBARDEAMENTO DE PÓSITRONS']

        self.banco_emocionalidade = ['Un jour je serai de retour près de toi', 'Surtando em:\n3...\n2...\n1', 'As estatuetas não a trarão de volta', 
        'together we will walk the waste land of reality', 'O canto insuportável das cigarras seria acolhedor num momento desses...']

        self.banco_combate_emocionalidade = ['E se eu errar? E se eu perder? E se tudo der errado?', 'Eu sou o Arauto do Oitavo Selo', 'Será que eu consigo lidar com tudo isso? Acho que vou surtar a qualquer momento',
        'Desculpa criaturinha, eu preciso ver o pôr do Sol mais uma vez', 'Como eu gostaria de naõ ter pressionado aquele maldito botão']
        

    def gerar_frase_aleatoria (self):
        aleatorio = random.choices(['fisicalidade', 'racionalidade', 'emocionalidade'], weights = [self.fisicalidade, self.racionalidade, self.emocionalidade], k = 1)
        if aleatorio[0] == 'fisicalidade':
            print('A FISICALIDADE grita em sua mente: '+ random.choice(self.banco_fisicalidade))
        elif aleatorio[0] == 'racionalidade':
            print('A RACIONALIDADE ecoa em sua mente: '+ random.choice(self.banco_racionalidade))
        else:    
            print('A EMOCIONALIDADE sussura em sua mente: '+ random.choice(self.banco_emocionalidade))
    
    def frase_combate(self, categoria):
        if categoria == 'fisicalidade':
            print('A FISICALIDADE grita em sua mente: '+ random.choice(self.banco_combate_fisicalidade ))
        elif categoria == 'racionalidade':
            print('A RACIONALIDADE ecoa em sua mente: '+ random.choice(self.banco_combate_racionalidade))
        else:    
            print('A EMOCIONALIDADE sussura em sua mente: '+ random.choice(self.banco_combate_emocionalidade))

introdução = """Olá, Engenheiro do Fim do Mundo!

Parabéns, você sobreviveu ao apocalipse nuclear. O seu maior pesadelo como Engenheiro Nuclear foi realizado!

O melhor de tudo é que você foi o responsável por apertar aquele botão vermelho que gerou todo esse caos!

Agora, você tem a chance única de enfrentar criaturas mutantes, passar por chuvas ácidas e algumas surpresinhas a mais.

Sua missão é simples: sobreviver. Ok, talvez não seja tão simples, mas, por enquanto, você é nossa única esperança (estamos lascados).

Então, você está pronto para, pelo menos, tentar não piorar as coisas?

Sua energia, vida e sanidade estão completos, e você tem 20 pontos para distribuir entre:

- Fisicalidade: Afeta sua força física;

- Racionalidade: Afeta suas capacidade de resolver problemas;

- Emocionalidade: Afeta sua estabilidade emocional.

De alguma forma, fisicalidade, racionalidade e emocionalidade falam através de você agora...

Como você quer distribuir esses pontos?"""

texto_saida_bunker = """Você sai do bunker e percebe que o mundo está pior do que nas suas piores previsões de desastre nuclear. O mundo está silencioso e afetado pela radioatividade.
Talvez voltar para o bunker não seja uma ideia tão ruim assim.. Quanto tempo será que a comida ainda vai durar?"""

texto_evento_1 = """Talvez seja coragem, talvez seja desespero, mas você saiu do bunker e vai explorar a região.

Você encontra um supermercado destruído e fica na dúvida se deve explorar o que ainda restou dentro dele ou continuar a sua jornada."""

texto_derrota = """Você sucumbe à dor\nMemórias de um passado longínquo começam a pipocar, a brisa da natureza move uma mecha de seu cabelo e você engole um pouco de seu próprio sangue.
Por um último instante, você sente falta de toda aquela confusão, desentendimentos, discussões\nVocê guardou a sensação daquele maldito abraço até a morte, hein?
É hora de descansar, caro humano..."""

texto_vitoria = """O futuro é incerto, mas você aprendeu a lutar e se tornou capaz de sobreviver. Os monstros continuarão à solta, lutando pela dominação, mas você também estará!"""

texto_agradecimento = 'Obrigado por jogar! :)'