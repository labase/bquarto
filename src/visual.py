"""
############################################################
Quarto - Montagem Visual
############################################################

:Author: *Carlo E. T. Oliveira*
:Author: *Kyle Kuo*
:Contact: carlo@nce.ufrj.br
:Date: 2013/04/09
:Status: This is a "work in progress"
:Revision: 0.1.1
:Home: `Labase <http://labase.selfip.org/>`__
:Copyright: 2013, `GPL <http://is.gd/3Udt>`__.
"""
RAIO = 45
RAIOP = 1.618 * 45 /2
ESP = 10
PASSO = 2 * RAIO + ESP
LP = ESP + 2 * PASSO
LG = ESP + 4 * PASSO
BASE = LP + LG + 3 * ESP

class Visual:
    """Montagem das partes visuais."""
    def __init__(self, doc, gui):
        """Constroi as partes do Jogo. """
        self.gui = gui
        self.canvas = gui.svg(width = BASE, height = BASE)
        doc["main"] <= self.canvas
        self.build_base()
        #self.build_tabuleiro()
        #self.build_mao()
        
    def build_base(self):
        """docs here"""
        base = self.gui.rect(x=0, y= 0, width=BASE, height=BASE,
                      rx = RAIO, fill = "navajowhite")
        self.canvas <= base
    def build_tabuleiro(self):
        return self.build_parte(ESP, LP + 2 * ESP, 4, 4)
    def build_mao(self):
        """docs here"""
        mao1 = self.build_parte(ESP, ESP, 4, 2)
        mao2 = self.build_parte(LG + 2 * ESP, LP + 2 * ESP, 2, 4)
        return mao1 + mao2
    def build_parte(self, x, y, nch, ncv):
        rect = self.gui.rect(x=x, y= y,
          width=nch * PASSO + ESP, height= ncv * PASSO + ESP,
                      rx = RAIO, fill = "peru")
        self.canvas <= rect
        casas = [self.build_casa(self.canvas,
          ESP + RAIO + x + (c % nch) * PASSO,
          ESP + RAIO + y+ (c // nch) * PASSO)
                 for c in range(nch * ncv)]
        return casas
    def build_casa(self, lugar, x, y):
        casa = self.gui.g(transform = "translate(%d %d)"%(x, y))
        elipse = self.gui.ellipse(cx = 0, cy = 0,
          rx = RAIO, ry = RAIO, fill = "burlywood")
        casa <= elipse
        lugar <= casa
        return casa
    def build_pecas(self, lugar):
        print('build pecas')
        return [self.build_peca(umlugar, tipo)
                for tipo, umlugar in enumerate(lugar)]
    def build_peca(self, lugar, tipo):
        cores = ("sandybrown","saddlebrown")
        peca = self.gui.g()
        elipse = self.gui.ellipse(cx = 0, cy = 0,
          rx = RAIOP, ry = RAIOP, fill = cores[tipo % 2])
        peca <= elipse
        lugar <= peca
        print('peca')
        return peca

