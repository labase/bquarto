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
        self.build_tabuleiro()
        self.build_mao()
        
    def build_base(self):
        """docs here"""
        base = self.gui.rect(x=0, y= 0, width=BASE, height=BASE,
                      rx = RAIO, fill = "navajowhite")
        self.canvas <= base
    def build_tabuleiro(self):
        self.build_parte(ESP, LP + 2 * ESP, 4, 4)
    def build_mao(self):
        """docs here"""
        self.build_parte(ESP, ESP, 4, 2)
        self.build_parte(LG + 2 * ESP, LP + 2 * ESP, 2, 4)
    def build_parte(self, x, y, nch, ncv):
        rect = self.gui.rect(x=x, y= y,
          width=nch * PASSO + ESP, height= ncv * PASSO + ESP,
                      rx = RAIO, fill = "peru")
        self.canvas <= rect
        casas = [self.build_casa(self.canvas,
          ESP + RAIO + x + (c % nch) * PASSO,
          ESP + RAIO + y+ (c // nch) * PASSO) for c in range(nch * ncv)]
    def build_casa(self, lugar, x, y):
        casa = self.gui.ellipse(cx = x, cy = y,
          rx = RAIO, ry = RAIO, fill = "burlywood")
        lugar <= casa

